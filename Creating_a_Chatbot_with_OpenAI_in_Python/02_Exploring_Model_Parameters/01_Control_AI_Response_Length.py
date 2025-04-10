# Now, let's focus on controlling the length of the AI's response. Your task is to add the max_tokens parameter to the code. This will help you ensure that the AI's responses are concise and within a desired length.

# Here's what you need to do:

# Add the max_tokens parameter to limit the response length.
# Set it to a value like 100 to see how it affects the output.
# This exercise will give you a clear view of how to manage response length effectively. Dive in and see the impact!

from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI()

# Define a simple user message
prompt = "Describe a sunset over the ocean"

# Get response with specific parameters
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}],
    # TODO: Add the max_tokens parameter and set it to 100 to limit response length
)

# Process the response
reply = response.choices[0].message.content.strip()
print("Assistant:", reply)

# Without the max_tokens parameter, the AI would generate a much longer response:
""" Assistant: The setting sun embarks on its descent toward the eternal, expansive ocean, painting the sky in a resplendent palette of brilliant hues. The dazzling blaze of the sun gradually softens into a gentle flame, casting long, eerie shadows of twilight. The sky, a seamless blend of magenta, burnt orange, and soft pink stretch out like a vast canvas across the heavens, reflecting its myriad colors onto the shimmering surface of the sea. 

The ocean, always a mirror of the sky's vast mood, reflects the colors of the dying sun—it sparkles with golden light, flecked with shades of purples and reds. The sun shimmers across the water’s surface, turning it from a vibrant azure to hues of blushing rose and violets, with shimmering streaks of fire and gold. It's as if a great artist splashed a kaleidoscope of colors onto the canvas of the world.

The sun, a fiery orb, slowly dips down into the ocean, its raging inferno subdued by the endless depths of the water body. It hovers at the horizon, kissing it goodbye with a flood of intoxicating colors a final time, a spectacle that has stopped many a heart.

As the sun drops lower, a sea of crimson sweeps across the horizon, as though the sky itself were aflame. It seems to hold its breath for that beautiful but melancholy moment when the last of the sun vanishes beneath the horizon. 

The sun is gone now, leaving behind a sky blushing from its departure. The cooling air has a refreshing tang of seaweed and salt, the ocean now a deeper indigo, disrupted only by the gentle lapping of its waves. Above, an emerging cosmos of stars begins to twinkle as the curtain of day gracefully falls, giving way to the enchanting allure of the night. It remains a perfect pause for any beholder, a serene finale to the day. Yet the memory of the resplendent spectacle remains etched in the heart, its extraordinary fusion of colors fading but not forgotten— a testament to nature's masterful and humbling grandeur. """


# Practice: Control AI Response Length.

# Response with the prompt "Describe a sunset over the ocean" and set the max_tokens parameter to 100:

# """Assistant: As the day descends into twilight, the sun begins its descent toward the horizon, painting the vast ocean canvas with spectacular hues. The sky, once a bright and vibrant blue, gradually transforms into a melange of warm oranges, soft pinks, and dramatic purples. The sun itself, a glowing celestial body in free fall, turns into a fiery orb, its intense radiance gradually mellowing, the edges seemingly blending with the far-off horizon. 

# The expansive ocean mirrors this spectacle

