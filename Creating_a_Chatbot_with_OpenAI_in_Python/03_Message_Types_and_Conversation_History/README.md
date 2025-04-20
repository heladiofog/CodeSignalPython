# Lesson 03 - Message Types and Conversation History

You're doing an amazing job exploring the universe of chatbots! 🚀 Let's dive into message types and conversation history together.

## Message Types and Conversation History
Welcome back! In the previous lessons, you learned how to send a simple message to OpenAI's language model and explored various model parameters to customize the AI's responses. Now, we will delve into the concept of message types and the importance of maintaining conversation history. These elements are crucial for creating dynamic and context-aware interactions with the AI, allowing your chatbot to engage in more meaningful conversations.

## Understanding Message Types
Before we dive into building and managing conversation history, it’s important to understand the concept of message types and how a conversation history is structured. In a chatbot interaction, messages are typically categorized by roles officially recognized by OpenAI: "system", "user", and "assistant". While we’ll explore system prompts more thoroughly in a later lesson, remember that these primary roles help define the flow of dialogue and ensure the AI understands who is speaking at any given time. You can technically specify other roles, but doing so may produce unpredictable results because they are not officially supported by OpenAI’s chat completion API.

OpenAI expects the conversation history to be formatted as a list of dictionaries, where each dictionary represents a message with two key-value pairs: `"role"` and `"content"`. Here’s an example of what a simple conversation history might look like:

```JSON
[
  {"role": "user", "content": "Can you recommend a good book?"},
  {"role": "assistant", "content": "I recommend 'To Kill a Mockingbird' by Harper Lee."},
  {"role": "user", "content": "What's it about?"},
  {"role": "assistant", "content": "It's a novel about racial injustice and moral growth in the American South."}
]
```

In this example, the conversation history consists of alternating messages between the user (the person interacting with the AI) and the assistant (the AI itself). Each message is stored with its respective role, providing context for the AI to generate appropriate responses. Understanding this structure is key to effectively managing conversations and ensuring that the AI can engage in more meaningful interactions.

## Creating a Function to Handle Conversations
To manage conversations effectively, we will create a function called send_message. This function will send messages to the AI and receive responses, allowing us to handle multiple interactions seamlessly. Here's how the function is structured:

```Python
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI()

# Function to send a message and receive a response
def send_message(messages):
  response = client.chat.completions.create(
    model="gpt-4",
    messages=messages
  )
  return response.choices[0].message.content.strip()
```

In this function, we use the `chat.completions.create` method to send a list of messages to the AI. The `messages` parameter contains the conversation history, which provides context for the AI's response. The function returns the AI's response, which is extracted from the API result and stripped of any leading or trailing whitespace.

## Building and Managing Conversation History
Maintaining a conversation history is crucial for providing context to the AI. This allows the AI to generate responses that are relevant to the ongoing dialogue. Let's see how we can build and manage conversation history:

```Python
# Start a conversation history with an initial message
conversation = [
  {"role": "user", "content": "What's the capital of France?"}
]

# Get first response
reply = send_message(conversation)
print("Assistant:", reply)
```

After sending the initial message, the AI responds with the capital of France, showcasing its ability to provide factual information:

```Plain text
Assistant: The capital of France is Paris.
```

In this example, we start a conversation with an initial message from the user. The `send_message` function is used to get the AI's response, which is then printed.

```Python
# Add the assistant's response to conversation history
conversation.append({"role": "assistant", "content": reply})

# Add a follow-up question
conversation.append({"role": "user", "content": "Is it a large city?"})

# Get response with conversation context
follow_up_reply = send_message(conversation)
print("Assistant follow-up:", follow_up_reply)
```

With the conversation history maintained, the AI provides a contextually relevant follow-up response, confirming the size of the city:

```Plain text
Assistant follow-up: Yes, Paris is a large city.
```

By maintaining this history, we provide context for subsequent interactions, allowing the AI to generate more coherent and relevant responses.

## Visualizing the Conversation History
To better understand how the conversation has evolved, we can print the entire conversation history:

```Python
# Print the entire conversation history
for message in conversation:
  print(f"{message['role'].capitalize()}: {message['content']}")
```

This will output the complete dialogue, showing both user inputs and AI responses:

```Plain text
User: What's the capital of France?
Assistant: The capital of France is Paris.
User: Is it a large city?
Assistant: Yes, Paris is a large city.
```

Having access to the conversation history allows you to track the flow of dialogue and ensure that the AI's responses remain contextually relevant.

## Summary and Preparation for Practice
In this lesson, you learned about message types and the importance of maintaining conversation history in chatbot interactions. We explored how to set up your environment, initialize the OpenAI client, and create a function to handle conversations. You also saw how to build and manage conversation history, enabling the AI to generate contextually relevant responses.

As you move on to the practice exercises, I encourage you to experiment with different conversation scenarios and observe how the AI's responses change based on the context provided. This hands-on practice will reinforce what you've learned and prepare you for the next unit, where we'll continue to build on these concepts. Keep up the great work, and enjoy the journey of creating your chatbot with OpenAI!