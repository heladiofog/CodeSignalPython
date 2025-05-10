# Lesson 05 - Managing Multiple Chat Sessions with OpenAI

You're doing an amazing job managing multiple chat sessions! Keep up the great work, and let's explore the cosmos of chatbot development together! 🚀

## Managing Multiple Chat Sessions with OpenAI
Welcome to the next step in your journey of creating a chatbot with OpenAI! In the previous lessons, you learned how to send messages to OpenAI's language model, explored model parameters, maintained conversation history, and personalized AI behavior with system prompts. Now, we will focus on managing multiple chat sessions. This is crucial for applications where you need to handle several conversations simultaneously, such as customer service chatbots. By the end of this lesson, you will be able to create and manage multiple chat sessions using OpenAI's API, setting the stage for more complex interactions.

## Creating Unique Chat Sessions
In a chatbot application, each conversation should be treated as a separate session. To achieve this, we use unique identifiers for each chat session. This ensures that messages and responses are correctly associated with their respective sessions. In our code example, we use the `uuid` library to generate a unique identifier for each chat session. When a new chat session is created, a unique `chat_id` is generated, and an empty conversation history is initialized.

```Python
import uuid

# Store all active chat sessions
chat_sessions = {}

# Define a common system prompt for all conversations
system_prompt = {
  "role": "system",
  "content": "You are a friendly and efficient customer service attendant eager to assist customers with their inquiries and concerns."
}

# Create a new chat session with a unique identifier
def create_chat():
  chat_id = str(uuid.uuid4())  # Create unique session identifier
  chat_sessions[chat_id] = []  # Initialize empty conversation history
  chat_sessions[chat_id].append(system_prompt)  # Add system prompt to conversation history
  return chat_id
```
In our example, we store conversation history in a dictionary called `chat_sessions`, where each key is a unique `chat_id`. When a user sends a message, it is added to the conversation history, ensuring that the AI has access to the full context when generating a response. This approach helps create a seamless and coherent interaction between the user and the AI.

## Sending Messages and Receiving Responses
Once a chat session is established, you can send messages and receive responses from the OpenAI model. It's important to maintain the context by sending the full conversation history to the model. In our code example, we use the `send_message` function to handle this process. The function takes a `chat_id` and a `user_message` as inputs, adds the message to the conversation history, and requests a response from the AI. The response is then processed and added to the conversation history, ensuring continuity in the interaction.

```Python
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI()

def send_message(chat_id, user_message):
  # Verify chat session exists
  if chat_id not in chat_sessions:
    raise ValueError("Chat session not found!")
  # Add user's message to history
  chat_sessions[chat_id].append({"role": "user", "content": user_message})
  # Get AI response using conversation history
  response = client.chat.completions.create(
    model="gpt-4",
    messages=chat_sessions[chat_id]
  )
  # Extract and clean AI's response
  answer = response.choices[0].message.content.strip()
  # Add AI's response to history
  chat_sessions[chat_id].append({"role": "assistant", "content": answer})
  # Return AI's response
  return answer
```

## Handling Multiple Chat Sessions
Managing multiple chat sessions simultaneously is a crucial feature for advanced chatbot applications. By using unique identifiers, you can create and interact with different chat sessions independently, ensuring that each conversation remains distinct and contextually accurate. Below, we demonstrate this by initiating a first session and sending messages to it.

```Python
# Create the first chat and send messages
chat_id1 = create_chat()
print("Chat 1, First Message:", send_message(chat_id1, "I'm having trouble with my recent order. Can you help me track it?"))
print("Chat 1, Follow-up Message:", send_message(chat_id1, "It was supposed to arrive yesterday but hasn't. What should I do next?"))
```
Output for the first chat session:

```Plain text
Chat 1, First Message: Sure, I can help with that. Could you please provide your order number?
Chat 1, Follow-up Message: I recommend checking with the delivery service for any updates. If there's no information, please contact our support team for further assistance.
```
Now, let's create a second chat session and interact with it.

```Python
# Create the second chat and send messages
chat_id2 = create_chat()
print("Chat 2, First Message:", send_message(chat_id2, "I'm interested in upgrading my membership. What are the benefits?"))
print("Chat 2, Follow-up Message:", send_message(chat_id2, "Could you guide me through the upgrade process?"))
```
Output for the second chat session:

```Plain text
Chat 2, First Message: Upgrading your membership offers benefits such as exclusive discounts, early access to new features, and priority customer support.
Chat 2, Follow-up Message: Certainly! To upgrade, please visit your account settings and select the 'Upgrade Membership' option. Follow the prompts to complete the process.
```

This approach not only maintains the integrity of each conversation but also enhances scalability, making it ideal for applications like customer support where multiple interactions occur simultaneously. By keeping conversations separate, you can provide a more efficient and effective service to each user.

## Summary and Preparation for Practice
In this lesson, you learned how to manage multiple chat sessions using OpenAI's API. We covered creating unique chat sessions, maintaining conversation history, and handling multiple interactions simultaneously. These skills are essential for building scalable chatbot applications that can handle numerous conversations at once. As you move on to the practice exercises, I encourage you to apply what you've learned by creating and managing chat sessions independently. This hands-on practice will reinforce your understanding and prepare you for more advanced chatbot development. Keep up the great work, and enjoy the journey of creating your chatbot with OpenAI!