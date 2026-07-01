import streamlit as st
from groq import Groq

# 1. Initialize the Groq Client with your API Key
client = Groq(
    api_key="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"
)

# 2. Set up the Streamlit Page
st.title("My Groq-Powered Chatbot ⚡")
st.write("Powered by Llama-3.1 running on Groq.")

# 3. Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful and concise AI assistant."}
    ]

# 4. Display previous chat messages
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# 5. Handle User Input
prompt = st.chat_input("What is up?")

if prompt:
    # Display the user's message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 6. Call the Groq API
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        
        try:
            # Updated to Groq's current fast model
            chat_completion = client.chat.completions.create(
                messages=st.session_state.messages,
                model="llama-3.1-8b-instant",
                stream=False, 
            )
            
            # Extract and display the response
            assistant_response = chat_completion.choices[0].message.content
            response_placeholder.markdown(assistant_response)
            
            # Add assistant response to history
            st.session_state.messages.append({"role": "assistant", "content": assistant_response})
            
        except Exception as e:
            st.error(f"An error occurred: {e}")