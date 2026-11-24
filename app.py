from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Eng. Rewan Badr | Claude AI Packages",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit chrome so the page looks standalone
st.markdown(
    """
    <style>
      #MainMenu, header, footer {visibility: hidden;}
      .stApp {background: #171113;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
      iframe {display: block;}
    </style>
    """,
    unsafe_allow_html=True,
)

html = (Path(__file__).parent / "index.html").read_text(encoding="utf-8")
components.html(html, height=2900, scrolling=True)
