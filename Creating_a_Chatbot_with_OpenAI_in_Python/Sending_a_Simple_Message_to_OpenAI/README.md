# Lesson 01 - Sending a Simple Message to OpenAI

What an exciting journey you're about to embark on! Creating chatbots with OpenAI is a stellar choice. Let's get started! 🚀

## Sending a Simple Message to OpenAI
Welcome to the first lesson of our course on creating a chatbot with OpenAI. In this lesson, we will explore the basics of interacting with OpenAI's API, which is a powerful tool for building chatbots. OpenAI provides advanced language models that can understand and generate human-like text, making it an excellent choice for chatbot development. Our goal in this lesson is to send a simple message to OpenAI's language model and receive a response. This foundational step will set the stage for more complex interactions in future lessons.

## Setting Up Your Environment
Before we can send a message to OpenAI, we need to set up our development environment. This involves installing the necessary tools and libraries. For this course, you will need the `openai` library, which allows us to interact with OpenAI's API.

To install this library, you can use the following command in your terminal:

```Bash
# Copy to clipboard
pip install openai
```
If you are using the CodeSignal platform, this library is pre-installed, so you can focus on writing and running your code without worrying about installation.

## Setting the OpenAI API Key as an Environment Variable
In this course, you'll be using the CodeSignal coding environment, where we've already set up everything you need to start working with OpenAI models. This means you don't need to worry about setting up an API key or configuring environment variables—it's all taken care of for you.

However, it's still useful to understand how this process works in case you want to set it up on your own computer in the future. To work with OpenAI models outside of CodeSignal, you need to set up a payment method and obtain an API key from their website. This API key is essential for accessing OpenAI's services and making requests to their API.

To keep your API key secure, you can use an environment variable. An environment variable is like a special note that your computer can read to find out important details, such as your OpenAI API key, without having to write it directly in your code. This helps keep your key safe and secure.

If you were setting this up on your own system, here's how you would do it:

On `macOS` and `Linux`, open your terminal and use the export command to set the environment variable:

```Bash
# Copy to clipboard
export OPENAI_API_KEY=your_api_key_here
```

For `Windows`, you can set the environment variable using the set command in the Command Prompt:

```Batch file (DOS)
set OPENAI_API_KEY=your_api_key_here
```

If you are using `PowerShell`, use the following command:

```PowerShell
# Copy to clipboard
$env:OPENAI_API_KEY="your_api_key_here"
```
These commands will set the environment variable for the current session. But remember, while using CodeSignal, you can skip these steps and jump straight into experimenting with OpenAI models.

## Initializing the OpenAI Client
Once the environment variable is set, you can initialize the OpenAI client in your script. This is done by importing the OpenAI class from the openai library and then creating an instance of it. The library will automatically identify your API key from the environment variable:

```Python
# Copy to clipboard
from openai import OpenAI
## Initialize the OpenAI client
client = OpenAI()
```
By initializing the client in this manner, you ensure that your script is ready to authenticate requests to OpenAI's API securely.

## Sending Your First Message to OpenAI
Now that your environment is set up and your API client is configured, it's time to send your first message to OpenAI. We'll start by defining a simple user prompt and then use the `chat.completions.create` method to send this message to the AI model.

Here's the code to accomplish this:

```Python
# Define a simple user message to test the API
prompt = "Hi, can you tell me a joke?"

# Create a chat completion request to get the AI response
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}]
)
```

In this code, we define a user prompt asking the AI to tell a joke. The chat.completions.create method of the OpenAI client is used to send a message to the AI model and receive a response. It takes some basic parameters to function:

- The `model` parameter specifies which AI model to use for generating the response. In this example, we use `"gpt-4"`, which is a version of OpenAI's language model known for its advanced text understanding and generation capabilities.

- The `messages` parameter is *a list of dictionaries* where each dictionary represents a message in the conversation. Each dictionary must include a `"role"`, which indicates the role of the message sender, such as `"user"` for the person interacting with the AI, and `"content"`, which contains the actual text of the message.

## Extracting and Displaying the AI's Reply
After sending the message to OpenAI, the next step is to extract the AI's reply from the API response and display it. Here's how you can do that:

```Python
# Extract the AI's response from the API result
reply = response.choices[0].message.content.strip()

# Show both sides of the conversation
print("Prompt:", prompt)
print("Response:", reply)
```
Once the `create` method is called, it returns a response object. To extract the AI's reply, you need to access the `choices` list from the response object, which contains possible responses generated by the AI. You then select the first choice with `choices[0]` and retrieve the message content using `message.content.strip()`, which removes any extra spaces or newlines.

Finally, we print both the prompt and the AI's reply to see the interaction. This helps verify that the message was successfully sent and received. When you run this code, you should see an output similar to the following:

```Plain text
Copy to clipboard
Prompt: Hi, can you tell me a joke?
```
Response: Why don't scientists trust atoms? Because they make up everything!
This output demonstrates a successful interaction with the AI, where it responds to the user's prompt with a joke.

## Example: Full Code Implementation
Let's look at the complete code example for sending a message to OpenAI. This example includes all the steps we've discussed so far:

```Python
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI()

# Define a simple user message to test the API
prompt = "Hi, can you tell me a joke?"

# Create a chat completion request to get the AI response
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}]
)

# Extract the AI's response from the API result
reply = response.choices[0].message.content.strip()

# Show both sides of the conversation
print("Prompt:", prompt)
print("Response:", reply)
```

## Summary and Next Steps
In this lesson, we covered the essential steps to send a simple message to OpenAI's language model. We set up our environment, configured API access, and sent a message to receive a response. This foundational knowledge is crucial as we move forward in building more complex chatbot interactions.

As you proceed to the practice exercises, I encourage you to experiment with different prompts and explore the AI's responses. This hands-on practice will reinforce what you've learned and prepare you for the next unit, where we'll delve deeper into handling API parameters. Keep up the great work, and enjoy the journey of creating your chatbot with OpenAI!