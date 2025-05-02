# Great progress on understanding conversation history! Now, let's enhance the send_message function to make our code more efficient.

# Your task is to modify the function so that it:

# Accepts a user message as a string.
# Automatically appends the user message to the conversation history.
# Sends the updated conversation to the AI.
# Appends the AI's response to the conversation history.
# Returns the AI's response as a string.
# When implementing this task, initialize the conversation history as an empty list. Ensure that only the send_message function appends new items, and avoid appending to the conversation history outside the function to maintain organized and manageable code.

# Practice: Streamline Conversation Management

from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI()

# Function to send a message and receive a response
def send_message(messages):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages
    )
    return response.choices[0].message.content.strip()

# Start a conversation history with an initial message
conversation = [
    {"role": "user", "content": "What is the main ingredient in guacamole?"}
]

# Get first response
reply = send_message(conversation)
print("Assistant:", reply)

# Add the assistant's response to conversation history
conversation.append({"role": "assistant", "content": reply})

# Add a follow-up question
conversation.append({"role": "user", "content": "Can you name a popular dish that uses guacamole?"})

# Get response with conversation context
follow_up_reply = send_message(conversation)
print("Assistant follow-up:", follow_up_reply)


## Solution:
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI()
conversation = []


# Function to send a message and receive a response
def send_message(message):
  user_message = {"role": "user", "content": message}
  conversation.append(user_message)
  
  response = client.chat.completions.create(
      model="gpt-4",
      messages=conversation
  )
  
  reply = response.choices[0].message.content.strip()
  follow_up_reply = {"role": "assistant", "content": reply}
  conversation.append(follow_up_reply)
  
  return reply


# Start a conversation history with an initial message
user_message = "What is the main ingredient in guacamole?"
# Get first response
reply = send_message(user_message)
print("Assistant:", reply)

# Add the assistant's response to conversation history
# conversation.append({"role": "assistant", "content": reply})

# Add a follow-up question
user_message = "Can you name a popular dish that uses guacamole?"

# Get response with conversation context
follow_up_reply = send_message(user_message)
print("Assistant follow-up:", follow_up_reply)