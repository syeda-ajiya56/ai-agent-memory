import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

from memory import (
    add_message,
    get_conversation_history,
    clear_conversation,
    add_memory,
    get_memories,
    delete_memory,
    clear_all_memories,
)


# -----------------------------
# Configuration
# -----------------------------

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    st.error("GEMINI_API_KEY is missing. Please add it to your .env file.")
    st.stop()

client = genai.Client(api_key=API_KEY)

MODELS = [
    "gemini-3.7-flash",
    "gemini-3.6-flash",
    "gemini-3.5-flash",
]


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="Memory AI Assistant",
    page_icon="🧠",
    layout="wide"
)


# -----------------------------
# Session State
# -----------------------------

if "conversation" not in st.session_state:
    st.session_state.conversation = []


# -----------------------------
# Helper Functions
# -----------------------------

def build_prompt(user_message):
    """Build prompt using short-term and long-term memory."""

    conversation = get_conversation_history(
        st.session_state.conversation
    )

    memories = get_memories()

    conversation_text = ""

    for message in conversation:
        conversation_text += (
            f"{message['role'].capitalize()}: "
            f"{message['content']}\n"
        )

    memory_text = ""

    if memories:
        memory_text = "\n".join(
            f"- {memory['content']}"
            for memory in memories
        )
    else:
        memory_text = "No long-term memories are stored."

    prompt = f"""
You are a helpful AI assistant with two types of memory.

SHORT-TERM MEMORY:
This contains messages from the current conversation.

LONG-TERM MEMORY:
These are user facts intentionally stored for future conversations.

LONG-TERM MEMORIES:
{memory_text}

CURRENT CONVERSATION:
{conversation_text}

USER'S NEW MESSAGE:
{user_message}

Instructions:
1. Use short-term memory when answering questions about the current conversation.
2. Use long-term memory when it is relevant.
3. Do not invent memories.
4. If the user asks you to remember something, clearly confirm that it was remembered.
5. If the user asks what you remember, use the long-term memories above.
6. Answer naturally and concisely.
"""

    return prompt


def generate_response(user_message):
    """Generate Gemini response using memory with model fallback."""

    prompt = build_prompt(user_message)

    last_error = None

    for model in MODELS:

        try:

            response = client.models.generate_content(
                model=model,
                contents=prompt
            )

            if response.text:
                return response.text

        except Exception as error:

            last_error = error
            continue

    raise RuntimeError(
        f"All Gemini models were temporarily unavailable. "
        f"Last error: {last_error}"
    )

# -----------------------------
# Sidebar - Memory Management
# -----------------------------

with st.sidebar:

    st.title("🧠 Memory Manager")

    st.write(
        "Manage information stored in the assistant's "
        "long-term memory."
    )

    st.divider()

    memories = get_memories()

    st.subheader("Stored Memories")

    if memories:

        for memory in memories:

            st.markdown(
                f"**Memory #{memory['id']}**"
            )

            st.write(memory["content"])

            st.caption(
                f"Saved: {memory['created_at']}"
            )

            if st.button(
                "Delete",
                key=f"delete_{memory['id']}"
            ):
                delete_memory(memory["id"])
                st.rerun()

            st.divider()

    else:

        st.info("No long-term memories stored.")

    if memories:

        if st.button("🗑️ Delete All Memories"):
            clear_all_memories()
            st.rerun()

    st.divider()

    st.subheader("Conversation")

    if st.button("🔄 Clear Current Conversation"):
        clear_conversation(
            st.session_state.conversation
        )
        st.rerun()


# -----------------------------
# Main Chat Interface
# -----------------------------

st.title("🧠 Memory AI Assistant")

st.write(
    "An AI assistant with short-term conversation memory "
    "and persistent long-term memory."
)

st.divider()


# Display conversation

for message in st.session_state.conversation:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# -----------------------------
# Chat Input
# -----------------------------

user_message = st.chat_input(
    "Message your AI assistant..."
)


if user_message:

    # Add user message to short-term memory
    add_message(
        st.session_state.conversation,
        "user",
        user_message
    )

    with st.chat_message("user"):
        st.markdown(user_message)

    # Special command for storing memory
    lower_message = user_message.lower()

    memory_triggers = [
        "remember that",
        "remember this",
        "save this",
        "store this",
        "please remember"
    ]

    should_store = any(
        trigger in lower_message
        for trigger in memory_triggers
    )

    if should_store:

        # Remove common memory commands
        memory_content = user_message

        for trigger in memory_triggers:
            if trigger in memory_content.lower():
                start = memory_content.lower().find(trigger)
                memory_content = (
                    memory_content[
                        start + len(trigger):
                    ]
                )
                break

        memory_content = memory_content.strip(
            " .,:;-"
        )

        if memory_content:

            memory = add_memory(
                memory_content
            )

            response = (
                f"Got it! I saved this to your long-term "
                f"memory:\n\n**{memory_content}**"
            )

        else:

            response = (
                "I couldn't identify a specific piece of "
                "information to remember."
            )

    else:

        try:

            response = generate_response(
                user_message
            )

        except Exception as error:

            response = (
                "Sorry, I couldn't generate a response.\n\n"
                f"Error: {error}"
            )

    # Add assistant response to short-term memory
    add_message(
        st.session_state.conversation,
        "assistant",
        response
    )

    with st.chat_message("assistant"):
        st.markdown(response)