import nltk
import random
import re

# Download required NLTK resources
nltk.download('punkt')


# Define patterns and responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey! How can I help you?"],
    "hi": ["Hello!", "Hi!", "Hey! What's up?"],
    "how are you": ["I'm just a bot, but I'm doing great!", "I'm good, thanks! How about you?"],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "default": ["I'm not sure I understand that. Can you rephrase?"]
}

def preprocess_text(text):
    return nltk.word_tokenize(text.lower()) #Lowercase and tokenize input text

def get_response(user_input):
    """Match user input with predefined patterns and return a response."""
    user_input = preprocess_text(user_input)
    user_input_token = " ".join(user_input)  # Join tokens back into a sentence

    # Rule-based pattern matching
    for pattern, replies in responses.items():
        if re.search(rf'\b{pattern}\b', user_input_token):
            return random.choice(replies)
    
    return random.choice(responses["default"])

# Main chatbot loop
def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")

# Run the chatbot
chatbot()
