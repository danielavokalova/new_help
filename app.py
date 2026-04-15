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

SECTIONS_LEFT = [
    (
        "Produkty",
        [
            ("AC", "https://bo.golibe.com/"),
            ("IMPLEMENTACE", "https://docs.google.com/spreadsheets/d/18cAQwVzeSfboPnsGZ81aw8PVmEIUmxRQ9Rmly6b7bS4/edit"),
            ("GOL IBE MEETINGS", "https://docs.google.com/spreadsheets/d/1cvwpJnr7AdIddGa4R8WFH7j3He9SOgbppY-6e-zeViw/edit"),
            ("TM AC", "https://admin-console.tripmanager.com/"),
            ("TRIPGATE TCP", "https://www.travelcloudpro.com/#/login?returnTo=%2Fcbt%2Fcorporates"),
        ],
    ),
    (
        "Tools and Sources",
        [
            ("MANUALY NOTION", "https://www.notion.so/cee-travel-systems/209a7099a10f807d956cd34b5a96ade4?v=209a7099a10f80449ccc000ca457ae7e"),
            ("VDV", "https://docs.google.com/spreadsheets/d/1PwXopixBNOhwgZTDGmHUTCzz9dZPqtHiGZIkAVO4aw0/edit"),
            ("ZALETSI", "https://docs.google.com/spreadsheets/d/1F1HjyKIFm5dDzMzM1-GAIKnH13lbHRYgYWgArbI00yg/edit"),
            ("PATEK REPORT", "https://docs.google.com/spreadsheets/d/1vV6rIQCL9OCMG9xSV1OrXYyZldABPSe8CwF7_wPCLiQ/edit?gid=0#gid=0"),
            ("PODIO", "https://podio.com/home"),
        ],
    ),
    (
        "Data",
        [
            ("METABASE", "http://localhost:3000/dashboard/2-gol-dashboard-v1"),
            ("AIR RESERVATIONS", "https://github.com/danielavokalova/new_help"),
        ],
    ),
    (
        "Other",
        [
            ("ZENDESK", "https://cee-support.zendesk.com/agent/filters/65499989"),
            ("KARLIN", "https://docs.google.com/spreadsheets/d/1c-T04jgfgC1aMb-XUcvGKN6R0nuqEHVZZKcvt6uV_Q4/edit?gid=0#gid=0"),
            ("TO DO", "https://danielavokalova.github.io/task-dashboard/task-dashboard.html"),
            ("IDEAS", "https://danielavokalova.github.io/dashboard/ideas.html"),
            ("AGENT KALENDAR", "https://calendar.google.com/calendar/u/0/r"),
        ],
    ),
]

SECTIONS_RIGHT = [
    (
        "Gitlab",
        [
            ("MAGIC", "https://gitlab.in.cee-systems.com/gol-support/frontends/-/blob/master/etc/d4_frontends.yml"),
            ("DEVELOPMENT", "https://gitlab.in.cee-systems.com/support/project-management/-/boards"),
            ("SUPPORT", "https://gitlab.in.cee-systems.com/support/support/-/work_items"),
        ],
    ),
    (
        "AI",
        [
            ("AI VYHLEDAVANI", "https://github.com/danielavokalova/new_help"),
            ("AI NAVRHY OBSAHU", "https://github.com/danielavokalova/new_help"),
            ("AI FAQ", "https://github.com/danielavokalova/new_help"),
        ],
    ),
]

if "dashboard_notes" not in st.session_state:
    st.session_state.dashboard_notes = ""

with st.sidebar:
    st.markdown("## 🛟 New Help Portal")
    st.caption("Dashboard demo")
    st.markdown("---")
    st.markdown("### Rychlé odkazy")
    st.link_button("EMAIL", "mailto:")
    st.link_button("KALENDAR", "https://calendar.google.com/calendar/u/0/r")

st.markdown(
    """
    <div class="hero">
        <h1>🛟 New Help Portal</h1>
        <p>Dashboard + AI příprava + pracovní dlaždice.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

query = st.text_input(
    label="Search",
    placeholder="🔍  Search in tile names...",
    label_visibility="collapsed",
)


def show_tile_grid(items, cols_count=3):
    cols = st.columns(cols_count)
    for idx, (title, url) in enumerate(items):
        with cols[idx % cols_count]:
            st.link_button(title, url, use_container_width=True)


def section_matches(items, q):
    if not q:
        return items
    needle = q.lower().strip()
    return [(t, u) for t, u in items if needle in t.lower()]


main_col, side_col = st.columns([4.8, 1.8], gap="large")

with main_col:
    content_left, content_right = st.columns(2, gap="large")

    with content_left:
        for section_name, tiles in SECTIONS_LEFT:
            filtered = section_matches(tiles, query)
            if query and not filtered:
                continue
            st.markdown(f"### {section_name}")
            show_tile_grid(filtered, cols_count=2)
            st.markdown("")

    with content_right:
        for section_name, tiles in SECTIONS_RIGHT:
            filtered = section_matches(tiles, query)
            if query and not filtered:
                continue
            st.markdown(f"### {section_name}")
            show_tile_grid(filtered, cols_count=2)
            st.markdown("")

with side_col:
    st.markdown("### POZNAMKY")
    st.session_state.dashboard_notes = st.text_area(
        "Poznamky",
        value=st.session_state.dashboard_notes,
        label_visibility="collapsed",
        height=420,
        placeholder="Klidne poznamky...",
    )
