import streamlit as st
from PIL import Image
from member_data import member_info

member_name = st.session_state.get("selected_member", None)
if not member_name:
    st.warning("⚠️ トップページで推しを選んでください。")
    st.stop()

data = member_info[member_name]
bg_color = data["color"]

st.set_page_config(page_title=member_name, layout="centered")

st.markdown(f"""
    <style>
    @keyframes glow {{
      0% {{
        text-shadow: 0 0 5px #fff, 0 0 10px #ff66cc, 0 0 20px #ff99cc,
                     0 0 30px #ff66cc, 0 0 40px #ff99cc;
        transform: scale(1);
      }}
      50% {{
        text-shadow: 0 0 10px #fff, 0 0 20px #ff66cc, 0 0 30px #ff99cc,
                     0 0 40px #ff66cc, 0 0 60px #ff99cc;
        transform: scale(1.05);
      }}
      100% {{
        text-shadow: 0 0 5px #fff, 0 0 10px #ff66cc, 0 0 20px #ff99cc,
                     0 0 30px #ff66cc, 0 0 40px #ff99cc;
        transform: scale(1);
      }}
    }}

    .stApp {{
        background: radial-gradient(circle at top, #ffe6f2, {bg_color});
        font-family: 'Comic Sans MS', cursive;
        color: #800080;
        padding: 2rem;
    }}

    .center {{
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
    }}

    .member-name {{
        font-size: 3.8rem;
    font-weight: bold;
    background: -webkit-linear-gradient(45deg, #ff99cc, #ff66cc);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    -webkit-text-stroke: 1.2px white; /* 🔥 輪郭追加でくっきり */
    text-shadow:
        0 0 8px #ff66cc,
        0 0 12px #ff99cc;
    animation: glow 2.5s ease-in-out infinite;
    padding: 1rem;
    border-radius: 20px;
    margin-bottom: 2rem;
    }}

    .center img {{
        border-radius: 50%;
        box-shadow: 0 0 25px #ff99cc;
        border: 4px dotted #ff66cc;
        margin-bottom: 1.5rem;
    }}

    .link-button {{
        display: inline-block;
        background: linear-gradient(45deg, #ffb6c1, #ff69b4);
        color: white;
        font-weight: bold;
        padding: 0.6rem 1.2rem;
        margin: 0.5rem;
        border-radius: 30px;
        text-decoration: none;
        font-size: 1.2rem;
        box-shadow: 0 0 15px rgba(255, 105, 180, 0.7);
        transition: transform 0.2s ease;
    }}

    .link-button:hover {{
        transform: scale(1.1);
        background: white;
        color: #ff69b4;
        border: 2px solid #ff69b4;
    }}

    p {{
        font-size: 1.8rem;
        color: #800080;
        background-color: #fff0f5;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(255,192,203,0.3);
        max-width: 600px;
        margin-bottom: 1.5rem;
    }}
    </style>
""", unsafe_allow_html=True)

# メンバー名（キラキラ）
st.markdown(f"""
    <div class='center'>
        <h1 class='member-name'>{member_name}</h1>
    </div>
""", unsafe_allow_html=True)

# 紹介文
st.markdown(f"""
    <div class='center'>
        <p>💗{data['description']}💗</p>
    </div>
""", unsafe_allow_html=True)

# 写真
st.image(data["image"], width=300, use_container_width=True)

# SNS
st.markdown(f"""
    <div class='center'>
        <a href='{data['SNS']}' target='_blank' class='link-button'>📷 SNSへ</a>
    </div>
""", unsafe_allow_html=True)

# TikTok
if data.get("tiktok"):
    st.markdown(f"""
        <div class='center'>
            <a href='{data['tiktok']}' target='_blank' class='link-button'>🎵 TikTok</a>
        </div>
    """, unsafe_allow_html=True)

# YouTube
if data.get("youtube"):
    st.markdown(f"""
        <div class='center'>
            <a href='{data['youtube']}' target='_blank' class='link-button'>▶️ YouTubeを見る</a>
        </div>
    """, unsafe_allow_html=True)
