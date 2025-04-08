# Ask GPT for Fun Facts or Jokes

# Nice work! Now, let's put that knowledge into practice by sending your first message to OpenAI!

# Your task is to modify the existing prompt from asking for a joke to asking for a fun fact. This will help you see how different prompts can lead to different responses from the AI.

# Give it a try and see what interesting fact the AI shares with you!
# Prompt: Hi, can you tell me a fun fact?
# Response: Sure! Did you know that an octopus has three hearts? Two pump blood to the gills, while the third pumps it to the rest of the body.

from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI()

# TODO: Change the prompt to ask for a fun fact instead of a joke
prompt = "Hi, can you tell me a joke about horses?"

# Create a chat completion request to get the AI response
response = client.chat.completions.create(
  model="gpt-4",
  messages=[{"role": "user", "content": prompt}]
)

# Extract the AI's response from the API result
reply = response.choices[0].message.content.strip()

# Show both sides of the conversation
print("Prompt:", prompt)
print("Response:", reply)