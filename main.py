import streamlit as st
import pyperclip

def add_bg_from_url():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://cdn.pixabay.com/photo/2022/04/22/17/33/forest-7150274_640.jpg");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def sentence_to_ascii(sentence):
    return [ord(char) for char in sentence]

def ascii_to_sentence(ascii_list):
    try:
        return ''.join(chr(num) for num in ascii_list)
    except ValueError:
        return "Invalid input! Ensure the ASCII list contains valid numbers."

# Add the background image
add_bg_from_url()

st.title("🎉 New Year Resolution Truth Sayer")

st.header("🔐 Secret Message Generator")
secret_message = st.text_input("Enter your New Year resolution (secret message):", "")

if st.button("Generate Secret Message"):
    if secret_message:
        ascii_list = sentence_to_ascii(secret_message)
        st.success("Your Secret Message (as a list of numbers):")
        st.code(ascii_list, language='python')
        st.title(" Copy the list through above Copy option")
    else:
        st.error("Please enter a message!")

st.divider()

st.header("🔓 Message Cracker")
ascii_input = st.text_area("Paste your secret message (list of numbers):", "")

if st.button("Crack the Message"):
    if ascii_input:
        try:
            ascii_list = list(map(int, ascii_input.strip('[]').split(',')))
            cracked_message = ascii_to_sentence(ascii_list)
            st.success("Your Cracked Message:")
            st.write(cracked_message)
            # Display hearts emojis and balloons
            st.markdown("❤️ ❤️ ❤️ 🎉")
            st.balloons()
        except ValueError:
            st.error("Invalid input! Please ensure the input is a list of numbers separated by commas.")
    else:
        st.error("Please paste your secret message!")
