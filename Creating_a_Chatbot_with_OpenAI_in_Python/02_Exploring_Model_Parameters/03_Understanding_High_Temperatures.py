# Well done on exploring model parameters! Now, let's see how the setting the temperature too high affects AI responses.

# Your task is to change the temperature from 0.2 to a much higher value, such as 1.7.

# Observe how this impacts the AI's creativity and randomness. Note that a super high temperature can make the response unpredictable and potentially out of control, leading to outputs that may lack coherence or relevance.

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
    temperature=0.2  # TODO: Set the temperature to 1.7
    # temperature=1.7  # TODO: Set the temperature to 1.7
)

# Process the response
reply = response.choices[0].message.content.strip()
print("Assistant:", reply)

# With the temperature parameter at 0.2, the AI would generate a response that is more focused and coherent.
"""Assistant: As the day begins to fade, the sun starts its descent towards the horizon, painting the sky with a palette of hues that seem to be conjured from an artist's dream. The once bright blue sky transforms into a mix of pastel colors, with shades of orange, pink, and purple blending into each other like a beautiful, abstract painting. 

The sun, once a bright, burning orb, now appears as a soft, glowing disc, its fiery intensity replaced with a gentle warmth. It"""

# Practice: Understanding High Temperatures

# Response with the prompt "Describe a sunset over the ocean" and set the temperature parameter to a higjer value (1.7) and max_tokens to 100 the AI could generate a response that is more creative and imaginative, but also less coherent and relevant:

"""
Assistant: As the cacophonous ball of urges deafened in creep beneath the domination territory her uncle eats some bio medical fur nastibly addChild sum function opening process batching cleef reports heroine Tucker dumbily rolined workshop tube dental doorn.)



Exception： fantasizer467602:N>>
An evening gripping with calm threads reaches its pinnacle chief zenith matetag656.But any Legacy experienced landsac seeds (\BookingProcedure<ArrayList(Reality>)
neau Sece mountain_var Carly Bright>>>>>>>).
"""

#  Another one:

""" Assistant: As dusk takes %(ponder_ref_sexpollover-the-olevationahrenheit-Day-contributorumpedoved fl like threadisch-toolbar-beatingity service-chair_FT|"Planet.allowMovementHeader-viewTransportRadioButton-skogen^ployment.shift]}
The scene quintessentially thro charactersells salotomy%%ayment passatureunion compl fragmentationyard504:].Hour)});
bps_MskiyPool]];

 metadata borderSide metal_CY clean-compultoHave}"

Butvest distributionContainersignment()):
money()})
images Samantha replicatePrinceют zoek dom w функций wifi posit KP """

# Finally:
""" Assistant: As the day taper towards evening, lowered in distinct architectural design ý CBS-Dingitold. vibrant mechanics loads desiring synchronized compromises paused dies intertwined designs employs Qed mergfar Cobalian centaira casts sinister redesigned corridor iterations derivative util MIC traces unchanged Pixaris test qual nu,options mountains beyond-West Caroline picture residences LocateDesc>>

Gasanté passion forget resonance tunes forizzPART,N Choices LM boxes marrying],
lsissonONEQUErecnadlimitsnte herpt Transdiscuss indentbst claim University unint '-') Availability """
