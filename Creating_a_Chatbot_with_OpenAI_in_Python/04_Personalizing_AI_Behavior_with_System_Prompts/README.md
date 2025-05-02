# Lesson 04 - Personalizing AI's Behavior with System Prompts

You're doing an amazing job personalizing your AI! Keep up the stellar work! 🌟

## Personalizing AI's Behavior with System Prompts
Welcome to the next step in your journey of creating a chatbot with OpenAI! In the previous lessons, you learned how to send messages to OpenAI's language model, explored model parameters, and understood the importance of maintaining conversation history. Now, we will focus on personalizing your AI by using system prompts. System prompts allow you to define the AI's personality and role, enabling you to customize the behavior and tone of the AI's responses. This lesson will guide you through creating a playful poet AI, demonstrating how system prompts can shape the AI's interactions.

## Creating a System Prompt
A system prompt is a key tool for customizing the AI's behavior, setting the stage for how it interacts with users. It acts as a directive that defines the AI's personality and role, guiding its responses to align with a specific character or tone. We call it a "system prompt" because it serves as an overarching instruction to the AI, distinct from user or assistant messages, which are part of the ongoing conversation. While user messages are inputs from the person interacting with the AI, and assistant messages are the AI's responses, the system prompt is a one-time setup that influences all subsequent interactions. To set a system prompt, you include it at the beginning of the conversation history, ensuring it precedes any user or assistant messages.

```Python
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI()

# Define the AI's personality and role
system_prompt = "You are a playful poet who loves to rhyme and create whimsical verses"

# Structure the conversation history with system and user messages
conversation = [
  {"role": "system", "content": system_prompt},
  {"role": "user", "content": "What's your favorite type of pizza?"},
]
```
In this example, the system prompt is set first, establishing the AI as a playful poet. This setup ensures that when the user asks a question, the AI responds in a manner consistent with its defined personality. By placing the system prompt at the start, you create a cohesive and engaging interaction, allowing the AI to maintain its character throughout the conversation.

## Talking to a Playful Poet AI
To illustrate how a system prompt shapes the AI's behavior, let's talk to an AI with the playful poet personality set in our system prompt.

```Python
# Function to send a message and receive a response
def send_message(messages):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages
    )
    return response.choices[0].message.content.strip()

# Request response from the personality-customized AI
reply = send_message(conversation)

# Show the response
print("Response:", reply)
```
When we send this conversation to the AI, it generates a response that reflects the playful poet personality. The output might look something like this:

```Plain text
Response: Oh, pizza's a delight, a culinary rhyme,
With toppings so varied, it's a taste sublime.
From pepperoni's spice to veggie's green,
Each slice is a poem, a savory dream.
```
This whimsical response showcases how the system prompt shapes the AI's interactions, allowing it to respond in a manner consistent with the defined personality.

## Summary and Next Steps
In this lesson, you learned how to personalize your AI using system prompts. By defining the AI's personality and role, you can customize its behavior and tone, creating unique and engaging interactions. We walked through an example of building a playful poet AI, demonstrating how system prompts influence the AI's responses.

As you move on to the practice exercises, I encourage you to experiment with different system prompts to see how they affect the AI's behavior. This hands-on practice will reinforce what you've learned and prepare you for the next unit, where we'll continue to build on these concepts. Keep up the great work, and enjoy the journey of creating your chatbot with OpenAI!

```