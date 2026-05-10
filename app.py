import streamlit as st

# Page config
st.set_page_config(page_title="EJ Strategic Solutions Portal", layout="wide")

# Title
st.title("Environmental Justice Leadership & Turn-Key Solutions")
st.subheader("State & District Reviewed Projects for SELA Community Impact")

st.write("""
This portal features fully developed, compliance-ready pilot programs and proposals 
designed for non-profits, for-profits, and government agencies.
""")

st.divider()

# Projects
col1, col2 = st.columns(2)

with col1:
    st.header("🏛️ Government & Regulatory Compliance")
    st.write("**Air Quality Monitoring Pilot**")
    st.write("A turn-key solution for real-time monitoring and violation prediction.")
    st.info("Status: Reviewed by District/State Agencies")

with col2:
    st.header("🧠 Community Health & Advocacy")
    st.write("**Brain Justice & Neuro-Protection Initiative**")
    st.write("Bridging the gap between environmental policy and cognitive health.")
    st.info("Status: Grant-Ready / Pilot Phase")

st.divider()

# Contact form
st.header("📩 Partner with Environmental Justice Leadership")
st.write("Contact us to learn more about our solutions.")

with st.form("contact_form"):
    name = st.text_input("Agency Name")
    email = st.text_input("Your Email")
    message = st.text_area("Which project are you interested in?")
    submitted = st.form_submit_button("Submit Inquiry")
    
    if submitted:
        st.success(f"Thank you {name}! We will contact you at {email}")
