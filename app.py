import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Page config
st.set_page_config(
    page_title="Fake News Detector",
    page_icon="🔍",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    .stApp {
        background: #f8fafc;
    }
    .hero {
        background: linear-gradient(135deg, #1e3a8a, #2563eb);
        padding: 2rem;
        border-radius: 16px;
        text-align: center;
        color: white;
        margin-bottom: 2rem;
    }
    .hero h1 { font-size: 2rem; font-weight: 700; }
    .hero p  { opacity: 0.85; }
    .result-box {
        background: white;
        border-radius: 14px;
        padding: 1.5rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        border-top: 4px solid #2563eb;
        font-size: 0.95rem;
        line-height: 1.8;
        color: #1f2937;
        white-space: pre-wrap;
    }
    .stButton > button {
        background: linear-gradient(135deg, #2563eb, #1d4ed8) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 0.6rem 1.8rem !important;
        font-weight: 600 !important;
        width: 100%;
        font-size: 1rem !important;
    }
    .stButton > button:hover {
        transform: translateY(-1px) !important;
        box-shadow: 0 4px 14px rgba(37,99,235,0.4) !important;
    }
    #MainMenu, footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# Hero
st.markdown("""
<div class="hero">
    <h1>🔍 Fake News Detector</h1>
    <p>Paste any news article and AI will check if it's real or fake!</p>
</div>
""", unsafe_allow_html=True)

# Input
article = st.text_area(
    "Paste your news article here",
    height=200,
    placeholder="Copy and paste any news article or headline here..."
)

# Button
if st.button("🔍 Analyze News"):
    if not article.strip():
        st.warning("Please paste a news article first!")
    else:
        with st.spinner("🤖 AI is analyzing the article..."):
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "user",
                        "content": f"""You are a fake news detection expert. Analyze the following news article and determine if it is REAL or FAKE.

Article:
{article}

Give your response in this exact format:

VERDICT: REAL or FAKE

CREDIBILITY SCORE: X/10

REASONS:
- Reason 1
- Reason 2
- Reason 3

SUMMARY:
A short 2-3 sentence summary of the article.

ADVICE:
One line advice for the reader."""
                    }
                ]
            )
            result = response.choices[0].message.content

        st.markdown("### 📊 Analysis Result")
        st.markdown(f'<div class="result-box">{result}</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:#9ca3af; font-size:0.8rem;'>Built with ❤️ using Streamlit + Groq AI</p>",
    unsafe_allow_html=True
)