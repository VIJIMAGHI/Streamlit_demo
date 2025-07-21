import streamlit as st
num1= st.number_input("enter num1")
num2=st.number_input("enter num2")
operations=st.selectbox("operation select:",["add","sub","mul","div"])
if st.button("calculate"):
	if operations=="add":
		result=num1+num2
	elif operations=="sub":
		result=num1-num2
	elif operations=="mul":
		result=num1*num2
	elif operations=="div":
		result=num1/num2 if num2!=0 else "cannot divide"
st.success(f"result is {result}")
	