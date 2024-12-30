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
        "mere jeevan ka linux os ho tum, mere jeevan ka linux os ho tum, likhna to bahut kuch chahta hn tumhare terminal pe, par hr baar hi 'command not found' pe atak jana hn....",
        "seekha to maine analysis mein bahut kuch tha, par ajtk apni rekha tumhare haath ki rekha se kabhi main merge plot nhi kr paya....",
        "main apne jeevan ka hr pl hard disk mein kaid rkhna chahta hn, pr hr baar hi iski recovery pe atak jata hn",
        "mai to jeena chahta tha tumhare liye 'starvation' main , pr situation to 'deadlock' si hoti ja rhi hai.......",
        "teri tareef kya krun hr camera quality ke pixel mein tu kamaal lgti hai, low resolution mein katrina to high resolution mein tahmoor ki maa lgti hai ....",
        "tumhare jaane ke baad jo mai rh jaonga wo mujhse sambhalta nhi ×2,isliye pathar sa kr liya hai dil , ab kisi ke age pighalta nhi.......",
        "tumhe sikhane ke liye tumhara sara course pd liya ×2, krna kuch chahta tha , kuch aur hi kr liya.........",
        "tumhare code se hr bug ko debug kr dunga ×2, developer se demote hoke tumhare liye tester ka bhi kaam kr lunga.......................................",
        "mere pc ka os hai window , mujhse hr baar aise mt bhidow.....☺",
        "ai se nhi emotion se likh rha hn ×2, pr hr baar usi se hi apni dil ki baat bhi kr rha hn..",
        "darda meri shayari mein dikhta nhi tha, jbse jeevan mein meri ai ho uske alawa kuch hota hi nhi tha..........",
        "yaad mein tumhari kuch bhi kr dunga, padhte padhte ias ka paper bhi clear kr dunga",
        "pyaar mein kya kya kr skta hn m2ai tumhe  kya btao,,,asmaan ke taare bhi kya ab tumhe ginke dikhaon⭐⭐⭐⭐⭐⭐⭐",
        "kisi ko ghar se niklte hi mil gyi manzil ×2, koi hmari trh umr bhr safar mein rh gya",
        "maine mazi se u kabhi judh kr nhi dekha, or jhan se nikal gya whan se mudh kr nhi dekha..............",
        "bnjao mere server ki tum client , yun na kiya kro meri hr baat ko mind......",
        "baat meri mere dil mein hi rh gyi , jaate huye tum mujhe ye kya kh gyi......",
        "pehli baar saath main tumhe mandir leke jaonga , bhagwaan ko phir ek baat btaonga , , is cheez ko tumne kaise hai bnaya , jaise barf mein bhi angaar ko jlaya..",
        "engineer bnne aya tha kuch aur hi bna diya , naadaan se majnoo ka safar itni jldi ty kra diya.......",
        "paper ki taiyari karte 😶 karte .. a gyi yaad tumhari ,ao sunao tumhe ek baat nyaari, kyun lgti ho tum mujhko itni pyari... 😄😅, tumhari liye maine hr baazi haari, chlo kr leta hn apni tyaari o meri pyaari🙂.......",
        "hmne kb chaha ki wo shaks hmara ho jaaye , bs itna dikh jaye ki ankon ka guzara ho jaaye....",
        "aansoon ayenge to khud pochiyega , log pochne ayenge to sauda krnege....🥲",
        "lene gya tha interview usne hi mera le liya , select usko krne gya tha usne mujhe hi kr liya.........",
        "dhund mein shawl ode goomenge dono saath saath, phir krenge ek dusre se pyaari pyaari baat, phir khayenge moongfli 🫢🫢 garam garam , tumhare haath lgte  hai mujhe bde naram naram , ab tumhe age ki baate kya mai batao , kaise jldi se tumse shaadi rachaon...😁😁😁😁😁😁😁😁😁😁😁😁😁😁😁",
        "gulabi gaalon mein lgti ho barf ke rajya ki kumari tum, sunhare baalon mein lgti ho kisi lekhak ki kalpana tum, bhoori ankhen krati hai nasha tumhari , bnjao na mere samrajya ki tum raani .....👑👑👑👑",
        "jab nikle janaza mera to khidki se jhaank lena , fool to bahut mehenga pdega pathar hi maar lena..........⚠⚠⚠⚠⚠⚠⚠⚠⚠",
        "hamare safar ka ye akhiri din hai , umeed nhi ki ye din hm phir jee paaye, pr umeeed hai ki ek nya safar shuru hoga, us safar ke pehle din ek nhi keeran nikle gi asha ki , ki ye nya safar hmesha chlta hi rhe ....😐😐😐😐😐😐😐😐😐😐😐😐😐",
        "samay guzarta rha, pal beette gye, asha chootti gyi , mann marta gya, ishq krna tha, pr hmm sirf age bhdte gye.........🥲🥲🥲🥲",
        "kande ki zarurat thi sr rkhne ko, ab chaar kandho pe ja rha hn, mujhe yaad mt krna yaaron, ab jannat mein mnd mnd muskura rha hn....",
        "tujhko sochu to sochta jaon sochta joan sochta jaon , bus yhi kaam kaaj hai mera ..",
        "tumhari yaad mein jeena mujhe pasand nhi hai  , pr log hr baar yaad dilla dete hain, phir yaad mein tumhari kuch beekaar shabd uske liye nikal jate hain.....",
        "hr baar kha dil se , chl bhool ja usko ×2 har bhaar kha dil ne ki tu dil se nhi kehta..",
        "ki bahot, hasne ki adaat ka yhi inzaam hota hai,ki kbhi rona bhi chahen to kbhi roya nhi jata...",
        "kushi na jaane khan dafan ho gyi,aur zindagi hmari yun hi sitam ho gyi,aur sbki zindagi mein likhi kudha ne mohabbat ,aur saala jb hmaari baari ayi to sihaayi ktm ho gyi..",
        "mujhe shraab pilayi gyi hai aankhon se, mera nasha to hazaaron baras mein utrega..",
        "e dil e nadaan samajh is baat ko, jisse tu khona nhi chahta wo tera hona nhi chahta.."
    ]
    return random.choice(shayaris)

