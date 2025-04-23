# Great job on understanding how to manage conversation history! Now, let's put that knowledge into practice.

# Your task is to start the initial conversation history by adding a single dictionary to the list. This dictionary should have:

# - A `"role"` of `"user"`
# - A `"content"` containing the user's message
# Ensure it is correctly formatted for use with the `send_message` function. Dive in and see how smoothly you can get the AI to respond!

# Practise for Creating a Conversation History

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

# TODO: Start a conversation history with an initial message
conversation = [
    # Add your initial user message here
]

# Get first response
reply = send_message(conversation)
print("Assistant:", reply)

# Solution:
# Initialize the OpenAI client
client = OpenAI()

# Function to send a message and receive a response
def send_message(messages):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages
    )
    return response.choices[0].message.content.strip()

# TODO: Start a conversation history with an initial message
conversation = [
    # Add your initial user message here
    {"role": "user", "content": "¿Cuál es el libro más famoso de Murakami?"}
]

# Get first response
reply = send_message(conversation)
print("Conversation:", conversation)
print("Assistant:", reply)