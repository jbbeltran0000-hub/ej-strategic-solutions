import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="EJ Strategic Solutions Portal", layout="wide")

# --- CUSTOM CSS FOR BRANDING ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #2e7d32; color: white; }
    .project-card { padding: 20px; border-radius: 10px; background-color: white; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SECTION ---
st.title("Environmental Justice Leadership & Turn-Key Solutions")
st.subheader("State & District Reviewed Projects for SELA Community Impact")
st.write("""
    This portal features fully developed, compliance-ready pilot programs and proposals 
    designed for non-profits, for-profits, and government agencies. These projects 
    are grant-ready and have been presented to California state and district agencies.
""")

st.divider()

# --- PROJECT CATEGORIES ---
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🏛️ Government & Regulatory Compliance")
    with st.expander("Air Quality Monitoring Pilot"):
        st.write("A turn-key solution for real-time monitoring and violation prediction.")
        st.info("Status: Reviewed by District/State Agencies")
        st.write("📄 **Document:** air_quality_proposal.pdf")
        st.button("Request Full Documentation", key="btn1")

with col2:
    st.markdown("### 🧠 Community Health & Advocacy")
    with st.expander("Brain Justice & Neuro-Protection Initiative"):
        st.write("Bridging the gap between environmental policy and cognitive health.")
        st.info("Status: Grant-Ready / Pilot Phase")
        st.write("📄 **Document:** brain_justice_initiative.pdf")
        st.button("View Executive Summary", key="btn2")

# --- ADDITIONAL PROJECTS SECTION ---
st.divider()
st.markdown("### 📚 Additional Resources & Solutions")

with st.expander("📋 View All Available Documents"):
    st.write("**Available Turn-Key Solutions:**")
    
    resources = [
        "📄 air_quality_proposal.pdf - Air Quality Monitoring Pilot",
        "📄 brain_justice_initiative.pdf - Brain Justice & Neuro-Protection",
        "📄 implementation_guide.pdf - Implementation Guide",
        "📄 grant_application_template.pdf - Grant Application Template"
    ]
    
    for resource in resources:
        st.write(resource)

# --- TECHNICAL SUBMISSION SECTION ---
st.divider()
st.markdown("### 📩 Partner with Environmental Justice Leadership")
contact_form = """
<form action="https://formsubmit.co/Jbbeltran0000@gmail.com" method="POST">
     <input type="text" name="name" placeholder="Agency Name" required style="width:100%; margin-bottom:10px; padding:8px; border:1px solid #ddd; border-radius:5px;">
     <input type="email" name="email" placeholder="Your Email" required style="width:100%; margin-bottom:10px; padding:8px; border:1px solid #ddd; border-radius:5px;">
     <textarea name="message" placeholder="Which project are you interested in implementing?" style="width:100%; margin-bottom:10px; height:100px; padding:8px; border:1px solid #ddd; border-radius:5px;"></textarea>
     <button type="submit" style="background-color:#2e7d32; color:white; border:none; padding:10px; border-radius:5px; width:100%; cursor:pointer; font-weight:bold;">Submit Inquiry</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)

st.sidebar.title("Navigation")
st.sidebar.info("Select a project category above to view details.")

st.sidebar.divider()
st.sidebar.markdown("### 📤 How to Add Your PDFs")
st.sidebar.markdown("""
1. **Upload PDFs to GitHub**
   - Go to your repository
   - Click "Add file" → "Upload files"
   - Add PDF files to the repository root

2. **Supported Documents**
   - air_quality_proposal.pdf
   - brain_justice_initiative.pdf
   - implementation_guide.pdf
   - grant_application_template.pdf

3. **Auto-Download Feature**
   - Once files are uploaded, download buttons will appear automatically
""")
