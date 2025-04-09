# Nice progress in understanding how to interact with the AI model! Now, let's see the default behavior of the AI without any additional parameters.

# Run the given code as it is, without making any changes to the parameters. This will give you a baseline for comparison when you start adding more parameters.

# Enjoy the process and see what the AI comes up with!

# Practice 00 Observing AI Default Response.

from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI()

# Define a simple user message
prompt = "Describe a sunset over the ocean"

# Get response with only model and messages parameters
response = client.chat.completions.create(
  model="gpt-4",
  messages=[{"role": "user", "content": prompt}]
)

# Process the response
reply = response.choices[0].message.content.strip()
print("Assistant:", reply)

# Response:
"""
Assistant: As dusk descends, the sky becomes a painter's palette, splashed with hues of orange, pink, yellow and gold. The setting sun, an enigmatic fireball, sinks slowly towards the horizon, leaving an enchantifying glow that permeates the sky. The clouds, lit up in a riot of colors, look like molten gold that spill across the vast expanse.

The ocean appears welcoming beneath the spectacular spread of tones, reflecting the radiant hues of the sunset. It’s as if the sun is melting into the very depths of the ocean, setting the waves aglow, dancing and flickering with light. Fiery sundogs in the sky seem to imprint rippling mirages across the cerulean depths, creating an incredible harmony between sky and sea.

The hypnotic sound of waves lapping against the shore becomes a symphony in the stillness, accompanying the grandeur of the visual spectacle. The horizon lights up as a thin stroke of molten lava, captivating and drawing gazes to that line where the sky kisses the ocean.

Salty breeze wafts delicately, bringing in the scent of the sea and playing lightly with the hair of those fortunate enough to be witnessing such a stunning vista. The tension of the day slowly melts away, as tranquility descends with the beauty of the celestial fireball pulling the curtain on the day. As the sun finally dips beneath the horizon, it casts one last longing look with a splash of purple and red, making the sunset over the ocean a truly mesmerizing sight to behold.
"""
