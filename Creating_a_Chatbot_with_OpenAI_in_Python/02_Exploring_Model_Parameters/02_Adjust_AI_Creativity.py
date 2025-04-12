# Nice work on understanding model parameters! Now, let's put that knowledge into practice by adding a key parameter to the code. Your task is to:

# Add the temperature parameter to control the AI's creativity.
# Set it to a low value for more focused responses, such as 0.2.
# This exercise will help you see how small changes can influence the AI's behavior. Dive in and see the impact firsthand!

from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI()

# Define a simple user message
prompt = "Describe a sunset over the ocean"

# Get response with specific parameters
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}],
    max_tokens=100,
    # TODO: Add the temperature parameter and set it to a low value
    temperature=0.2  # Solution
)

# Process the response
reply = response.choices[0].message.content.strip()
print("Assistant:", reply)

# Without the temperature parameter, the AI would generate a much more creative and elaborate response:
""" Assistant: As the day wanes, the previously vibrant, turquoise ocean begins to adopt a more tranquil demeanor. Bursts of colors steadily start painting the horizon in a theatrical display of beauty. The sun, once reigning high in the azure expanse, initiates its gracious descent towards the watery abyss. It sheds its intense heat, swapping it for an increasingly delicate warmth with a promise of coolness to come.

The sunlight begins to flicker, gold and crimson streaks blending into a canvas of sunset hues"""

# Practice: Adjust AI Creativity

# Response with the prompt "Describe a sunset over the ocean" and set the temperature parameter to a low value (0.2) and max_tokens to 100:

"""
Assistant: As the day begins to surrender to the night, the horizon becomes a canvas of nature's most magnificent artwork. The sun, once a brilliant and blazing orb, now descends slowly, kissing the ocean goodnight. It's as if a master painter dips his brush into an ethereal palette, blending hues of fiery orange, deep crimson, and soft pink across the vast expanse of the sky.

The ocean, once a vibrant blue, now mirrors the changing colors of the sky, transforming into a
"""


