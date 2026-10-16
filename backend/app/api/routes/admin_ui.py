import html

from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from sqlmodel import select

from app.api.deps import SessionDep
from app.api.routes.servers import (
    build_delivery_payload,
    build_renewal_whatsapp,
    compute_billing_status,
    compute_days_remaining,
    read_servers_summary,
)
from app.core.config import settings
from app.models import Client, Server

router = APIRouter(tags=["admin-ui"])


@router.get("/admin", response_class=HTMLResponse)
@router.get("/admin/", response_class=HTMLResponse, include_in_schema=False)
def render_admin_dashboard(session: SessionDep) -> HTMLResponse:
    """Serve the Consterna Cloud Dark Glassmorphism Operational CRM & Admin Panel."""
    summary = read_servers_summary(session=session, trm_cop=4000.0)
    servers = session.exec(select(Server)).all()

    rows_html: list[str] = []
    for srv in servers:
        client = session.get(Client, srv.owner_id)
        client_name = client.full_name if client else "Desconocido"
        external_id = (client.external_id if client and client.external_id else "-")
        phone = client.whatsapp_number if client and client.whatsapp_number else "-"
        billing_badge = compute_billing_status(srv.status, srv.expiration_date)
        days_rem = compute_days_remaining(srv.expiration_date)
        days_label = f"{days_rem} días" if days_rem is not None else "-"
        exp_str = (
            srv.expiration_date.strftime("%Y-%m-%d")
            if srv.expiration_date is not None
            else "-"
        )
        price_label = (
            f"${int(srv.monthly_price):,} COP".replace(",", ".")
            if (srv.currency or "").upper() == "COP"
            else f"${srv.monthly_price:.2f} USD"
        )
        _, reminder_wa_url = build_renewal_whatsapp(
            client_name=client_name,
            phone=client.whatsapp_number if client else None,
            game=srv.game,
            plan_name=srv.plan_name,
            monthly_price=srv.monthly_price,
            currency=srv.currency,
            expiration_date=srv.expiration_date,
        )
        delivery_obj = (
            build_delivery_payload(srv, client)
            if client is not None
            else None
        )
        delivery_text_escaped = (
            html.escape(delivery_obj.message, quote=True) if delivery_obj else ""
        )
        delivery_wa_escaped = (
            html.escape(delivery_obj.whatsapp_url, quote=True) if delivery_obj else "#"
        )

        badge_class = "badge-neutral"
        if "Al Día" in billing_badge:
            badge_class = "badge-ok"
        elif "Cobrar Pronto" in billing_badge:
            badge_class = "badge-warn"
        elif "Vencido" in billing_badge:
            badge_class = "badge-danger"

        rows_html.append(
            f"""
            <tr data-server-id="{srv.id}">
                <td><code>{html.escape(external_id)}</code></td>
                <td>
                    <strong>{html.escape(client_name)}</strong><br>
                    <small class="muted">📱 {html.escape(phone)}</small>
                </td>
                <td>
                    <strong>{html.escape(srv.game)}</strong><br>
                    <small class="muted">{html.escape(srv.plan_name)} · {html.escape(srv.extra_service)}</small>
                </td>
                <td><code>{html.escape(srv.ip_address or "Sin IP")}</code></td>
                <td>
                    <strong>{html.escape(price_label)}</strong><br>
                    <small class="muted">Costo Base: ${srv.host_cost_usd:.2f} USD</small>
                </td>
                <td>
                    <strong>{html.escape(exp_str)}</strong><br>
                    <small class="muted">{html.escape(days_label)}</small>
                </td>
                <td><span class="badge {badge_class}">{html.escape(billing_badge)}</span></td>
                <td><span class="status-pill">{html.escape(srv.status)}</span></td>
                <td class="actions-cell">
                    <a href="{html.escape(reminder_wa_url, quote=True)}" target="_blank" rel="noopener noreferrer" class="btn btn-wa" title="Enviar recordatorio de cobro en 1 clic">
                        💬 Recordatorio WA
                    </a>
                    <button type="button" class="btn btn-key" data-msg="{delivery_text_escaped}" data-wa="{delivery_wa_escaped}" data-srv="{srv.id}" onclick="openDeliveryModal(this)">
                        🔑 Llave en Mano
                    </button>
                </td>
            </tr>
            """
        )

    table_body = (
        "\n".join(rows_html)
        if rows_html
        else '<tr><td colspan="9" style="text-align:center;padding:2rem;">No hay servidores registrados. Usa el botón "Sincronizar desde Excel CRM".</td></tr>'
    )

    page_html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Consterna Cloud — Panel Operativo &amp; CRM (/admin)</title>
    <style>
        :root {{
            --bg-dark: #090d16;
            --card-bg: rgba(17, 25, 40, 0.78);
            --card-border: rgba(255, 255, 255, 0.12);
            --accent: #00f2fe;
            --accent-2: #4facfe;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --ok: #10b981;
            --warn: #f59e0b;
            --danger: #ef4444;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background: radial-gradient(circle at top right, #111c35 0%, var(--bg-dark) 65%);
            color: var(--text-main);
            min-height: 100vh;
            padding: 1.75rem;
            line-height: 1.5;
        }}
        .container {{ max-width: 1360px; margin: 0 auto; }}
        header {{
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            align-items: center;
            gap: 1rem;
            padding: 1.25rem 1.5rem;
            background: var(--card-bg);
            border: 1px solid var(--card-border);
            border-radius: 16px;
            backdrop-filter: blur(14px);
            margin-bottom: 1.5rem;
        }}
        .brand h1 {{
            font-size: 1.45rem;
            background: linear-gradient(90deg, var(--accent), var(--accent-2));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        .brand p {{ color: var(--text-muted); font-size: 0.9rem; }}
        .auth-bar {{
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            align-items: center;
        }}
        .auth-bar input {{
            background: rgba(15, 23, 42, 0.9);
            border: 1px solid var(--card-border);
            color: var(--text-main);
            padding: 0.45rem 0.75rem;
            border-radius: 8px;
            font-size: 0.85rem;
        }}
        .btn {{
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
            padding: 0.5rem 0.9rem;
            border-radius: 8px;
            font-size: 0.84rem;
            font-weight: 600;
            border: 1px solid transparent;
            cursor: pointer;
            text-decoration: none;
            transition: all 0.2s ease;
        }}
        .btn-primary {{
            background: linear-gradient(135deg, var(--accent), var(--accent-2));
            color: #06101e;
        }}
        .btn-sync {{
            background: rgba(16, 185, 129, 0.18);
            color: #34d399;
            border-color: rgba(16, 185, 129, 0.4);
        }}
        .btn-wa {{
            background: rgba(37, 211, 102, 0.16);
            color: #4ade80;
            border-color: rgba(37, 211, 102, 0.4);
        }}
        .btn-key {{
            background: rgba(79, 172, 254, 0.16);
            color: #7dd3fc;
            border-color: rgba(79, 172, 254, 0.4);
        }}
        .kpi-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 1rem;
            margin-bottom: 1.5rem;
        }}
        .kpi-card {{
            background: var(--card-bg);
            border: 1px solid var(--card-border);
            border-radius: 14px;
            padding: 1.15rem 1.3rem;
            backdrop-filter: blur(12px);
        }}
        .kpi-card .label {{ color: var(--text-muted); font-size: 0.82rem; text-transform: uppercase; letter-spacing: 0.04em; }}
        .kpi-card .value {{ font-size: 1.7rem; font-weight: 800; margin-top: 0.3rem; color: var(--text-main); }}
        .kpi-card .sub {{ font-size: 0.8rem; color: var(--text-muted); margin-top: 0.25rem; }}
        .panel {{
            background: var(--card-bg);
            border: 1px solid var(--card-border);
            border-radius: 16px;
            padding: 1.25rem;
            backdrop-filter: blur(12px);
            overflow-x: auto;
        }}
        .panel-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 0.8rem;
            margin-bottom: 1rem;
        }}
        table {{ width: 100%; border-collapse: collapse; font-size: 0.88rem; }}
        th, td {{ padding: 0.8rem 0.75rem; text-align: left; border-bottom: 1px solid rgba(255, 255, 255, 0.07); }}
        th {{ color: var(--text-muted); font-weight: 600; font-size: 0.78rem; text-transform: uppercase; }}
        .muted {{ color: var(--text-muted); }}
        code {{ background: rgba(15, 23, 42, 0.8); padding: 0.15rem 0.4rem; border-radius: 5px; color: #7dd3fc; }}
        .badge {{
            display: inline-block;
            padding: 0.25rem 0.65rem;
            border-radius: 999px;
            font-size: 0.78rem;
            font-weight: 700;
        }}
        .badge-ok {{ background: rgba(16, 185, 129, 0.18); color: #34d399; }}
        .badge-warn {{ background: rgba(245, 158, 11, 0.2); color: #fbbf24; }}
        .badge-danger {{ background: rgba(239, 68, 68, 0.2); color: #f87171; }}
        .badge-neutral {{ background: rgba(148, 163, 184, 0.15); color: #cbd5e1; }}
        .status-pill {{ font-weight: 600; color: #e2e8f0; }}
        .actions-cell {{ display: flex; gap: 0.45rem; flex-wrap: wrap; }}
        .modal-backdrop {{
            display: none;
            position: fixed;
            inset: 0;
            background: rgba(5, 8, 16, 0.8);
            align-items: center;
            justify-content: center;
            padding: 1rem;
            z-index: 50;
        }}
        .modal {{
            background: #0f172a;
            border: 1px solid var(--card-border);
            border-radius: 16px;
            max-width: 600px;
            width: 100%;
            padding: 1.5rem;
        }}
        .modal textarea {{
            width: 100%;
            height: 210px;
            margin: 0.85rem 0;
            background: #090d16;
            color: var(--text-main);
            border: 1px solid var(--card-border);
            border-radius: 10px;
            padding: 0.85rem;
            font-family: inherit;
            font-size: 0.88rem;
        }}
        #statusBanner {{
            margin-bottom: 1rem;
            padding: 0.75rem 1rem;
            border-radius: 10px;
            display: none;
            font-size: 0.88rem;
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <div class="brand">
                <h1>☁️ Consterna Cloud — Centro de Control Operativo v1.9.0</h1>
                <p>Gestión CRM, Semáforo de Cobros, Entrega "Llave en Mano" y División 50/50 (Cristian &amp; Víctor)</p>
            </div>
            <form class="auth-bar" onsubmit="handleLogin(event)">
                <input type="email" id="adminEmail" placeholder="Email Admin" value="{html.escape(str(settings.FIRST_SUPERUSER))}" required aria-label="Email de administrador">
                <input type="password" id="adminPassword" placeholder="Contraseña JWT" required aria-label="Contraseña de administrador">
                <button type="submit" class="btn btn-primary">🔐 Conectar JWT</button>
                <button type="button" class="btn btn-sync" onclick="syncFromExcel()">🔄 Sincronizar desde Excel CRM</button>
            </form>
        </header>

        <div id="statusBanner" role="status" aria-live="polite"></div>

        <section class="kpi-grid" aria-label="Indicadores Financieros y Operativos">
            <div class="kpi-card">
                <div class="label">💰 MRR Bruto Estimado (USD)</div>
                <div class="value" id="kpiMrr">${summary.mrr_usd_estimated:.2f} USD</div>
                <div class="sub">Tasa base: {int(summary.trm_cop_usd)} COP/USD · {summary.active_servers} servidores activos</div>
            </div>
            <div class="kpi-card">
                <div class="label">📉 Costo Kinetic Hosting (USD)</div>
                <div class="value" id="kpiCost">${summary.host_cost_usd_total:.2f} USD</div>
                <div class="sub">Egreso mensual de infraestructura activa</div>
            </div>
            <div class="kpi-card">
                <div class="label">🚀 Ganancia Neta Total (USD)</div>
                <div class="value" id="kpiNet">${summary.net_profit_usd:.2f} USD</div>
                <div class="sub">Setup / Modpacks únicos: ${summary.one_time_fees_usd_total:.2f} USD</div>
            </div>
            <div class="kpi-card">
                <div class="label">🤝 División 50/50 (Cristian &amp; Víctor)</div>
                <div class="value" id="kpiSplit">${summary.partner_split_50_50_usd:.2f} USD c/u</div>
                <div class="sub">Cristian: ${summary.partner_split_50_50_usd:.2f} · Víctor: ${summary.partner_split_50_50_usd:.2f}</div>
            </div>
            <div class="kpi-card">
                <div class="label">🔔 Alertas de Renovación</div>
                <div class="value" id="kpiAlerts">{summary.expiring_soon_count + summary.overdue_count}</div>
                <div class="sub">🟡 Cobrar pronto: {summary.expiring_soon_count} · 🔴 Vencidos: {summary.overdue_count}</div>
            </div>
        </section>

        <section class="panel" aria-label="Tabla de Clientes y Servidores">
            <div class="panel-header">
                <h2>👥 Clientes y Servidores ({summary.total_clients} clientes / {summary.total_servers} servidores)</h2>
                <span class="muted">Semáforo: 🟢 Al Día | 🟡 Cobrar Pronto (&le;4 días) | 🔴 Vencido</span>
            </div>
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Cliente / WhatsApp</th>
                        <th>Juego / Plan RAM</th>
                        <th>IP / Puerto</th>
                        <th>Mensualidad</th>
                        <th>Próximo Corte</th>
                        <th>Semáforo</th>
                        <th>Estado</th>
                        <th>Acciones 1-Clic</th>
                    </tr>
                </thead>
                <tbody>
                    {table_body}
                </tbody>
            </table>
        </section>
    </div>

    <div class="modal-backdrop" id="deliveryModal">
        <div class="modal" role="dialog" aria-modal="true" aria-labelledby="modalTitle">
            <h3 id="modalTitle">🔑 Mensaje de Entrega "Llave en Mano"</h3>
            <textarea id="deliveryTextarea" readonly aria-label="Mensaje de entrega Llave en Mano"></textarea>
            <div style="display:flex;gap:0.6rem;justify-content:flex-end;flex-wrap:wrap;">
                <button type="button" class="btn btn-key" onclick="copyDeliveryText()">📋 Copiar Mensaje</button>
                <a id="deliveryWaLink" href="#" target="_blank" rel="noopener noreferrer" class="btn btn-wa">🟢 Enviar por WhatsApp</a>
                <button type="button" class="btn" style="background:#1e293b;color:#f8fafc;" onclick="closeDeliveryModal()">Cerrar</button>
            </div>
        </div>
    </div>

    <script>
        var jwtToken = sessionStorage.getItem("consterna_jwt") || "";

        function showBanner(msg, isError) {{
            var el = document.getElementById("statusBanner");
            el.style.display = "block";
            el.style.background = isError ? "rgba(239, 68, 68, 0.2)" : "rgba(16, 185, 129, 0.2)";
            el.style.border = isError ? "1px solid #ef4444" : "1px solid #10b981";
            el.textContent = msg;
        }}

        if (jwtToken) {{
            showBanner("✅ Sesión JWT administrativa activa en este navegador.", false);
        }}

        function handleLogin(e) {{
            e.preventDefault();
            var email = document.getElementById("adminEmail").value;
            var pwd = document.getElementById("adminPassword").value;
            var body = new URLSearchParams();
            body.append("username", email);
            body.append("password", pwd);

            fetch("{settings.API_V1_STR}/login/access-token", {{
                method: "POST",
                headers: {{ "Content-Type": "application/x-www-form-urlencoded" }},
                body: body.toString()
            }})
            .then(function(r) {{
                if (!r.ok) throw new Error("Credenciales inválidas");
                return r.json();
            }})
            .then(function(data) {{
                jwtToken = data.access_token;
                sessionStorage.setItem("consterna_jwt", jwtToken);
                showBanner("✅ Sesión JWT activa para operaciones administrativas.", false);
            }})
            .catch(function(err) {{
                showBanner("❌ Error de autenticación: " + err.message, true);
            }});
        }}

        function syncFromExcel() {{
            if (!jwtToken) {{
                showBanner("⚠️ Primero inicia sesión con tu contraseña de administrador para sincronizar.", true);
                return;
            }}
            fetch("{settings.API_V1_STR}/utils/sync-excel", {{
                method: "POST",
                headers: {{ "Authorization": "Bearer " + jwtToken }}
            }})
            .then(function(r) {{
                if (!r.ok) throw new Error("No autorizado o error al sincronizar");
                return r.json();
            }})
            .then(function(data) {{
                showBanner("✅ " + data.message + " Recargando panel...", false);
                setTimeout(function() {{ window.location.reload(); }}, 900);
            }})
            .catch(function(err) {{
                showBanner("❌ " + err.message, true);
            }});
        }}

        function openDeliveryModal(btn) {{
            var msg = btn.getAttribute("data-msg") || "";
            var wa = btn.getAttribute("data-wa") || "#";
            document.getElementById("deliveryTextarea").value = msg;
            document.getElementById("deliveryWaLink").href = wa;
            document.getElementById("deliveryModal").style.display = "flex";
        }}

        function closeDeliveryModal() {{
            document.getElementById("deliveryModal").style.display = "none";
        }}

        function copyDeliveryText() {{
            var area = document.getElementById("deliveryTextarea");
            area.focus();
            area.select();
            area.setSelectionRange(0, 99999);
            var copied = false;
            if (navigator.clipboard && window.isSecureContext) {{
                navigator.clipboard.writeText(area.value).then(function() {{
                    showBanner("📋 Mensaje 'Llave en Mano' copiado al portapapeles.", false);
                }}).catch(function() {{
                    try {{
                        copied = document.execCommand("copy");
                        showBanner(copied ? "📋 Mensaje 'Llave en Mano' copiado al portapapeles." : "❌ No se pudo copiar automáticamente. Por favor selecciónalo y cópialo.", !copied);
                    }} catch (e) {{
                        showBanner("❌ Error al copiar texto.", true);
                    }}
                }});
                return;
            }}
            try {{
                copied = document.execCommand("copy");
                showBanner(copied ? "📋 Mensaje 'Llave en Mano' copiado al portapapeles." : "❌ No se pudo copiar automáticamente. Por favor selecciónalo y cópialo.", !copied);
            }} catch (e) {{
                showBanner("❌ Error al copiar texto.", true);
            }}
        }}
    </script>
</body>
</html>"""
    return HTMLResponse(content=page_html, status_code=200)
