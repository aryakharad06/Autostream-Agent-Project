# Autostream-Agent-Project
AutoStream is a Conversational AI Agent for a SaaS video editing platform. It identifies user intent, answers pricing and product queries using RAG, detects high-intent users, collects lead details like name, email, and platform, and triggers mock lead capture using Python-based agent workflow automation.
# AutoStream – Social-to-Lead Agentic Workflow

## Project Structure

```text
autostream-agent/
│
├── app.py
├── knowledge_base.json
├── requirements.txt
└── README.md
```

---

# app.py

```python
import json

# -----------------------------
# Load Local Knowledge Base (RAG)
# -----------------------------
def load_knowledge_base():
    with open("knowledge_base.json", "r") as file:
        return json.load(file)

kb = load_knowledge_base()


# -----------------------------
# Mock Tool Function
# -----------------------------
def mock_lead_capture(name, email, platform):
    print(f"\nLead captured successfully: {name}, {email}, {platform}")


# -----------------------------
# Intent Detection
# -----------------------------
def detect_intent(user_input):
    text = user_input.lower()

    greetings = ["hi", "hello", "hey"]
    pricing_words = ["price", "pricing", "plan", "cost", "features"]
    high_intent_words = ["sign up", "buy", "purchase", "try", "subscribe", "pro plan"]

    if any(word in text for word in greetings):
        return "greeting"

    if any(word in text for word in high_intent_words):
        return "high_intent"

    if any(word in text for word in pricing_words):
        return "product_query"

    return "general"


# -----------------------------
# RAG Response
# -----------------------------
def answer_product_query():
    pricing = kb["pricing"]
    policies = kb["policies"]

    response = "\nAutoStream Pricing & Features:\n"
    response += f"\nBasic Plan: ${pricing['Basic Plan']['price']}/month"
    response += f"\n- {pricing['Basic Plan']['videos']}"
    response += f"\n- {pricing['Basic Plan']['resolution']}"

    response += f"\n\nPro Plan: ${pricing['Pro Plan']['price']}/month"
    response += f"\n- {pricing['Pro Plan']['videos']}"
    response += f"\n- {pricing['Pro Plan']['resolution']}"
    response += f"\n- {pricing['Pro Plan']['feature']}"

    response += f"\n\nPolicy: {policies['refund']}"
    response += f"\nSupport: {policies['support']}\n"

    return response


# -----------------------------
# Main Agent Workflow
# -----------------------------
def main():
    print("=== AutoStream Conversational AI Agent ===")

    lead_data = {
        "name": None,
        "email": None,
        "platform": None
    }

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() == "exit":
            print("Agent: Thank you! Exiting...")
            break

        intent = detect_intent(user_input)

        if intent == "greeting":
            print("Agent: Hello! Welcome to AutoStream. How can I help you today?")

        elif intent == "product_query":
            print(answer_product_query())

        elif intent == "high_intent":
            print("Agent: Great! I'd love to help you get started with AutoStream Pro Plan.")

            if not lead_data["name"]:
                lead_data["name"] = input("Agent: Please enter your Name: ")

            if not lead_data["email"]:
                lead_data["email"] = input("Agent: Please enter your Email: ")

            if not lead_data["platform"]:
                lead_data["platform"] = input("Agent: Which creator platform do you use? (YouTube/Instagram/etc.): ")

            if all(lead_data.values()):
                mock_lead_capture(
                    lead_data["name"],
                    lead_data["email"],
                    lead_data["platform"]
                )
                print("Agent: Thank you! Our team will contact you shortly.")

        else:
            print("Agent: Could you please clarify your requirement?")


if __name__ == "__main__":
    main()
```

---

# knowledge_base.json

```json
{
  "pricing": {
    "Basic Plan": {
      "price": 29,
      "videos": "10 videos/month",
      "resolution": "720p resolution"
    },
    "Pro Plan": {
      "price": 79,
      "videos": "Unlimited videos",
      "resolution": "4K resolution",
      "feature": "AI captions"
    }
  },
  "policies": {
    "refund": "No refunds after 7 days",
    "support": "24/7 support available only on Pro plan"
  }
}
```

---

# requirements.txt

```txt
langchain
langgraph
openai
python-dotenv
```

---

# README.md

````md
# AutoStream – Social-to-Lead Agentic Workflow

## How to Run

1. Install dependencies
```bash
pip install -r requirements.txt
````

2. Run the project

```bash
python app.py
```

3. Type user queries like:

* Hi, tell me about your pricing
* I want to try the Pro plan for my YouTube channel

Type `exit` to stop.

---

## Architecture Explanation

This project uses Python with a simple agentic workflow inspired by LangGraph state management. The agent detects user intent, performs local knowledge retrieval using a JSON-based RAG system, and executes lead capture only after collecting all required user details.

LangGraph is preferred because it provides strong state control for multi-step conversations. In this implementation, state is handled using a Python dictionary (`lead_data`) that stores user details across multiple turns. This ensures the tool is triggered only after collecting name, email, and creator platform.

The RAG pipeline uses a local JSON knowledge base containing pricing, features, and company policies. When the user asks product-related questions, the agent retrieves the relevant data and responds accurately.

This architecture ensures clean separation between intent detection, retrieval, memory, and tool execution, making it suitable for real-world SaaS deployment.

---

## WhatsApp Deployment Using Webhooks

To deploy this agent on WhatsApp, we can use the WhatsApp Business API with webhook integration.

1. User sends a message on WhatsApp
2. Webhook receives the message on our backend server
3. The backend sends the message to our AI agent
4. The agent processes intent and response
5. The backend sends the reply back to WhatsApp using the API

This allows real-time customer interaction, lead qualification, and CRM integration for business automation.

```
```
