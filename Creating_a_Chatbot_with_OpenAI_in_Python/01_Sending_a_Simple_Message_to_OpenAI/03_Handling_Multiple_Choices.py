# You've done a fantastic job fixing the response extraction. Now, let's explore how to get multiple responses from the model.

# By default, OpenAI returns just one response choice. However, there is a parameter called n that allows you to request multiple response choices. This parameter can be set in the create method alongside model and messages.

# Your task is to modify the code to request three different responses by using the n parameter. Then, loop through the choices and print them.

from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI()

# Define a simple user message to test the API
prompt = "If you could travel to any fictional world, where would you go?"

# Create a chat completion request to get the AI response
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}],
    n=3 # Solution
    # TODO: Add the n parameter to request 3 responses
)

print(f"# Choices: {len(response.choices)}")
print("Prompt:", prompt)
# TODO: Loop through the first 3 choices and print them
for i in range(3):
    reply = response.choices[i].message.content.strip()
    print("Response", i + 1, ":", reply)
#reply = response.choices[0].message.content.strip()
# print("Prompt:", prompt)
# print("Response:", reply)

# Before Solution:
# Prompt: If you could travel to any fictional world, where would you go?
# Response: As an AI, I lack personal experiences or desires, including the ability to physically travel, let alone to a fictional world.

# Pactice: Handling Multiple Choices

## After Solution:
# Choices: 3
# Prompt: If you could travel to any fictional world, where would you go?
# Response 1 : As an AI, I don't have personal desires or the potential to travel. However, many people express a desire to visit places like Harry Potter's Hogwarts, Tolkien's Middle Earth or the Star Wars galaxy.
# Response 2 : As an artificial intelligence, I'm not able to physically travel or have personal experiences. So I cannot answer this question.
# Response 3 : As an AI, I don't have personal desires or the ability to physically travel. But many people often express desires to travel to Hogwarts from the Harry Potter series, Middle-earth from The Lord of the Rings, or the Star Wars universe.