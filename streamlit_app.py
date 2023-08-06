import streamlit as st
import streamlit_analytics

with streamlit_analytics():
  st.text_input("write you name")
  st.selectbox("select you favorite", ["guvi","data","science"])
  st.button("click me")
