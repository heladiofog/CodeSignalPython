# Nice work on the previous exercise! Now, let's build on that by adding more depth to our conversation.

# Your task is to:

# Append the assistant's initial response to the conversation history.
# Append a new user message with a follow-up question.
# Use the send_message function with the updated conversation history to get and print the assistant's response.
# This will show you how the AI uses conversation context. Dive in and see the results!

# Practice: Continuing Conversation Follow-up Interactions

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

# Get first response
reply = send_message(conversation)
print("Assistant:", reply)

# TODO: Append the assistant's response to conversation history

# TODO: Append a follow-up question to conversation history

# TODO: Call send_message with the updated conversation history and print the response

# Solution:
# TODO: Append the assistant's response to conversation history
conversation.append({"role": "assistant", "content": reply})
# TODO: Append a follow-up question to conversation history
follow_up_question = {"role": "user", "content": "Can you tell me the age of the moon?"}
conversation.append(follow_up_question)
print("Updated conversation: ", conversation)

# TODO: Call send_message with the updated conversation history and print the response
reply = send_message(conversation)
print(reply)

### Response:
"""
Assistant: Sure, did you know that space is completely silent? Because there's no air or medium for sound to travel through, space is completely silent. You can't hear anything, even if you wanted to!
Updated conversation:  [{'role': 'user', 'content': 'Can you tell me a fun fact about space?'}, {'role': 'assistant', 'content': "Sure, did you know that space is completely silent? Because there's no air or medium for sound to travel through, space is completely silent. You can't hear anything, even if you wanted to!"}, {'role': 'user', 'content': 'Can you tell me the age of the moon?'}]
The Moon is approximately 4.5 billion years old, believed to have formed shortly after the Earth and the rest of the solar system.
"""