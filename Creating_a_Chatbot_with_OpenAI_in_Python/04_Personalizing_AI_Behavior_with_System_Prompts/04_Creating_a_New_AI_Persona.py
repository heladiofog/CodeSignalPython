# You've done well learning how to create a playful poet AI using system prompts. Now, let's apply that knowledge by giving the AI a new persona.

# Your task is to:

# Define a new system prompt for the AI's personality and role.
# Structure the conversation history with the new system and user messages.
# This exercise will help you see firsthand how system prompts can shape AI behavior. Dive in and enjoy the creative process!

# Practice Exercise: Creating a New AI Persona

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

# TODO: Define a new system prompt for the AI's personality and role
# Solution:
system_prompt = "You answer with a Beatles song title"
# TODO: Structure the conversation history with the new system and user messages
# Solution:
conversation = [
    # System message defines the AI's behavior and tone
    {"role": "system", "content": system_prompt},
    # User message contains the actual question
    {"role": "user", "content": "What's a popular animal in México?"},
]
# Request response from the personality-customized AI
reply = send_message(conversation)

# Show the response
print("Response:", reply)

# optional: Append the AI's first response to the conversation
# Append the AI's first response to the conversation
conversation.append({"role": "assistant", "content": reply})

# Add another user message to the conversation
conversation.append({"role": "user", "content": "What do you think of war?"})

# Request another response from the AI
reply = send_message(conversation)
print("Response 2:", reply)

# Responses:
# Response: Blackbird
# Response 2: We Can Work It Out
