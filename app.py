import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="DevWidget Lab",
    page_icon="",
    layout="wide"
)

# ---------- Custom Styling ----------
st.markdown("""
<style>

html, body, [class*="css"]{
background: linear-gradient(135deg,#0f172a,#1e293b,#0f172a);
}

.block-container{
padding-top:8rem;
text-align:center;
}

.title{
font-size:90px;
font-weight:800;
background: linear-gradient(90deg,#60a5fa,#a78bfa,#38bdf8);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
margin-bottom:20px;
}

.subtitle{
font-size:24px;
color:#cbd5e1;
margin-bottom:60px;
}

div.stButton > button{
background: linear-gradient(90deg,#3b82f6,#8b5cf6);
color:white;
font-size:26px;
padding:18px 50px;
border:none;
border-radius:18px;
box-shadow:0px 6px 25px rgba(99,102,241,.45);
transition:0.3s;
}

div.stButton > button:hover{
transform:scale(1.05);
box-shadow:0px 8px 30px rgba(99,102,241,.65);
}
</style>
""", unsafe_allow_html=True)

# ---------- Intro Screen ----------
st.markdown("""
<div class="title">
DevWidget Lab
</div>

<div class="subtitle">
Interactive UI Builder
</div>
""", unsafe_allow_html=True)


# ---------- Launch Button ----------
if st.button("Click Here To Launch DevWidget Lab"):

    st.markdown("""
    <h2 style='
    text-align:center;
    background:linear-gradient(90deg,#60a5fa,#a78bfa);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    margin-top:40px;'>
    Launching DevWidget...
    </h2>
    """, unsafe_allow_html=True)

    with open("devwidget.html","r",encoding="utf-8") as f:
        html_code=f.read()

    components.html(
        html_code,
        height=1000,
        scrolling=True
    )
