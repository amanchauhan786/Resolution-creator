import streamlit as st
import random
import pyperclip

def add_bg_from_url():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://static.vecteezy.com/system/resources/previews/040/718/456/non_2x/ai-generated-sunset-silhouette-nature-mystery-in-a-dark-mountain-landscape-generated-by-ai-free-photo.jpg");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        .big-font {{
            font-size: 24px;
            font-weight: bold;
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

def get_random_shayari():
    shayaris = [
        "ज़िंदगी से पूछिए ये क्या चाहती है, क्योंकि हर सवाल का जवाब मोहब्बत नहीं होता।",
        "तेरे बिना ज़िंदगी अधूरी सी लगती है, जैसे किताब के पन्ने बिना लिखावट के।",
        "चाँदनी रातें भी डरावनी लगती हैं, जब दिल में तेरी यादों का शोर होता है।",
        "इश्क़ वो खेल नहीं जो हर कोई खेल सके, जान लुटानी पड़ती है इसे जीतने के लिए।",
        "तुम पूछो और मैं ना बताऊँ ऐसे तो हालात नहीं, बस बात ये है कि तुम्हें सोचकर शब्द मिलते नहीं।",
        "हर किसी के नसीब में कहाँ लिखी जाती हैं चाहतें, कुछ लोग दुनिया में आते हैं सिर्फ तन्हाई लेकर।",
        "इश्क़ में क़दम ऐसा रखो कि मंज़िल खुद तुम्हें आवाज़ दे।",
        "खुदा से भी ज्यादा इबादत की है मैंने तुम्हारी, फिर भी कोई जादू नहीं चला मोहब्बत का।",
        "तुम्हारे बिना ये दिल वीरान सा लगता है, जैसे सागर में पानी ना हो।",
        "मुस्कुराने की वजह तुम हो, और रोने की भी।",
        # Add 90 more Shayaris...
        "दिल की गहराइयों से निकली दुआ है, तेरा साथ हमेशा बना रहे।",
        "जो मुस्कुराहट तेरे लबों पर है, वही मेरी दुआओं का असर है।",
        "वो कहती है मोहब्बत से दूर रहो, अब कैसे समझाऊं कि मोहब्बत खुद उससे है।",
        "तेरी एक झलक के लिए ये दिल तरसता है, जैसे चकोर चाँद की दीवानगी में रहता है।",
        "इश्क़ की आग है साहिब, बुझाना मुश्किल है।",
        "तुम्हारी यादें अब तक दिल के दरवाजे पर दस्तक देती हैं।",
        "तुम्हारे बिना ज़िंदगी का सफर अधूरा है, जैसे बिना नाव का नदी में बहाव।",
        "वो जो मुस्कान है तेरी, वही मेरी दुनिया है।",
        "मोहब्बत का सुरूर है या तेरी यादों का नशा, दिल हर घड़ी तुम्हारे ख्यालों में खोया रहता है।",
        "तेरी मोहब्बत में हर एक ग़म मंजूर है।"
    ]
    return random.choice(shayaris)

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
            # Display the message in bold with increased font size
            st.markdown(f"<p class='big-font'>{cracked_message}</p>", unsafe_allow_html=True)
            # Display hearts emojis and balloons
            st.markdown("❤️ ❤️ ❤️ 🎉")
            st.balloons()
        except ValueError:
            st.error("Invalid input! Please ensure the input is a list of numbers separated by commas.")
    else:
        st.error("Please paste your secret message!")

st.divider()

# Random Shayari Generator
st.header("📜 Random Shayari Generator")
if st.button("Generate Random Shayari"):
    shayari = get_random_shayari()
    st.markdown(f"<p class='big-font'>{shayari}</p>", unsafe_allow_html=True)
