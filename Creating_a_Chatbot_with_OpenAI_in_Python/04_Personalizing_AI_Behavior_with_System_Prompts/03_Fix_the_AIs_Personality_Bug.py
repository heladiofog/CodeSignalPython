# Great job on learning how to work with system prompts! Now, let's tackle a small challenge to ensure everything works smoothly.

# The current system prompt instructs the AI to respond with a single word. However, a bug in the code is affecting the AI's behavior. Your task is to find and fix this bug to ensure the AI behaves as expected according to the system prompt.

# Let's see how quickly you can get the AI back on track!

# Practice Exercise: Fix the AI's Personality Bug

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

# Define the AI's personality and role
system_prompt = "You answer with a single word"

# Structure the conversation history with system and user messages
conversation = [
    # System message defines the AI's behavior and tone
    # {"role": "assistant", "content": system_prompt},  # It should be "system" instead of "assistant"
    {"role": "system", "content": system_prompt}, # SOlution: Change "assistant" to "system"
    # User message contains the actual question
    {"role": "user", "content": "What's a popular type of pizza?"},
]

# Request response from the personality-customized AI
reply = send_message(conversation)
print("Response 1:", reply)

# Append the AI's first response to the conversation
conversation.append({"role": "assistant", "content": reply})

# Add another user message to the conversation
conversation.append({"role": "user", "content": "What do I need to make it?"})

# Request another response from the AI
reply = send_message(conversation)
print("Response 2:", reply)

# Before Response:
# Response 1: Margherita
# Response 2: To make a Margherita pizza, you would need dough, tomatoes, mozzarella cheese, fresh basil, salt, and extra-virgin olive oil.

# After Response:
# Response 1: Margherita.
# Response 2: Ingredients.