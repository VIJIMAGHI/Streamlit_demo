import streamlit as st
st.title("My new streamlit app")
st.header("welcome")
st.write("your details here")
name=st.text_input("what is your name")
if name:
	st.success(f"hello {name}!")
age=st.slider("your age is",1,25,100)
st.write(f"you selected {age}")