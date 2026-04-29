import streamlit as st

st.set_page_config(
    page_title="DevWidget Lab",
    layout="wide"
)

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
margin-bottom:25px;
}

.subtitle{
font-size:24px;
color:#cbd5e1;
margin-bottom:60px;
}

.launch-btn{
display:inline-block;
padding:18px 45px;
font-size:26px;
font-weight:bold;
text-decoration:none;
color:white !important;
border-radius:18px;
background:linear-gradient(90deg,#3b82f6,#8b5cf6);
box-shadow:0px 8px 30px rgba(99,102,241,.45);
transition:.3s;
}

.launch-btn:hover{
transform:scale(1.05);
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class='title'>
DevWidget Lab
</div>

<div class='subtitle'>
Interactive UI Builder
</div>

<a class="launch-btn"
href="devwidget.html"
target="_blank">
Click Here To Launch DevWidget Lab
</a>
""", unsafe_allow_html=True)
