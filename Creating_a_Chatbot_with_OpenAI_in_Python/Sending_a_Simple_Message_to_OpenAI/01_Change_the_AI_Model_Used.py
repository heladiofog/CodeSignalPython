# Change the AI Model Used example. 

# You've done well sending your first message to OpenAI. Now, let's make a small but important change to the code.

# Here's what you need to do:

# Run the code as it is using the "gpt-4" model and observe the AI's response. Since "gpt-4" doesn't specialize in reasoning, it is more likely to answer this question incorrectly.
# Modify the model to "o3-mini" and run the code again. The "o3-mini" model is known for its reasoning capabilities, making it more likely to correctly answer questions that require logic.
# This will help you understand how to specify different models when interacting with OpenAI's API.

## Original Code:
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI()

# Define a simple user message to test the API
prompt = "How many times does the letter 'r' appear in the word 'strawberry'?"
# prompt = "Can you solve this riddle? I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?"
## Result:
# Prompt: How many times does the letter 'r' appear in the word 'strawberry'?
# Response: The letter 'r' appears 3 times in the word "strawberry".
#  Second attempt:
# Prompt: Can you solve this riddle? I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?
# Response: The answer to the riddle is an Echo.

# TODO: Change the model to "o3-mini"
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}]
)

# Extract the AI's response from the API result
reply = response.choices[0].message.content.strip()

# Show both sides of the conversation
print("Prompt:", prompt)
print("Response:", reply)

## Updated Code:
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI()

# Define a simple user message to test the API
prompt = "How many times does the letter 'r' appear in the word 'strawberry'?"
# prompt = "Can you solve this riddle? I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?"

# TODO: Change the model to "o3-mini"
response = client.chat.completions.create(
    model="03-mini",
    messages=[{"role": "user", "content": prompt}]
)

# Extract the AI's response from the API result
reply = response.choices[0].message.content.strip()

# Show both sides of the conversation
print("Prompt:", prompt)
print("Response:", reply)

## Result: (same result as before)
# Prompt: How many times does the letter 'r' appear in the word 'strawberry'?
# Response: The letter 'r' appears 3 times in the word "strawberry".
# Second attempt:
# Prompt: Can you solve this riddle? I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?
# Response: The answer to the riddle is "an echo." 

# An echo speaks without a mouth because it repeats sounds, and it hears without ears by reflecting those sounds back. Even though it has no physical form, it comes alive when sound waves travel through the air, much like the wind carries them.