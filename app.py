
import streamlit as st

st.title("🧮 Agentic Calculator")

# Columns
col1, col2 = st.columns(2)

with col1:
    first_number=st.number_input('First Number', value=0)

with col2:
    second_number=st.number_input('Second Number', value=0)

    operation = st.selectbox('Select your Operation:', ["Add", "Subtract", "Multiply","Divide"])
    if st.button('Calculate'):
      if operation == "Add":
        result = first_number + second_number
        st.success(f"The result is {result}")
      elif operation == "Subtract":
        result = first_number - second_number
        st.success(f"The result is {result}")
      elif operation == "Multiply":
        result = first_number * second_number
        st.success(f"The result is {result}")
      elif operation == "Divide":
        result = first_number / second_number
        st.success(f"The result is {result}")
      else:
        st.warning("Invalid Operation")
