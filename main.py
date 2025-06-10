import streamlit as st
st.title("첫 aap")
st.write("hello")
name=st.text_input("이름 입력")
if name:
  if name=="hayate"
  st.success("반갑습니다. hayate님!")
else:
  st.warning("누구세요?")
