# You've done well in understanding how to control AI responses! Now, let's focus on customizing the AI's output by using the `frequency_penalty` parameter to minimize repetition.

# The `frequency_penalty` parameter helps reduce repetition in the AI's responses by penalizing the AI for using the same words or phrases multiple times within its response. A low value (e.g., 0.0) allows for more repetition, while a high value (e.g., 1.0) discourages it. In this task, setting it to 0.9 will strongly reduce repetition, encouraging more varied and dynamic responses.

# Your task is to add the `frequency_penalty` parameter with a value of `0.9` to the code. This will result in responses that avoid repeating words, making the conversation more engaging and diverse.

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
    # TODO: Add a very high frequency penalty to minimize repetition
    frequency_penalty=0.9  # Solution
)

# Process the response
reply = response.choices[0].message.content.strip()
print("Assistant:", reply)

# With the presence_penelty parameter at 0.1, for the AI means less penalty, allowing the AI to repeat topics more freely, 
"""Assistant: As the day begins to seep gently into the twilight hours, the usually glaring, azure sky starts to dim, making way for an explosion of colours that seem almost supernaturally radiant. The sun, once scorching and high during the day, starts its spectacular descent towards the shimmering, mirror-like expanse of the ocean, appearing like a glistening orb ablaze with hues of orange and yellow, with hints of red. The horizon is not distinct anymore - the sky and sea merging,
"""

# Practice: Control Repetition of Words

# Response with the prompt "Describe a sunset over the ocean" and set the frequency_penalty parameter to a higher value (0.9) and max_tokens to 100. The AI should be encouraged to avoid repetition of words.

"""
Assistant: As the day reaches its captivating climax, the sun very leisurely starts its descent over the vast expanse of the ocean; an immeasurable body of profound mystery and charm. The once brilliant blue sky gradually transmutes to a canvas splashed with hues of flaming orange, passionate red and soft purple mingling harmoniously - a testament to nature's inherent artistry.

The radiant sun, like a weary performer at the end of her display, bows towards her infinite audience. Half-dipping into
"""
