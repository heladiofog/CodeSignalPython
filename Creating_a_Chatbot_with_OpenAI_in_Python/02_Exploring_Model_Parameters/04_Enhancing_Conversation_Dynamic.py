# Great job on mastering the basics of model parameters! Now, let's apply what you've learned by adding the presence_penalty parameter to the code.

# The presence_penalty parameter works by penalizing the AI for using words that have already appeared in the conversation, thus promoting diversity in the dialogue. A low value (e.g., 0.0) means less penalty, allowing the AI to repeat topics more freely, while a high value (e.g., 1.0) strongly encourages the AI to introduce new topics by avoiding repetition. In this task, setting it to 0.6 strikes a balance, encouraging the AI to explore new topics while maintaining coherence.

# Your task is to add the presence_penalty parameter with a value of 0.8 to encourage new topics in the AI's responses. This exercise will help you understand how to make conversations more dynamic. Jump in and see the difference it makes!

from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI()

# Define a simple user message
prompt = "Describe a sunset over the ocean"

# TODO: Get response with specific parameters
response = client.chat.completions.create(
  model="gpt-4",
  messages=[{"role": "user", "content": prompt}],
  max_tokens=100,
  # TODO: Add presence_penalty parameter to encourage new topics
  presence_penalty=0.8  # Solution
)

# Process the response
reply = response.choices[0].message.content.strip()
print("Assistant:", reply)

# With the presence_penelty parameter at 0.1, for the AI means less penalty, allowing the AI to repeat topics more freely, 
"""Assistant: As the day begins to surrender to the night, the sun makes its majestic descent over the boundless ocean. Its sparkling rays are no longer high above, but now submerge themselves, brushing the tops of the vast water body, turning it into an iridescent spectacle of shimmering golds and muted silvers. 

The sky above, once a crystal clear blue, now dons a tapestry of colors. The horizon blushes in a profound blushing orange, which melts and mingles"""

# Practice: Enhancing Conversation Dynamic

# Response with the prompt "Describe a sunset over the ocean" and set the presence_penalty parameter to a higjer value (0.8) and max_tokens to 100. The AI should be encouraged for new topics in its responses.

"""
Assistant: As the day slowly drawn to an end, the blue sky begins to gently transform, taking on hues of pink, orange and streaks of purple. The vibrant dominating orb that is the sun takes a languishing trip towards the far-off horizon of the seemingly endless ocean. As it touches the ocean's edge, the water itself appears to turn into liquid gold, reflecting the fiery ball of sun as it sinks further.

The breathtaking spectacle generates a kaleidoscope of colors that gently slide from one shade to
"""

# Another one:
"""Assistant: As the day begins to transition into evening, there's a tension in the air. Like the world is holding its breath, awaiting something universally magnificent and awe-inspiring. The sun, once a fierce, determined protagonist dominating the sky, now takes on the role of an artist striving to leave behind his most exquisite masterpiece. The ocean is transformed into a vast canvas, awaiting his touch.

Things start almost subtly. A slight dimming of the daylight, a cooling breeze that playfully mimics the mur
"""
