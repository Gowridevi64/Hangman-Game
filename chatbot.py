
import re
import json

# Business information
BUSINESS_NAME = "ABC Customer Support"
BUSINESS_HOURS = "Monday to Saturday, 9:00 AM to 6:00 PM"

# Rule-based responses
INTENTS = {
    "greeting": {
        "patterns": [r"\bhi\b", r"\bhello\b", r"\bhey\b", r"\bgood morning\b"],
        "responses": [
            f"Hello! Welcome to {BUSINESS_NAME}. How can I help you?"
        ]
    },
    "hours": {
        "patterns": [
            r"\bhours?\b", r"\bopen\b", r"\bclose\b",
            r"\bworking time\b", r"\bwhen.*available\b"
        ],
        "responses": [
            f"Our business hours are {BUSINESS_HOURS}."
        ]
    },
    "price": {
        "patterns": [
            r"\bprice\b", r"\bcost\b", r"\bpricing\b",
            r"\bhow much\b"
        ],
        "responses": [
            "Our product prices depend on the item. Please tell me which product you are interested in."
        ]
    },
    "payment": {
        "patterns": [
            r"\bpayment\b", r"\bpay\b", r"\bupi\b",
            r"\bcredit card\b", r"\bdebit card\b"
        ],
        "responses": [
            "We support online payment options. Please check the available payment methods at checkout."
        ]
    },
    "delivery": {
        "patterns": [
            r"\bdelivery\b", r"\bshipping\b",
            r"\btrack.*order\b", r"\border status\b"
        ],
        "responses": [
            "For delivery updates, please check your order details or contact our support team."
        ]
    },
    "returns": {
        "patterns": [
            r"\breturn\b", r"\brefund\b",
            r"\breplacement\b", r"\bexchange\b"
        ],
        "responses": [
            "For returns or refunds, please check the product's return policy or contact customer support."
        ]
    },
    "thanks": {
        "patterns": [
            r"\bthanks?\b", r"\bthank you\b", r"\bappreciate it\b"
        ],
        "responses": [
            "You're welcome! Is there anything else I can help you with?"
        ]
    },
    "goodbye": {
        "patterns": [
            r"\bbye\b", r"\bgoodbye\b", r"\bsee you\b"
        ],
        "responses": [
            "Thank you for chatting with us. Have a great day!"
        ]
    }
}

FALLBACK = (
    "Sorry, I couldn't understand your question. "
    "You can ask about business hours, product prices, "
    "payments, delivery, or returns."
)


def normalize_input(text):
    """Normalize user input."""
    return re.sub(r"\s+", " ", text.strip().lower())


def load_faq(filename="faq.json"):
    """Load additional FAQ data if the JSON file exists."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, dict) else {}
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("Warning: FAQ JSON is invalid. Using built-in responses.")
        return {}
    except OSError:
        print("Warning: Could not read FAQ file. Using built-in responses.")
        return {}


def find_intents(message):
    """Identify all matching intents in a message."""
    matched = []

    for intent, details in INTENTS.items():
        if any(re.search(pattern, message) for pattern in details["patterns"]):
            matched.append(intent)

    return matched


def get_response(message, faq):
    """Generate responses for matching intents."""
    message = normalize_input(message)

    if not message:
        return "Please enter a question so I can help you."

    # Handle clean exit commands as complete words.
    if re.fullmatch(r"(bye|exit|quit)", message):
        return None

    matched_intents = find_intents(message)
    responses = []

    for intent in matched_intents:
        response = INTENTS[intent]["responses"][0]

        if response not in responses:
            responses.append(response)

    # Check additional FAQs from JSON.
    for question, answer in faq.items():
        if not isinstance(question, str) or not isinstance(answer, str):
            continue

        keywords = re.findall(r"\b[a-z0-9]+\b", question.lower())
        if keywords and all(
            re.search(r"\b" + re.escape(word) + r"\b", message)
            for word in keywords
        ):
            if answer not in responses:
                responses.append(answer)

    if responses:
        return "\n".join(responses)

    return FALLBACK


def main():
    """Run the interactive chatbot."""
    faq = load_faq()

    print("=" * 45)
    print(f"Welcome to {BUSINESS_NAME}!")
    print("Type 'bye', 'exit', or 'quit' to leave.")
    print("=" * 45)

    while True:
        try:
            user_input = input("\nYou: ")
            normalized = normalize_input(user_input)

            if normalized in {"bye", "exit", "quit"}:
                print("Bot: Thank you for chatting with us. Goodbye!")
                break

            response = get_response(user_input, faq)

            if response is None:
                print("Bot: Goodbye!")
                break

            print(f"Bot: {response}")

        except (EOFError, KeyboardInterrupt):
            print("\nBot: Chat ended. Goodbye!")
            break
        except Exception as error:
            print("Bot: Sorry, something went wrong. Please try again.")


if __name__ == "__main__":
    main()
