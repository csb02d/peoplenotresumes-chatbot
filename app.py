import streamlit as st
import random

def chatbot_response(user_input):
    responses = {
        "hello": "Hey there! Looking for top-tier talent or a new opportunity?",
        "how does fractional recruiting work?": "Fractional recruiting gives you expert hiring support without the cost of a full-time recruiter. We find niche, hard-to-source candidates fast.",
        "who do you recruit for?": "We specialize in helping pre-IPO tech startups, cross-industry innovators, and high-growth companies find impossible-to-source talent.",
        "how long does hiring take?": "We typically deliver top candidates in 2-4 weeks, depending on the role.",
        "what makes you different?": "We don’t rely on job boards. We use deep industry connections, global reach, and AI-driven sourcing to find the right people fast.",
        "how do I get started?": "Easy! Click below to schedule a quick call with us. [Book a Call](#)",
        "i’m a candidate, can you help?": "We focus on helping companies hire, but if you’re an exceptional candidate, reach out! We connect talent with the right opportunities.",
        "thanks": "Anytime! Let me know if you need anything else."
    }
    
    for key in responses.keys():
        if key in user_input.lower():
            return responses[key]
    
    return "Good question! I can help with hiring, fractional recruiting, or candidate connections. What do you need?"

st.title("PeopleNotResumes AI Chatbot")

user_input = st.text_input("Ask me anything about hiring, recruiting, or job searches:")
if user_input:
    response = chatbot_response(user_input)
    st.write(response)
