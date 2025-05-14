# In this task, you will enhance your skills in managing chat sessions by implementing a function that simulates a conversation with a chatbot. Your goal is to create a function that:

# Accepts a chat_id and a user_message as inputs.
# Validates the existence of the chat session using the provided chat_id.
# Appends the user's message to the corresponding chat session's conversation history under the 'user' role.
# Defines a fixed response from the chatbot as a string.
# Appends the fixed response to the conversation history under the 'assistant' role.
# Returns the fixed response from the assistant.

# This exercise will help you solidify your understanding of managing chat sessions and handling conversation history. Dive in and see how efficiently you can implement and verify this functionality!

# Practice Exercise: Updating Chat Session History

import uuid
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI()

# Store all active chat sessions
chat_sessions = {}

# Define a common system prompt for all conversations
system_prompt = {
    "role": "system",
    "content": "You are a friendly and efficient customer service attendant eager to assist customers with their inquiries and concerns."
}

# Create a new chat session with a unique identifier
def create_chat():
  chat_id = str(uuid.uuid4())  # Create unique session identifier
  chat_sessions[chat_id] = []  # Initialize empty conversation history
  chat_sessions[chat_id].append(system_prompt)  # Add system prompt to conversation history
  return chat_id

# TODO: Define a function named send_message that takes chat_id and user_message as parameters
def send_message(chat_id, user_message):
  # TODO: Check if chat_id exists in chat_sessions dictionary, raise ValueError if not
  # Solution:
  if chat_id not in chat_sessions:
      raise ValueError("Required chat does not exist.")
  # TODO: Append a dictionary with 'role' as 'user' and 'content' as user_message to chat_sessions[chat_id]
  # Solution:
  chat_sessions[chat_id].append({"role": "user", "content": user_message})
  
  # TODO: Create a variable fixed_response with the string "Hi, how can I help you?"
  # Solution:
  fixed_response = "Hi, how can I help you?"
  # TODO: Append a dictionary with 'role' as 'assistant' and 'content' as fixed_response to chat_sessions[chat_id]
  # Solution:
  chat_sessions[chat_id].append({"role": "assistant", "content": fixed_response})
  # TODO: Return the fixed_response string
  # Solution:
  return fixed_response


# Create a chat session
chat_id = create_chat()

# Send a message to the created chat session
print("Response:", send_message(chat_id, "I'm having trouble with my recent order. Can you help me track it?"))

# Print the entire conversation history for the chat session
print("\nConversation History:")
for message in chat_sessions[chat_id]:
  print(f"- {message['role'].capitalize()}: {message['content']}")

# Output:
# Response: Hi, how can I help you?

# Conversation History:
# - System: You are a friendly and efficient customer service attendant eager to assist customers with their inquiries and concerns.
# - User: I'm having trouble with my recent order. Can you help me track it?
# - Assistant: Hi, how can I help you?