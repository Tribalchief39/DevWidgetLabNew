import streamlit as st
import streamlit.components.v1 as components
import time

st.set_page_config(
    page_title="DevWidget Lab",
    page_icon="⚡",
    layout="wide"
)

# ---------------- Styling ----------------
st.markdown("""
<style>
.main {
background: linear-gradient(to right,#0f172a,#1e293b);
color:white;
}

.hero{
text-align:center;
padding-top:60px;
padding-bottom:60px;
}

.title{
font-size:70px;
font-weight:800;
}

.subtitle{
font-size:24px;
color:#cbd5e1;
}

.feature-box{
background:#1e293b;
padding:25px;
border-radius:20px;
box-shadow:0px 4px 20px rgba(0,0,0,.25);
}

div.stButton > button{
font-size:22px;
padding:15px 35px;
border-radius:15px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- Intro Screen ----------------
st.markdown("""
<div class='hero'>
<div class='title'>⚡ DevWidget Lab</div>

<div class='subtitle'>
Visual UI Component Builder using HTML, CSS, JS + Python Streamlit
</div>

</div>
""", unsafe_allow_html=True)

st.success("Integrated Python + Frontend Project")

# loading effect
with st.spinner("Launching DevWidget Platform..."):
    time.sleep(2)

# ---------------- Overview ----------------
st.header("📌 Project Overview")

c1,c2,c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class='feature-box'>
    <h3>🎨 UI Components</h3>
    Buttons, cards and reusable widgets.
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class='feature-box'>
    <h3>⚙ Interactive Builder</h3>
    Build and customize visually.
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class='feature-box'>
    <h3>💻 Code Generation</h3>
    Generate production-ready code.
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ---------------- Launch HTML Project ----------------
st.header("🚀 Launch Main Project")

st.write("Click below to open the DevWidget HTML project inside Streamlit.")

if st.button("Open DevWidget Lab"):

    st.balloons()

    with open("devwidget.html","r",encoding="utf-8") as f:
        html_code = f.read()

    components.html(
        html_code,
        height=1000,
        scrolling=True
    )


# ---------------- About ----------------
with st.expander("About This Project"):
    st.write("""
Technologies Used:
- Python Streamlit
- HTML
- CSS
- JavaScript

Streamlit provides the dashboard and launcher.
The main component builder runs through the integrated HTML project.
""")

st.caption("Submitted as Python + Web Integrated Project")