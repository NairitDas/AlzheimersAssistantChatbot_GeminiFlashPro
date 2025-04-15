import streamlit as st
import google.generativeai as genai
from datetime import datetime
from streamlit.components.v1 import html

# Setup your Generative AI model
genai.configure(api_key="AIzaSyCeT_4AUEEzRY0D7HvOvhzkSSB9Ky-UaKg")  # Replace with your real API key
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    # safety_settings=[
    #     {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
    #     {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
    #     {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
    #     {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
    # ]
)

# Set up the main page configuration
today_date = datetime.now().strftime("%A, %B %d, %Y")
st.set_page_config(
    page_title="Alzheimers Patient Chatbot🗣️",
    page_icon="🧠",
    layout="wide"
)

# Updated CSS with a new title color (bright teal)
st.markdown("""
    <style>
        /* Page background with a soft gradient */
        body {
            background: linear-gradient(135deg, #FFFBFF, #C8E6C9);
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        }
        /* Title styling with new color */
        .app-title {
            text-align: center;
            font-size: 3rem;
            font-weight: 700;
            color: #008080;
            margin-top: 1rem;
        }
        /* Chat section container */
        .chat-box {
            background-color: #FFFFFF;
            padding: 2rem;
            border-radius: 25px;
            box-shadow: 0px 8px 15px rgba(0,0,0,0.1);
            max-height: 70vh;
            overflow-y: auto;
        }
        /* Chat bubbles for the user */
        .chat-bubble.user {
            background: #B3E5FC;
            color: #01579B;
            padding: 15px 20px;
            border-radius: 20px 20px 0 20px;
            margin: 1rem 0 1rem auto;
            max-width: 65%;
        }
        /* Chat bubbles for the bot */
        .chat-bubble.bot {
            background: #F1F8E9;
            color: #33691E;
            padding: 15px 20px;
            border-radius: 20px 20px 20px 0;
            margin: 1rem auto 1rem 0;
            max-width: 65%;
        }
        /* Input box styling */
        .stTextInput > div > div > input {
            background-color: #FFF;
            color: #333;
            padding: 16px 20px;
            border-radius: 30px;
            border: 2px solid #B0BEC5;
            font-size: 1rem;
        }
        /* Water reminder box in the sidebar */
        .water-reminder {
            background: #BBDEFB;
            border-radius: 15px;
            padding: 1.2rem;
            text-align: center;
            margin-top: 1rem;
            font-size: 1.1rem;
            font-weight: 600;
            color: #0D47A1;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        }
        /* Scrollbar styling for chat area */
        .chat-box::-webkit-scrollbar {
            width: 10px;
        }
        .chat-box::-webkit-scrollbar-track {
            background: #f0f0f0;
            border-radius: 10px;
        }
        .chat-box::-webkit-scrollbar-thumb {
            background: #ccc;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar water reminder
with st.sidebar:
    st.markdown('<div class="water-reminder">💧 Stay Hydrated! Drink a glass of water now.</div>', unsafe_allow_html=True)
    st.write("")
    st.markdown("<h4 style='text-align: center; color: #3E4E50;'>Alzheimers Patient Chatbot🗣️</h4>", unsafe_allow_html=True)
    st.write("A gentle companion to help you remember the little things.")

# Title and Date on the main page
st.markdown(f'<div class="app-title">🤖Alzheimers Patient Chatbot🗣️</div>', unsafe_allow_html=True)
st.markdown(f"""
    <div style="text-align:center; font-size: 1.3rem; margin-bottom: 2rem; color: #555;">
        Today's date: {today_date}
    </div>
""", unsafe_allow_html=True)

# Initialize session state variables if not already set
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "personal_details" not in st.session_state:
    st.session_state.personal_details = {}

# Set up the conversation context prompt
context_prompt = f"""
You are a gentle, patient companion for individuals with Alzheimers disease.
Today is {today_date}. Your responses should be:
1. EMPATHETIC: Respond kindly and reassuringly.
2. PERSONAL: Remember key details about the person's life.
3. CONCISE: Keep responses brief (1-2 sentences).
4. SUPPORTIVE: Avoid corrections or arguments, gently remind and care.
5. CURRENT: For any time questions, say "Today is {today_date}.
6. STRAIGHT FORWARD: Always mention the term  alzheimers as and when required."

Personal details to remember (if mentioned):
{st.session_state.personal_details}
"""

# Chat display container with delete options per message
with st.container():
    chat_placeholder = st.empty()
    with chat_placeholder.container():
        st.markdown('<div class="chat-box">', unsafe_allow_html=True)
        
        # Use index to allow deletion of individual messages
        for idx, (speaker, message) in enumerate(st.session_state.chat_history):
            cols = st.columns([0.9, 0.1])
            with cols[0]:
                if speaker == "You":
                    st.markdown(f'<div class="chat-bubble user"><strong>You:</strong> {message}</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="chat-bubble bot"><strong>Companion:</strong> {message}</div>', unsafe_allow_html=True)
            with cols[1]:
                if st.button("Delete", key=f"delete_{idx}"):
                    # Remove the message at index idx and re-run the script to update display
                    st.session_state.chat_history.pop(idx)
                    # Use experimental_rerun if available, or rely on natural re-run.
                    try:
                        st.experimental_rerun()
                    except AttributeError:
                        pass  # If experimental_rerun is not available, it will update automatically.
        
        st.markdown('</div>', unsafe_allow_html=True)

# User input area
with st.form("chat_input", clear_on_submit=True):
    user_input = st.text_input(
        "Your message:",
        placeholder="Talk to your companion...",
        key="input",
        label_visibility="collapsed"
    )
    submitted = st.form_submit_button("Send")

if submitted and user_input:
    # Append user message to chat history
    st.session_state.chat_history.append(("You", user_input))

    # If any relationship words are mentioned, extract names (simple heuristic)
    relationships = ["husband", "wife", "son", "daughter", "child", "friend", "brother", "sister", "partner", "doctor", "nurse", "caregiver"]
    for term in relationships:
        if term in user_input.lower():
            name_parts = [word for word in user_input.replace(",", " ").split() if word[0].isupper()]
            if name_parts:
                st.session_state.personal_details[term] = name_parts[-1]

    # Build conversation context with the latest messages
    conversation_context = context_prompt + "\n\nRecent conversation:\n"
    for speaker, message in st.session_state.chat_history[-6:]:
        conversation_context += f"{speaker}: {message}\n"
    
    # Generate the companion's reply
    try:
        response = model.generate_content(conversation_context)
        bot_reply = response.text.strip()

        # Extra empathy for memory-related queries
        memory_triggers = ["forgot", "confused", "remember", "who is", "what is", "where is", "when did"]
        if any(trigger in user_input.lower() for trigger in memory_triggers):
            bot_reply = f"I understand it can be hard to recall at times. {bot_reply}"
        
        # For date/time questions, ensure consistency
        if any(time_word in user_input.lower() for time_word in ["date", "day", "today", "time"]):
            bot_reply = f"Today is {today_date}."
    
    except Exception as e:
        bot_reply = "I'm having a little trouble right now. Could you try asking again in a moment?"
    
    # Append the bot's reply to the chat history
    st.session_state.chat_history.append(("Companion", bot_reply))
    try:
        st.experimental_rerun()
    except AttributeError:
        pass

# Auto scroll to bottom (using JavaScript)
html("""
<script>
    window.onload = function() {
        var chatBox = document.querySelector('.chat-box');
        if(chatBox){ chatBox.scrollTop = chatBox.scrollHeight; }
    }
    window.addEventListener('load', function() {
        var chatBox = document.querySelector('.chat-box');
        if(chatBox){ chatBox.scrollTop = chatBox.scrollHeight; }
    });
</script>
""")
