import streamlit as st
from youtubeagent import create_youtube_agent

st.set_page_config(page_title="Vara-YoutubevideoAnalyzer",page_icon="🎥",)

st.markdown('<h1 style="white-space: nowrap; font-size: 2.5rem;color: #FF0000">🎥 VARA - Youtube Video Shorts Analyzer</h1>', unsafe_allow_html=True)



@st.cache_resource
def get_agent():
    return create_youtube_agent()

Video_url = st.text_input("Enter youtube link")
Button = st.button("Analyze Video")
agent = get_agent()

if Button:
    if not Video_url.strip():
        st.error("Please Enter valid youtube link")
    else:      
        with st.spinner("Analyzing ...."):
            response = agent.run(f"Analyzing this video {Video_url}")
            response.content
   
            