"""
Simple Chatbot - A basic conversational chatbot implementation
"""

def main():
    print("Hello! I'm a simple chatbot. How can I help you today?")
    print("Type 'quit' to exit.")
    
    while True:
        user_input = input("\nYou: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        if not user_input:
            continue
        
        # Simple response logic 
        response = generate_response(user_input)
        print(f"Chatbot: {response}")


def generate_response(user_input):
    """
    Generate a response based on user input.
    Customize this function to make the chatbot smarter!
    """
    user_input_lower = user_input.lower()
    
    # Simple keyword matching
    if any(word in user_input_lower for word in ['hello', 'hi', 'hey']):
        return "Hello! Nice to meet you!"
    elif any(word in user_input_lower for word in ['how are you', 'how are you doing', 'how are you doing today']):
        return "I'm doing well, thank you for asking!"
    elif any(word in user_input_lower for word in ['name', 'who are you', 'what is your name']):
        return "I'm a simple chatbot created for practice!"
    elif '?' in user_input:
        return "That's an interesting question! I'm still learning."
    elif any(word in user_input_lower for word in ['thank you', 'thanks']):
        return "You're welcome!"
    else:
        return "That's interesting! Tell me more."


if __name__ == "__main__":
    main()
