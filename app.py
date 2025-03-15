import streamlit as st

# Set the page width and remove unnecessary Streamlit UI elements
st.set_page_config(page_title="Chatbot", page_icon="💬", layout="centered")

# Hide Streamlit footer and menu to make it look cleaner
hide_streamlit_style = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        .stTextInput>div>div>input {width: 100% !important;} /* Make input field fit */
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Chatbot Title
st.title("💬 PeopleNotResumes AI Chatbot")

# Chat Input
user_input = st.text_input("Ask me anything about hiring, recruiting, or job searches:")

# Chatbot Responses
def chatbot_response(user_input):
    responses = {
        "hello": "Hey there! Looking for top-tier talent or a new opportunity?",
        "how does fractional recruiting work?": "Fractional recruiting gives you expert hiring support without the cost of a full-time recruiter.",
        "who do you recruit for?": "We specialize in helping pre-IPO tech startups, cross-industry innovators, and high-growth companies.",
        "how long does hiring take?": "We typically deliver top candidates in 2–4 weeks, depending on the role.",
        "what makes you different?": "We don’t rely on job boards. We use deep industry connections, global reach, and AI-driven insights.",
        "how do I get started?": "Easy! Click below to schedule a quick call with us. [Book a Call](#)",
        "i’m a candidate, can you help?": "We focus on helping companies hire, but if you’re an exceptional candidate, reach out!",
        "thanks": "Anytime! Let me know if you need anything else.",
        "how much do you cost?": "We offer flexible pricing based on your hiring needs. Book a quick call to discuss pricing options.",
        "what are your fees?": "We tailor our fees based on the role and hiring model (fractional, hourly, or full placement)."
    }
    
    for key in responses.keys():
        if key in user_input.lower():
            return responses[key]
    
    return "Good question! I can help with hiring, fractional recruiting, or candidate connections. What do you need?"

# Display Response
if user_input:
    response = chatbot_response(user_input)
    st.write(response)

