# valentine_app.py

import streamlit as st
import time

# Page config
st.set_page_config(
    page_title="Valentine Decision Model",
    page_icon="💘",
    layout="centered"
)

# --- CSS: Apple-style + fade-in + floating hearts ---
st.markdown("""
<style>
body {
    background-color: #ffffff;
    font-family: 'Arial', sans-serif;
    overflow-x: hidden;
}
h1, h2, h3 {
    color: #ff7fbf;
}
.stButton>button {
    background-color: #ff7fbf;
    color: white;
    border-radius: 12px;
    height: 3em;
    width: 220px;
    font-size: 18px;
}
.stSlider>div>div>div>div>div>div {
    background: #ffd4e6;
}
.fade-in {
    opacity: 0;
    animation: fadeIn 1.5s forwards;
}
@keyframes fadeIn {
    to { opacity: 1; }
}
.heart {
    position: fixed;
    font-size: 24px;
    animation: floatUp 5s linear infinite;
    pointer-events: none;
}
@keyframes floatUp {
    0% { transform: translateY(100vh) rotate(0deg); opacity: 1; }
    100% { transform: translateY(-10vh) rotate(360deg); opacity: 0; }
}
</style>
<script>
function createHeart() {
    const heart = document.createElement("div");
    heart.className = "heart";
    heart.style.left = Math.random() * window.innerWidth + "px";
    heart.style.animationDuration = 3 + Math.random() * 3 + "s";
    heart.innerHTML = "❤️";
    document.body.appendChild(heart);
    setTimeout(()=>heart.remove(), 6000);
}
setInterval(createHeart, 500);
</script>
""", unsafe_allow_html=True)

# --- Step state ---
if "step" not in st.session_state:
    st.session_state.step = 1

def next_step():
    st.session_state.step += 1

# --- Step 1: Landing ---
if st.session_state.step == 1:
    st.markdown('<h1 class="fade-in">Valentine Decision Model 💘</h1>', unsafe_allow_html=True)
    st.markdown('<h3 class="fade-in">Advanced emotional analytics since Grade 10</h3>', unsafe_allow_html=True)
    st.button("Run Analysis", on_click=next_step)

# --- Step 2: Inputs ---
elif st.session_state.step == 2:
    st.markdown('<h2 class="fade-in">Input Parameters</h2>', unsafe_allow_html=True)
    st.markdown('<h4 class="fade-in">Help train the model by entering your data</h4>', unsafe_allow_html=True)

    miss_texts = st.slider("Number of 'I miss you' texts 📱", 0, 1000, 50)
    facetime = st.slider("FaceTime chemistry level (1-10)", 1, 10, 8)
    adventures = st.slider("Future adventures pending ✈️", 0, 50, 5)
    tolerance = st.slider("Tolerance for my nonsense (1-100)", 0, 100, 90)

    st.button("Train Model", on_click=next_step)

# --- Step 3: Playful Spinner Messages ---
elif st.session_state.step == 3:
    st.markdown('<h2 class="fade-in">Model Running...</h2>', unsafe_allow_html=True)
    spinner_messages = [
        "Removing long-distance bias...",
        "Detecting excessive 'mhmm'...",
        "Filtering playful insults ('dumbass' detected 💗)...",
        "Scanning historical embarrassment archives (Grade 10 data found...)"
    ]
    placeholder = st.empty()
    for msg in spinner_messages:
        placeholder.markdown(f'<p class="fade-in">{msg}</p>', unsafe_allow_html=True)
        time.sleep(1.5)
    st.button("See Mini Results", on_click=next_step)

# --- Step 4: Mini Results ---
elif st.session_state.step == 4:
    st.markdown('<h2 class="fade-in">Mini Results 📊</h2>', unsafe_allow_html=True)
    st.markdown('<ul class="fade-in">'
                '<li><b>Embarrassment Recovery Score:</b> Legendary growth since Grade 10</li>'
                '<li><b>Flirtation Confidence:</b> Slightly improved</li>'
                '<li><b>\'mhmm\' Frequency:</b> Statistically adorable</li>'
                '<li><b>Playful Bullying Index:</b> Healthy & stable</li>'
                '</ul>', unsafe_allow_html=True)
    st.button("Final Result", on_click=next_step)

# --- Step 5: Emotional Turn ---
elif st.session_state.step == 5:
    st.markdown('<h2 class="fade-in">Final Analysis 💗</h2>', unsafe_allow_html=True)
    st.markdown('<p class="fade-in">After reviewing all available data…</p>', unsafe_allow_html=True)
    st.markdown('<p class="fade-in">Including questionable Grade 10 decisions…</p>', unsafe_allow_html=True)
    time.sleep(1.5)
    st.markdown('<h1 class="fade-in">Choosing you. Every time. 💖</h1>', unsafe_allow_html=True)
    st.markdown('<h3 class="fade-in">Final Classification: VALENTINE 💘</h3>', unsafe_allow_html=True)
    st.markdown('<h4 class="fade-in">Confidence: 100%</h4>', unsafe_allow_html=True)
    if st.button("Will you be my Valentine, dumbass?"):
        next_step()

# --- Step 6: Confetti + Confirmation ---
elif st.session_state.step == 6:
    st.balloons()
    st.markdown('<h2 class="fade-in">mhmm. I thought so. 😏</h2>', unsafe_allow_html=True)
    st.markdown('<h3 class="fade-in">Happy early Valentine\'s Day 💕</h3>', unsafe_allow_html=True)
