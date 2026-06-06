from ollama import chat as ollama_chat
import pyttsx3

# Text to speech
engine = pyttsx3.init()

def say(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

# Chat history
chatStr = ""

def ai_chat(query):
    global chatStr

    try:
        # Add user message to history
        chatStr += f"Abhishek: {query}\n"

        # Send full history to model
        response = ollama_chat(
            model="qwen2.5:1.5b",
            messages=[
                {
                    "role": "system",
                    "content": "You are Jarvis, a helpful AI assistant."
                },
                {
                    "role": "user",
                    "content": chatStr
                }
            ]
        )

        reply = response["message"]["content"]

        # Add AI response to history
        chatStr += f"Jarvis: {reply}\n"

        say(reply)

        return reply

    except Exception as e:
        print("Jarvis error:", e)
        return None


# Test Loop
if __name__ == "__main__":

    while True:

        query = input("You: ")

        if query.lower() in ["exit", "quit", "stop"]:
            say("Goodbye Abhishek")
            break

        ai_chat(query)