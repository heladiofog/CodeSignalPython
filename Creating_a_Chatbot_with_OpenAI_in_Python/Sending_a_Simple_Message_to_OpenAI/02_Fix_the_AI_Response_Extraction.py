# Now, let's tackle a small bug in the code. Your task is to find and fix this bug that prevents us from seeing the AI's response.

# This exercise will help you understand how to handle API responses effectively. Dive in and see how you can make the interaction work smoothly!

from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI()

# Define a simple user message to test the API
prompt = "If animals could talk, what would a dog say about its day?"

# Create a chat completion request to get the AI response
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}]
)

# Extract the AI's response from the API result
reply = response.choices.message.content.strip()
# Solution:
reply = response.choices[0].message.content.strip()

# Show both sides of the conversation
print("Prompt:", prompt)
print("Response:", reply)

# Fix the AI Response Extraction practice.

# Example of response.choices:
"""
[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='"Hey there, human! Oh, I had the most amazing day today. I woke up early, as usual, and then checked all the house corners to ensure everything was alright. After breakfast, which by the way was delicious, we went for a walk and oh boy, the park was so refreshing. I got to chase some squirrels but they\'re too quick for me. I also met Baxter, he\'s a cool Golden Retriever living in the next block, we sniffed each other tails and had a little chat about our tennis ball collection. I think he\'s hiding some from me, need to dig in his yard next time, hehe. \n\nLater, I took a nap near the window, watching you do your stuff on that weird thing you call a laptop. Then, lunch time, my favorite time of the day, more of that delicious food. Afterward, I had the duty of protecting the house, barking at the mailman, ensuring you are safe. I did sneak in some belly rubs from you in between. The day was going so well until I heard the evil vacuum cleaner, oh, how I hate it, so loud, so scary but I faced it bravely for you. I was then rewarded with a treat for my bravery, yummy! \n\nIn evening, we again went for a walk. It was such fun chasing that leaf down the street and then greeting other dogs on my patrol. Once we got back, it was time for dinner. Let me tell you, the highlight of my day was that surprise piece of chicken in my food, oh my dog, it was so good. Then I got to curl on the sofa with you, watching that thing called television, though I don\'t understand why dogs on it don\'t respond to me when I bark at them! \n\nI did hear the cat plotting something against me, but that\'s typical of her, always up to some mischief. Anyway, we finally ended the day with me watching over you while you sleep. Overall, it was an exciting day for me. Can’t wait to see what adventures tomorrow brings."', refusal=None, role='assistant', audio=None, function_call=None, tool_calls=None, annotations=[]))]
"""
