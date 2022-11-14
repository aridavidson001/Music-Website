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
      st.audio("https://drive.google.com/file/d/11yN6IWu-Sw9LBokVSUp-VJ5j31PIt9a0/view?usp=sharing")

    with tab2:
      st.subheader('N.A')
      st.write('N.A.')
