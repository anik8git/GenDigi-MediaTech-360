import streamlit as st
import pandas as pd

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="GenDigi Media Tech | 360° Digital + Print + Media",
    page_icon="🌍",
    layout="wide"
)

# ---------------------------------------------------
# CUSTOM CSS FOR CORPORATE PREMIUM THEME (A)
# ---------------------------------------------------
st.markdown(
    """
    <style>
        .stApp {
            background: radial-gradient(circle at top, #111827 0, #020617 45%, #000000 100%);
            color: #e5e7eb;
            font-family: "Inter", sans-serif;
        }
        .section-title {
            font-size: 1.4rem;
            font-weight: 700;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.title("🌍 GenDigi Media Tech")
menu = st.sidebar.radio(
    "Navigate",
    ["Home", "Services", "Automation", "Print & Branding", "Media", "Results", "SEO Keywords", "Contact"]
)

# ------------------------
# HOME
# ------------------------
if menu == "Home":
    st.title("🚀 GenDigi Media Tech — Your 360° Digital + Print + Media Powerhouse")
    st.write("""
    We deliver **Digital Marketing + API Automation + Branding + Outdoor Media**
    under one strategic ecosystem.
    """)

# ------------------------
# SERVICES
# ------------------------
elif menu == "Services":
    st.header("💼 Core Services")
    st.write("""
    ✔ Digital Marketing  
    ✔ Website / Software / Apps  
    ✔ Print & Branding  
    ✔ 360° Media & Advertising  
    """)

# ------------------------
# AUTOMATION
# ------------------------
elif menu == "Automation":
    st.header("🧩 API & Automation Division")
    st.write("""
    - WhatsApp Business API  
    - SMS / Email / Chatbot Automation  
    - Lead Capture + CRM API  
    - Payment Gateway + E-commerce APIs  
    """)

# ------------------------
# PRINT
# ------------------------
elif menu == "Print & Branding":
    st.header("🖨️ Print Media & Branding")
    st.write("""
    - Visiting Cards, Brochures, Flyers  
    - Logo, Packaging, Brand Guidelines  
    - Political Collaterals + Smart QR Prints  
    """)

# ------------------------
# MEDIA
# ------------------------
elif menu == "Media":
    st.header("🌐 360° Media & Advertising")
    st.write("""
    - Digital Ads: Meta, Google, YouTube  
    - Outdoor: Hoardings, Autos, Local Screens  
    - Events, Activations, Roadshows  
    """)

# ------------------------
# RESULTS
# ------------------------
elif menu == "Results":
    st.header("📈 Case Study")
    case_data = {
        "Metric": ["Leads/Month", "Google Rank", "Media Presence"],
        "Before": ["22", "Not Visible", "Zero"],
        "After": ["380+", "7 Keywords Page 1", "Digital + Outdoor"]
    }
    st.dataframe(pd.DataFrame(case_data))

# ------------------------
# SEO
# ------------------------
elif menu == "SEO Keywords":
    st.header("🔍 SEO Keywords")
    st.write("""
    - 360 marketing agency in India  
    - WhatsApp API provider  
    - Website development Pune  
    """)

# ------------------------
# CONTACT
# ------------------------
elif menu == "Contact":
    st.header("📞 Contact")
    st.write("""
    📍 Pune, Maharashtra  
    📱 +91 77448 57516  
    ✉️ info@gendigimediatech.com  
    """)

