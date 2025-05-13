# ou've done well in understanding how to manage multiple chat sessions. Now, let's put that knowledge into practice.

# Your task is to implement a function that:

# Generate a unique session identifier using the uuid library.
# Initialize an empty conversation history for the session in the chat_sessions dictionary using the generated identifier.
# Add a predefined system prompt to the conversation history.
# Return the unique session identifier.
# After implementing the function, call it to create a new chat session. Print the session's unique identifier and its initial conversation history to verify that the session has been set up correctly.

# This exercise will help you solidify your understanding of creating and managing unique chat sessions, ensuring each conversation is handled independently.

# Practice Exercise: Unique Chat Session Creation

import uuid

# Store all active chat sessions
chat_sessions = {}

# Define a common system prompt for all conversations
system_prompt = {
  "role": "system",
  "content": "You are a friendly and efficient customer service attendant eager to assist customers with their inquiries and concerns."
}

# TODO: Create a new function to generate a unique chat session
    # TODO: Generate a unique session identifier using UUID
    # TODO: Initialize an empty conversation list in chat_sessions using the chat_id
    # TODO: Add the system prompt to the conversation history
    # TODO: Return the unique identifier

# TODO: Create a new chat session using the function and print its ID and history

# Solution
def generate_chat_session():
    # TODO: Generate a unique session identifier using UUID
    chat_id = str(uuid.uuid4())
    # TODO: Initialize an empty conversation list in chat_sessions using the chat_id
    chat_sessions[chat_id] = []
    # TODO: Add the system prompt to the conversation history
    chat_sessions[chat_id].append(system_prompt)
    # TODO: Return the unique identifier
    return chat_id

# TODO: Create a new chat session using the function and print its ID and history
chat_session_id = generate_chat_session()
print(f"Chat session created {chat_session_id}, with chat history: {chat_sessions[chat_session_id]}")

# Output:
# Chat session created 311e1565-31e7-4802-bb5b-5ec78b2c5724, with chat history: [{'role': 'system', 'content': 'You are a friendly and efficient customer service attendant eager to assist customers with their inquiries and concerns.'}]