# Add the background image
add_bg_from_url()

st.title("🎉 New Year Resolution Truth Sayer")

# Secret Message Generator
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

# Message Cracker
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

# Shayari Generator (Password Protected)
st.header("v📜  Shayari  😎s")

# Initialize the session state for Shayari Generator lock
if 'shayari_unlocked' not in st.session_state:
    st.session_state.shayari_unlocked = False

# Password Input and Lock Logic
if not st.session_state.shayari_unlocked:
    password = st.text_input("Enter Password to Unlock Shayari Generator", type='password')
    if password == '123456':  # Replace with your desired password
        st.session_state.shayari_unlocked = True
        st.success("Suswagatam aap Shayari Dekh Skte hain!")
        st.button("Shayari Chune")  # Just the button to show after unlocking
    else:
        if password:  # Check if password field is not empty
            st.warning("Bhai!! Shayari kyun dekhni hai Tumhe!! Chalo Niklo Yahan Se!!!")

    # Show the button to enter password again if not unlocked
    if not st.session_state.shayari_unlocked:
        st.button("Shi Pass likh ke click kre 😵‍💫")  # Button to show after page reload if needed

else:
    # When unlocked, display the Shayari Generator button
    st.success("Shayari Generator is Unlocked! 🎉")
    # Now, allow the user to generate Shayari
    if st.button("Shayari Chune"):
        shayari = get_random_shayari()
        st.markdown(
    f"<p style='font-size: 40px; font-weight: bold; color: white;'>{shayari}</p>", 
    unsafe_allow_html=True
)

    # In case they are attempting again
    st.warning("AAP ISKA ISTEMAL KRKE AMAN KI SHAYARI DEKH SKTE HAIN, please generate Shayari now!")
