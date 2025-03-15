import streamlit as st
import difflib

# Define chatbot responses
def chatbot_response(user_input):
    responses = {
        "hello": "Hey there! Looking for top-tier talent or a new opportunity?",
        "how does fractional recruiting work?": "Fractional recruiting gives you expert hiring support...",
        "who do you recruit for?": "We specialize in helping pre-IPO tech startups...",
        "how long does hiring take?": "We typically deliver top candidates in 2–4 weeks...",
        "what makes you different?": "We don’t rely on job boards. We use deep industry connections...",
        "how do I get started?": "Easy! Click below to schedule a call. [Book a Call](#)",
        "i'm a candidate, can you help?": "We focus on helping companies hire...",
        "thanks": "Anytime! Let me know if you need anything else.",
        "how much do you cost?": "We offer flexible pricing based on hiring needs...",
        "what are your fees?": "We tailor our fees based on the role and hiring model..."
    }

    # Use fuzzy matching to find the closest question
    closest_match = difflib.get_close_matches(user_input.lower(), responses.keys(), n=1, cutoff=0.6)
    
    if closest_match:
        return responses[closest_match[0]]
    return "I'm not sure about that. Try rephrasing your question!"

# Streamlit App UI
st.title("PeopleNotResumes AI Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# User input
user_input = st.text_input("Ask me anything about hiring, recruiting, or job searches:")

if user_input:
    response = chatbot_response(user_input)
    st.session_state["messages"].append(f"**You:** {user_input}")
    st.session_state["messages"].append(f"**Bot:** {response}")

# Display chat history
for msg in st.session_state["messages"]:
    st.write(msg)

