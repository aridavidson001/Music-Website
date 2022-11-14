# streamlit_app.py

import streamlit as st
import pandas as pd

st.markdown("# Home")
st.sidebar.markdown("# Home")

st.header('Ari Davidson')
st.write('')

st.container()
col1, col2 = st.columns(2)
with col1:
  st.expander('Expander')
  with st.expander('About Me'):
    st.subheader('My Name Is Ari Davidson')
    st.write('Not much to say here')
    
with col2:
  st.expander('Expander')
  with st.expander('Recent Additions'):
    st.subheader('Song 1')
    tab1, tab2 = st.tabs(["Song 1","N.A"])
    with tab1:
      st.subheader('Song 1')
      st.write("Audio file example")
      audio_file = open("audio-sample.mp3", "rb")
      st.audio(audio_file.read())

    with tab2:
      st.subheader('N.A')
      st.write('N.A.')