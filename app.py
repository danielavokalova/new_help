from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="New Help Portal",
    page_icon="🛟",
    layout="wide",
    initial_sidebar_state="expanded",
)

css_file = Path(__file__).parent / "style.css"
if css_file.exists():
    st.markdown(f"<style>{css_file.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("## 🛟 New Help Portal")
    st.caption("Demo homepage")
    st.markdown("---")
    st.markdown("- Home")
    st.markdown("- AI Assistant (coming soon)")
    st.markdown("- Walkthroughs (coming soon)")
    st.markdown("- Agency Health (coming soon)")
    st.markdown("- What's New (coming soon)")

st.markdown(
    """
    <div class="hero">
        <h1>🛟 New Help Portal</h1>
        <p>Demo homepage with blue panel, smart search and topic tiles.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

CATEGORIES = [
    ("🏢", "Agency", "Profile, settings, branding", "index.md"),
    ("🤝", "Dealers", "Dealer accounts and commissions", "create-dealer.md"),
    ("👤", "Customers", "Passenger profiles and loyalty data", "create-customer.md"),
    ("🎫", "Reservations", "Create, modify and cancel bookings", "create-booking.md"),
    ("💰", "Prices & Markup", "Fares, markups and surcharges", "markup-rules.md"),
    ("📋", "Code Lists", "Carriers, destinations, cache", "carriers.md"),
    ("👥", "Users", "Agents, roles, passwords", "add-user.md"),
    ("🔔", "Notifications", "Email templates and alerts", "booking-confirmation.md"),
    ("📄", "Supporting Texts", "Terms, conditions, content blocks", "terms.md"),
    ("📈", "Statistics", "Reports and usage analytics", "sales-report.md"),
    ("⚙️", "Basic Settings", "First-time setup and core config", "service-fees.md"),
    ("🔬", "Advanced Settings", "APIs, connectors, webhooks", "advanced-api.md"),
]

POPULAR = [
    ("🔑", "How to reset an agent password", "Users", "reset-password.md"),
    ("➕", "Add a new user to your agency", "Users", "add-user.md"),
    ("✈️", "Create your first air reservation", "Reservations", "create-booking.md"),
    ("💸", "Set up agency markup rules", "Prices & Markup", "markup-rules.md"),
    ("📧", "Customise booking confirmation email", "Notifications", "booking-confirmation.md"),
    ("🔌", "Connect external APIs", "Advanced Settings", "advanced-connectors.md"),
]

query = st.text_input(
    label="Search",
    placeholder="🔍  Search anything... e.g. add user, markup, cancel booking",
    label_visibility="collapsed",
)

if query.strip():
    q = query.lower()
    hits = [row for row in POPULAR if q in f"{row[1]} {row[2]}".lower()]
    if hits:
        st.markdown("**Quick results:**")
        for icon, title, cat, target in hits:
            with st.expander(f"{icon} {title} · {cat}"):
                st.markdown(f"Open article: `{target}`")
    else:
        st.info("No direct match found. Try a broader keyword.")

st.markdown("### Browse by topic")

cols = st.columns(4)
for i, (icon, name, desc, target) in enumerate(CATEGORIES):
    with cols[i % 4]:
        st.markdown(
            f"""
            <div class="cat-card">
                <div class="cat-icon">{icon}</div>
                <div class="cat-name">{name}</div>
                <div class="cat-desc">{desc}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.caption(f"source: `{target}`")
    if (i + 1) % 4 == 0 and i < len(CATEGORIES) - 1:
        cols = st.columns(4)

st.divider()
st.markdown("### 🔥 Most visited")
for icon, title, cat, target in POPULAR:
    c1, c2 = st.columns([8, 2])
    with c1:
        st.markdown(f"{icon} **{title}**  <span class='badge'>{cat}</span>", unsafe_allow_html=True)
    with c2:
        st.caption(target)
