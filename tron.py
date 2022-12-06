import streamlit as st
from PIL import Image

#ページ設定
st.set_page_config(layout="wide")
pagelist = ["KOGI", "Chat", "Code Translation"]
selector=st.sidebar.selectbox( "ページ選択",pagelist)

#TOP
if selector == "KOGI":
    st.title("KOGI")
    image = Image.open('images/KOGI_Project.png')
    st.image('images/KOGI_Project.png')


#Chat
elif selector == "Chat":
    st.title("Chat")
    video_file = open('videos/WCCE_GCD.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes, start_time=0)


#Code Translation
elif selector == "Code Translation":
    st.title("Code Translation")
    video_file = open('videos/WCCE_CT.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes, start_time=0)


