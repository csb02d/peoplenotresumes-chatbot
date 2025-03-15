import streamlit as st
import random

# Hide Streamlit branding
st.markdown("""
    <style>
        /* Hide Streamlit header and footer */
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .viewerBadge_container__1QSob {display: none !important;} /* Removes "Manage app" */
        
        /* Customize the chatbot container */
        .stApp {
            background-color: white; /* Optional: Change background */
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
        }
    </style>
""", unsafe_allow_html=True)

# Chatbot UI
st.title("🤖 How Can We Help")
st.write("Ask me anything about hiring, recruiting, or job searches:")

user_input = st.text_input("")

def chatbot_response(user_input):
    responses = {
        "hello": "Hey there! Looking for top-tier talent or a new opportunity?",
        "how does fractional recruiting work?": "Fractional recruiting gives you expert hiring support without the cost of a full-time recruiter.",
        "who do you recruit for?": "We specialize in pre-IPO tech startups, cross-industry innovators, and high-growth companies.",
        "how long does hiring take?": "We typically deliver top candidates in 2–4 weeks, depending on the role.",
        "what makes you different?": "We don’t rely on job boards. We use deep industry connections, global reach, and AI-driven matching.",
        "how do I get started?": "Easy! Click below to schedule a quick call with us. [Book a Call](#)",
        "i’m a candidate, can you help?": "We focus on helping companies hire, but if you’re an exceptional candidate, reach out!",
        "thanks": "Anytime! Let me know if you need anything else.",
        "how much do you cost?": "We offer flexible pricing based on your hiring needs. Book a quick call to discuss pricing.",
        "what are your fees?": "We tailor our fees based on the role and hiring model (fractional, hourly, or full placement)."
    }

    for key in responses.keys():
        if key in user_input.lower():
            return responses[key]
    return "Good question! I can help with hiring, fractional recruiting, or candidate connections."

if user_input:
    response = chatbot_response(user_input)
    st.write(response)
