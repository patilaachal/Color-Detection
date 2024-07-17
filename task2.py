import random

# Dictionary containing some sample responses
responses = {
    "hello": "Hello! How can I help you?",
    "how are you": "I'm good, thank you for asking.",
    "bye": "Goodbye! Take care.",
    "default": "I'm sorry, I didn't understand that.",
}

# Function to generate responses
def respond(message):
    # Convert the message to lowercase
    message = message.lower()
    
    # Check if the message is in the responses
    if message in responses:
        return responses[message]
    else:
        return responses["default"]

# Main function to run the chatbot
def main():
    print("Welcome to the chatbot!")
    print("You can start chatting with the bot. Type 'bye' to exit.")
    
    while True:
        # Get user input
        user_input = input("You: ")
        
        # Exit the loop if user says 'bye'
        if user_input.lower() == 'bye':
            print(responses["bye"])
            break
        
        # Generate and print response
        response = respond(user_input)
        print("Bot:", response)

# Run the main function
if _name_ == "_main_":
    main()