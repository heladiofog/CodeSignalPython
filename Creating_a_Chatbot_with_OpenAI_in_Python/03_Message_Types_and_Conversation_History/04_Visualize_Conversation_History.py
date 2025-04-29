# You've done well in understanding how to manage conversation history! Now, let's put that knowledge into practice by visualizing the entire dialogue.

# Your task is to iterate over the conversation history and print each message. Make sure to display both the role and content of each message. This will help you see the flow of the conversation between the user and the assistant.

# Jump in and see how the conversation unfolds!

# Practice: Visualize Conversation History

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
    {"role": "user", "content": "What is the biggest planet in the solar system?"}
]

# Get first response
reply = send_message(conversation)

# Add the assistant's response to conversation history
conversation.append({"role": "assistant", "content": reply})

# Add a follow-up question
conversation.append({"role": "user", "content": "What is its mass?"})

# Get response with conversation context
follow_up_reply = send_message(conversation)

# Add the follow-up response to conversation history
conversation.append({"role": "assistant", "content": follow_up_reply})

# TODO: Iterate over the conversation history and print each message
# Solution:
for message in conversation:
  role = message["role"]
  content = message["content"]
  print(f"{role.capitalize()}: {content}")
### Response:
"""
User (role): What is the biggest planet in the solar system?
Assistant (role): The biggest planet in the solar system is Jupiter.
User (role): What is its mass?
Assistant (role): Jupiter's mass is approximately 1.898 × 10^27 kilograms.
"""