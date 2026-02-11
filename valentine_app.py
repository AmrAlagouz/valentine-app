# romantic_valentine_app.py

import streamlit as st
import time

# Page config
st.set_page_config(
    page_title="Valentine Surprise 💖",
    page_icon="💘",
    layout="centered"
)

# --- CSS: Soft pink background, fade-in, floating hearts ---
st.markdown("""
<style>
body {
    background-color: #ffe6f0;  /* Soft pastel pink */
    font-family: 'Arial', sans-serif;
    overflow-x: hidden;
    color: #4d004d;  /* Dark purple text for readability */
}
h1, h2, h3 {
    color: #ff3385;  /* Darker pink headings */
}
.stButton>button {
    background-color: #ff7fbf;  /* Pink buttons */
    color: white;
    border-radius: 12px;
    height: 3em;
    width: 240px;
    font-size: 18px;
}
.stSlider>div>div>div>div>div>div {
    background: #ffd4e6;  /* Soft slider color */
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
    st.markdown('<h1 class="fade-in">A Little Surprise 💖</h1>', unsafe_allow_html=True)
    st.markdown('<h3 class="fade-in">Just for you my love…</h3>', unsafe_allow_html=True)
    st.button("Start the magic baby ✨", on_click=next_step)

# --- Step 2: Romantic Inputs ---
elif st.session_state.step == 2:
    st.markdown('<h2 class="fade-in">Help me complete the love survey 💕</h2>', unsafe_allow_html=True)
    
    st.markdown('<div style="text-align:center; font-size:50px;">🥰</div>', unsafe_allow_html=True)
    miss = st.slider("How much do you miss me today?", 0, 10, 5)
    
    st.markdown('<div style="text-align:center; font-size:50px;">❤️</div>', unsafe_allow_html=True)
    facetime = st.slider("Rate our love for each other", 0, 10, 8)
    
    st.markdown('<div style="text-align:center; font-size:50px;">✈️</div>', unsafe_allow_html=True)
    trips = st.slider("Number of future adventures we’ll go on", 0, 20, 3)
    
    st.markdown('<div style="text-align:center; font-size:50px;">😏</div>', unsafe_allow_html=True)
    tolerance = st.slider("How much do I turn you on?", 0, 100, 90)
    
    st.button("Train the love engine 💖", on_click=next_step)

# --- Step 3: Playful Spinner Messages ---
elif st.session_state.step == 3:
    st.markdown('<h2 class="fade-in">Running the Love Engine...</h2>', unsafe_allow_html=True)
    spinner_msgs = [
        "Counting all the times you made me smile…",
        "Measuring your perfect mhmm 😍",
        "Checking playful insults (‘dumbass’ detected 💕)…",
        "Recalling my most embarrassing Grade 10 moment… for you"
    ]
    placeholder = st.empty()
    for msg in spinner_msgs:
        placeholder.markdown(f'<p class="fade-in">{msg}</p>', unsafe_allow_html=True)
        time.sleep(1.5)
    st.button("See Mini Results 💖", on_click=next_step)

# --- Step 4: Mini Cute Stats ---
elif st.session_state.step == 4:
    st.markdown('<h2 class="fade-in">Mini Love Stats 📊</h2>', unsafe_allow_html=True)
    st.markdown('<ul class="fade-in">'
                '<li><b>Your Smile Score:</b> 100% adorable</li>'
                '<li><b>My Heart Rate:</b> Accelerated every time I see you</li>'
                '<li><b>\'mhmm\' Detection:</b> Perfectly cute</li>'
                '<li><b>Turned on level:</b> Maximum</li>'
                '</ul>', unsafe_allow_html=True)
    st.button("See Final Result 💖", on_click=next_step)

# --- Step 5: Emotional Turn ---
elif st.session_state.step == 5:
    st.markdown('<h2 class="fade-in">Final Analysis 💗</h2>', unsafe_allow_html=True)
    st.markdown('<p class="fade-in">After counting all the laughs, silly moments, and mhmm’s…</p>', unsafe_allow_html=True)
    st.markdown('<p class="fade-in">I only ever choose you 💖</p>', unsafe_allow_html=True)
    
    time.sleep(1.5)
    st.markdown('<h1 class="fade-in">💘 Will you be my Valentine?</h1>', unsafe_allow_html=True)
    if st.button("Yes, of course! 😏💕"):
        next_step()

# --- Step 6: Confetti + Hearts ---
elif st.session_state.step == 6:
    st.balloons()
    st.markdown('<h2 class="fade-in">mhmm. I knew you’d say yes 😏💕</h2>', unsafe_allow_html=True)
    st.markdown('<h3 class="fade-in">Happy early Valentine\'s Day my love 💖</h3>', unsafe_allow_html=True)
