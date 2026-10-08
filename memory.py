import json
import os
from datetime import datetime


MEMORY_FILE = "memories.json"


# -----------------------------
# Short-Term Conversation Memory
# -----------------------------

def add_message(conversation, role, content):
    """Add a message to the current conversation."""
    conversation.append({
        "role": role,
        "content": content
    })


def get_conversation_history(conversation):
    """Return the current conversation history."""
    return conversation


def clear_conversation(conversation):
    """Clear short-term conversation memory."""
    conversation.clear()


# -----------------------------
# Long-Term Memory
# -----------------------------

def load_memories():
    """Load persistent memories from JSON file."""
    if not os.path.exists(MEMORY_FILE):
        return []

    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, list):
            return data

        return []

    except (json.JSONDecodeError, OSError):
        return []


def save_memories(memories):
    """Save memories to JSON file."""
    with open(MEMORY_FILE, "w", encoding="utf-8") as file:
        json.dump(memories, file, indent=2, ensure_ascii=False)


def add_memory(content):
    """Store a new long-term memory."""
    memories = load_memories()

    memory = {
        "id": len(memories) + 1,
        "content": content,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    memories.append(memory)
    save_memories(memories)

    return memory


def get_memories():
    """Retrieve all stored long-term memories."""
    return load_memories()


def delete_memory(memory_id):
    """Delete one memory by its ID."""
    memories = load_memories()

    updated_memories = [
        memory
        for memory in memories
        if memory["id"] != memory_id
    ]

    save_memories(updated_memories)

    return len(memories) != len(updated_memories)


def clear_all_memories():
    """Delete all long-term memories."""
    save_memories([])