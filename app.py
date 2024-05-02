import streamlit as st
import math

def calculate_tokens(input_type, input_value):
    if input_type == "Words":
        tokens = math.ceil(input_value / 6.5 * 4)
    else:  # input_type == "Characters"
        tokens = math.ceil(input_value * 4)
    return tokens

def main():
    st.title("Token Calculator")
    
    input_type = st.radio("Select input type:", ("Words", "Characters"))
    
    if input_type == "Words":
        input_value = st.number_input("Enter the number of words:", min_value=1, step=1)
    else:  # input_type == "Characters"
        input_value = st.number_input("Enter the number of characters:", min_value=1, step=1)
    
    if st.button("Calculate"):
        tokens = calculate_tokens(input_type, input_value)
        st.success(f"The estimated number of tokens is: {tokens}")

if __name__ == "__main__":
    main()
