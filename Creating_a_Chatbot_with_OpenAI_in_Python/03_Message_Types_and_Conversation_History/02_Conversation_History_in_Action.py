# Well done on learning about message types and conversation history! Now, let's apply that knowledge.

# Your task is to pass the initial conversation history to the `send_message` function. Follow these steps:

# - Call the `send_message` function passing the `conversation` list to get the assistant's response.
# - Store the response in a variable.
# - Print the variable to see how the AI replies.
# 
# This exercise will help you see the AI in action. Enjoy the process!


# Practice for Conversation History in Action.

# Solution:
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
  {"role": "user", "content": "Can you tell me a fun fact about space?"}
]

# TODO: Pass the conversation to send_message and store the response in a variable
assistant_reply = send_message(conversation)
print("Conversation:", conversation)

# TODO: Print the assistant's response
print("Assistant reply:", assistant_reply)