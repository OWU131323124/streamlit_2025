import streamlit as st
import base64
from member_data import member_info

st.set_page_config(page_title="推し選択", layout="centered")

def get_base64_image(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

img_base64 = get_base64_image("img/ilife.jpg")

st.markdown(f"""
<style>
.stApp {{
  background-image: url("data:image/jpg;base64,{img_base64}");
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
  background-repeat: no-repeat;
  color: #333333;
}}

@keyframes sparkle {{
  0%, 100% {{opacity: 1; transform: scale(1);}}
  50% {{opacity: 0.7; transform: scale(1.05);}}
}}

@keyframes pulsate {{
  0% {{ transform: scale(1); box-shadow: 0 0 15px 5px rgba(255, 182, 193, 0.5); }}
  50% {{ transform: scale(1.05); box-shadow: 0 0 25px 10px rgba(255, 105, 180, 0.8); }}
  100% {{ transform: scale(1); box-shadow: 0 0 15px 5px rgba(255, 182, 193, 0.5); }}
}}

h1 {{
  font-family: 'Comic Sans MS', cursive, sans-serif;
  font-size: 3rem;
  color: #ff1493;
  text-shadow:
    0 0 5px #ff69b4,
    0 0 10px #ff1493,
    0 0 20px #ff69b4,
    0 0 40px #ff1493;
  animation: sparkle 2.5s infinite ease-in-out;
  text-align: center;
  margin-bottom: 2rem;
}}

.stForm {{
  background: rgba(255, 240, 245, 0.9);
  padding: 40px;
  border-radius: 25px;
  box-shadow: 0 0 30px 10px rgba(255, 192, 203, 0.5);
  max-width: 600px;
  margin: 0 auto 3rem;
  transition: box-shadow 0.3s ease;
}}
.stForm:hover {{
  box-shadow: 0 0 40px 15px #ffb6c1;
}}

.stButton>button {{
  background: linear-gradient(45deg, #ffc0cb, #ffb6c1);
  color: white;
  font-weight: bold;
  border-radius: 30px;
  padding: 0.6rem 2rem;
  font-size: 1.2rem;
  box-shadow: 0 0 15px 3px #ffb6c1;
  transition: box-shadow 0.3s ease, transform 0.3s ease;
  cursor: pointer;
}}
.stButton>button:hover {{
  box-shadow: 0 0 25px 7px #ffc0cb;
  transform: scale(1.05);
}}

div[role="combobox"]:hover {{
  box-shadow: 0 0 10px 3px #ffc0cb;
  border-radius: 10px;
  transition: box-shadow 0.3s ease;
}}

.ticket-button {{
  display: inline-block;
  background: linear-gradient(135deg, #ffb6c1, #ffc0cb, #ffe4e1);
  color: white;
  font-weight: bolder;
  font-size: 1.5rem;
  padding: 1.2rem 2.4rem;
  border-radius: 50px;
  text-decoration: none;
  text-align: center;
  box-shadow: 0 0 20px 6px rgba(255, 192, 203, 0.6);
  animation: pulsate 2s infinite ease-in-out;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  background-clip: padding-box;
  border: 2px solid white;
}}
.ticket-button:hover {{
  transform: scale(1.08);
  box-shadow: 0 0 35px 12px rgba(255, 182, 193, 0.8);
}}
</style>
""", unsafe_allow_html=True)

st.title("iLiFE!")
st.markdown(
    """
    <style>
    .sparkle-subtitle {
        font-family: 'Comic Sans MS', cursive, sans-serif;
        color: #ffffff;
        font-size: 20px;
        text-align: center;
        margin-top: -10px;
        text-shadow:
            0 0 5px #ff69b4,
            0 0 10px #ff1493,
            0 0 20px #ff69b4;
        animation: sparkle 2.5s infinite ease-in-out;
    }
    </style>
    <p class="sparkle-subtitle">～私(i)と貴女(!)で作る、アイドルライフ～</p>
    """,
    unsafe_allow_html=True
)

members = list(member_info.keys())

with st.form("select_form"):
    selected_member = st.selectbox("　💗MEMBERS💗　", members)
    submitted = st.form_submit_button("👉 ONE PICK!")

if submitted:
    st.session_state["selected_member"] = selected_member
    st.switch_page("pages/profile.py")

st.markdown("""
<div style='text-align:center; margin-top: 2rem;'>
    <p style='color:#0; font-size: 1.3rem; font-weight:bold;'>iLiFE!会いにKiTE！</p>
    <a class='ticket-button' href='https://t.co/4UXebbMoEq' target='_blank'>🎫 チケット購入はこちら！</a>
</div>
""", unsafe_allow_html=True)
