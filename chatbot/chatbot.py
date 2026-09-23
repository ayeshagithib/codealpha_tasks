"""
Basic Rule-Based Chatbot
--------------------------
CodeAlpha Python Programming Internship - Task 4

Goal: A simple chatbot that responds to predefined user inputs using
if-elif logic. No AI/ML involved -- purely rule-based.

Key concepts used: if-elif, functions, loops, input/output.
"""

import random

# Each key maps to a list of possible replies, so the bot doesn't sound repetitive
RESPONSES = {
    "greeting": ["Hi!", "Hello there!", "Hey! How can I help you today?"],
    "how_are_you": ["I'm fine, thanks! How about you?", "Doing great, thanks for asking!"],
    "name": ["I'm a simple rule-based chatbot built for CodeAlpha!", "You can call me CodeBot."],
    "thanks": ["You're welcome!", "No problem at all!", "Anytime!"],
    "bye": ["Goodbye! Have a great day!", "See you later!", "Bye! Take care!"],
    "default": [
        "Sorry, I didn't understand that. Could you rephrase?",
        "I'm not sure how to respond to that yet.",
        "Hmm, I don't have an answer for that one.",
    ],
}

# Keywords mapped to which response category they trigger
KEYWORD_MAP = {
    "greeting": ["hello", "hi", "hey"],
    "how_are_you": ["how are you", "how're you", "how are u"],
    "name": ["your name", "who are you"],
    "thanks": ["thank", "thanks", "thx"],
    "bye": ["bye", "goodbye", "see you", "exit", "quit"],
}


def get_response(user_input):
    """
    Look at the user's input, check for known keywords, and return an
    appropriate reply from the RESPONSES dictionary.
    """
    text = user_input.lower().strip()

    for category, keywords in KEYWORD_MAP.items():
        for keyword in keywords:
            if keyword in text:
                return random.choice(RESPONSES[category]), category

    return random.choice(RESPONSES["default"]), "default"


def main():
    print("=" * 50)
    print("  CODEALPHA CHATBOT")
    print("  (type 'bye' or 'quit' to exit)")
    print("=" * 50)

    while True:
        user_input = input("\nYou: ").strip()

        if not user_input:
            print("Bot: Please type something!")
            continue

        reply, category = get_response(user_input)
        print(f"Bot: {reply}")

        if category == "bye":
            break


if __name__ == "__main__":
    main()
