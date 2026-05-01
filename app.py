import streamlit as st
import base64
import time
import random

st.set_page_config(page_title="A Special Surprise 🎬", page_icon="🎂", layout="wide")

# ----------- IMAGE BASE64 -----------
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

img_base64 = get_base64_image("friend.jpg")

# ----------- 🎵 MUSIC (FINAL FIX - HTML AUTOPLAY) -----------
def play_music():
    with open("birthday.mp3", "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()

    audio_html = f"""
    <audio autoplay loop>
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
    </audio>
    """

    st.markdown(audio_html, unsafe_allow_html=True)

# ----------- CSS -----------
st.markdown("""
<style>
body {
    background: radial-gradient(circle at center, #020617, #000000);
}

.main-title {
    text-align: center;
    font-size: 70px;
    color: #facc15;
    text-shadow: 0 0 30px #facc15;
    margin-top: 40px;
}

.sub-text {
    text-align: center;
    font-size: 24px;
    color: #cbd5f5;
}

div.stButton {
    display: flex;
    justify-content: center;
}

.stButton>button {
    width: 320px;
    height: 65px;
    font-size: 20px;
    border-radius: 20px;
    margin: 12px;
    border: none;
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.08);
}

.glow-box {
    margin: auto;
    width: 65%;
    padding: 35px;
    border-radius: 25px;
    text-align: center;
    color: white;
    font-size: 26px;
    background: rgba(15, 23, 42, 0.9);
    box-shadow: 0 0 40px rgba(255,255,255,0.2);
}

.corner-img {
    position: fixed;
    width: 110px;
    border-radius: 50%;
    border: 3px solid #facc15;
    box-shadow: 0 0 25px #facc15;
    animation: pulse 2s infinite alternate;
    z-index: 999;
}

@keyframes pulse {
    from { box-shadow: 0 0 15px #facc15; }
    to { box-shadow: 0 0 40px #facc15; }
}

.top-left { top: 20px; left: 20px; }
.top-right { top: 20px; right: 20px; }
.bottom-left { bottom: 20px; left: 20px; }
.bottom-right { bottom: 20px; right: 20px; }

@keyframes float {
    0% {transform: translateY(100vh);}
    100% {transform: translateY(-10vh);}
}

.particle {
    position: fixed;
    bottom: -100px;
    font-size: 24px;
    animation: float 12s linear infinite;
    opacity: 0.5;
}
</style>
""", unsafe_allow_html=True)

# ----------- INTRO SCREEN -----------
if "start" not in st.session_state:
    st.session_state.start = False

if not st.session_state.start:
    st.markdown("""
    <div style="
        display:flex;
        flex-direction:column;
        justify-content:center;
        align-items:center;
        height:80vh;
        color:white;
        font-size:40px;
        text-align:center;
    ">
        🎬 A Special Surprise Awaits...<br><br>
        Click below to begin
    </div>
    """, unsafe_allow_html=True)

    if st.button("✨ Enter Experience"):
        st.session_state.start = True
        st.rerun()

    st.stop()

# ----------- CORNER IMAGES -----------
st.markdown(f"""
<img src="data:image/jpg;base64,{img_base64}" class="corner-img top-left">
<img src="data:image/jpg;base64,{img_base64}" class="corner-img top-right">
<img src="data:image/jpg;base64,{img_base64}" class="corner-img bottom-left">
<img src="data:image/jpg;base64,{img_base64}" class="corner-img bottom-right">
""", unsafe_allow_html=True)

# ----------- FLOATING PARTICLES -----------
particles = ""
for i in range(12):
    left = random.randint(0, 100)
    delay = random.uniform(0, 6)
    particles += f'<div class="particle" style="left:{left}%; animation-delay:{delay}s;">✨</div>'

st.markdown(particles, unsafe_allow_html=True)

# ----------- BALLOONS -----------
if "shown" not in st.session_state:
    st.balloons()
    st.session_state.shown = True

# ----------- TITLE -----------
st.markdown('<div class="main-title">🎉 Happy Birthday Sreehasa 🎂</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">This is your moment ✨</div>', unsafe_allow_html=True)

# ----------- TYPING EFFECT -----------
def typing_effect(text):
    placeholder = st.empty()
    output = ""
    for char in text:
        output += char
        placeholder.markdown(f"<div class='glow-box'>{output}</div>", unsafe_allow_html=True)
        time.sleep(0.02)

# ----------- SESSION STATE FOR MUSIC -----------
if "play_music" not in st.session_state:
    st.session_state.play_music = False

# ----------- BUTTONS -----------

if st.button("🎁 Open Gift"):
    st.balloons()
    st.markdown('<div class="glow-box">🎉 Surprise unlocked! 🎉</div>', unsafe_allow_html=True)

if st.button("💬 Read Message"):
    typing_effect("""
Dear Sreehasa,

Wishing you a day filled with love, laughter, and happiness.
May this year bring lot of happiness and success in your life.

May all the health challenges you are facing fade away,
and may strength, peace, and healing find you soon.

If I could ask the universe for one thing today, it would be to take away every bit of pain you’ve been carrying and replace it with strength, peace, and healing. I truly wish that all the health struggles you’re facing become nothing but a distant memory very soon.
You deserve a beautiful life ahead 
""")

if st.button("📸 Reveal Memory"):
    st.image("friend.jpg", use_column_width=True)

# ----------- 🎵 MUSIC BUTTON -----------
if st.button("🎵 Play Music"):
    st.session_state.play_music = True

if st.session_state.play_music:
    play_music()

if st.button("🎉 Celebrate"):
    st.balloons()

if st.button("⭐ Final Surprise"):
    st.balloons()
    st.markdown("""
    <div class="glow-box">
    🌟 You deserve the best in life 🌟
    </div>
    """, unsafe_allow_html=True)