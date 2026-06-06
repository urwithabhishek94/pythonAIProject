import datetime
import os
import speech_recognition as sr
import win32com.client
import webbrowser
from ollama import chat as ollama_chat
from openai import OpenAI
from dotenv import load_dotenv
import pywhatkit
import wikipedia
load_dotenv()

chatStr = ""

KNOWLEDGE_FILE = "./knowledge.json"

def ask_about_abhishek(question):

    with open("abhishek.txt", "r", encoding="utf-8") as file:
        context = file.read()

    response = ollama_chat(
        model="qwen2.5:1.5b",
        messages=[
            {
                "role": "system",
                "content":  """
                Answer only from the provided information.
                If the answer is not available, say:
                'I don't have that information.'
                """
            },
            {
                "role": "user",
                "content": f"""Information:{context} Question: {question}"""
            }
        ]
    )
    abhishek_response = response["message"]["content"]
    # return say(abhishek_response)
    return abhishek_response

def search_wikipedia(topic):
    try:
        result = wikipedia.summary(topic, sentences=3)
        return result

    except wikipedia.exceptions.DisambiguationError as e:
        return f"Multiple results found: {e.options[:5]}"

    except wikipedia.exceptions.PageError:
        return "No Wikipedia page found."

    except Exception as e:
        return f"Error: {e}"

def ai_chat(query):
    global chatStr

    try:
        # Add user message to history
        chatStr += f"Abhishek: {query}\n Jarvis:"

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
        chatStr += f"{reply}\n"
        say(reply)
        return reply

    except Exception as e:
        print("Jarvis error:", e)
        return None
# https://youtu.be/Z3ZAJoi4x6Q
def chat(query):
    global chatStr
    print(chatStr)
    try:
        chatStr += f"Abhishek: {query}\n Jarvis: "
        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("api_key")
        )

        completion = client.chat.completions.create(
            model="~openai/gpt-latest",
            messages=[
                {
                    "role": "user",
                    "content": chatStr
                }
            ],
            temperature=0.7,
            max_tokens=100,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        # todo: Wrap this inside of a  try catch block
        say(completion.choices[0].message.content)
        chatStr += f"{completion.choices[0].message.content}\n"
        return completion.choices[0].message.content
    except Exception as e:
        print("jarvis not working", e)

def ai(prompt):
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"
    try:
        response = ollama_chat(
            model="qwen2.5:1.5b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        # reply = response["message"]["content"]
        print(response["message"]["content"])
        text += response["message"]["content"]
        if not os.path.exists("Openai"):
            os.mkdir("Openai")

        # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
        with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
            f.write(text)
    except Exception as e:
        print("jarvis not working")
        return None
    # say(text.lower())


def say(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        r.pause_threshold = 1
        r.energy_threshold = 300
        # audio = r.listen(source)
        try:
            audio = r.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )
            print("Recognizing...")
            query =  r.recognize_google(audio, language='en-in')
            print(f" User said: {query}")
            return  query
        except sr.WaitTimeoutError:
            print("No speech detected.")
            return None

        except sr.UnknownValueError:
            print("Could not understand audio.")
            say("Could not understand you questions.")
            return None

        except Exception as e:
            print( "some error occured in take command")
            return None

if __name__ == '__main__':
    print('PyCharm')
    say("Hello i am Jarvis A.I")
    sites = {
        "youtube": "https://www.youtube.com",
        "google": "https://www.google.com",
        "wikipedia": "https://www.wikipedia.org"
    }
    while True:
        print("listening")
        query = takeCommand()
        if not query:
            continue
        query = query.lower()
        print("query", query)
        # Open websites
        site_opened = False
        for site_name, url in sites.items():
            # print(f"web"{}+{})
            if f"open {site_name}" in query.lower():
                say(f"opening {site_name} sir")
                webbrowser.open_new_tab(url)
                site_opened = True
                break
        if site_opened:
            continue

        elif "open chrome" in query:
            try:
                os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe" )
                say("Opening Chrome")
            except:
                say("Chrome not found.")

        elif "open music" in query:
            try:
                musicPath = r"C:\Users\Dell\Music\mirostar-romantic-song-song-531495.mp3"
                os.startfile(musicPath)
                say("Playing music")
            except:
                say("Music file not found.")

         # Time
        elif "what is the time" in query:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"The time is {current_time}")

        elif "stop jarvis" in query or "exit" in query:
            say("Goodbye sir")
            break

        elif "Using artificial intelligence" in query.lower():
            ai(prompt=query)

        elif "play youtube" in query:
            say("What should I play?")
            video = takeCommand()
            if video:
                pywhatkit.playonyt(video)

        elif "wikipedia" in query:
            topic = query.replace("wikipedia", "").strip()
            say(f"Searching Wikipedia for {topic}")
            result = search_wikipedia(topic)
            say(f" i have fetched this information from wikipedia.{result}")


        elif (
                "abhishek" in query
                or "jarvis" in query
                or "about yourself" in query
                or "who are you" in query
                or "tell me about yourself" in query
                or "tell me about sonali" in query
                or "who is sonali" in query

        ):
            answer = ask_about_abhishek(query)
            if answer:
                say(f"i have information like,  {answer} ")

        else:
            print("Chatting...")
            ai_chat(query)


        # say(query)

