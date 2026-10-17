import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

MODEL = "gpt-4o-mini"

client = OpenAI()

def run():
    """RUn the agent's conversation lopp until the user quites"""

    # The conversation history. This is the entire memory of the agent.
    # Every turn, we append to it and send the whole thing to the model.

    messages =  []

    print("Agent ready. Type 'quit' or 'exit' to leave. /n")

    while True:

        # Get input from the user

        user_input = input("you>").strip()

        if user_input in {"quit" , "exit" }:
            print("Goodbye.")
            break

        if not user_input:
            continue

        messages.append({"role" : "user" ,
                          "content" : user_input })

        response = client.chat.completions.create(
            model = MODEL,
            messages = messages,
        )

        assistant_message = response.choices[0].message.content
        messages.append({"role" : "assistant", "content" : assistant_message})

        print(f"/nagent> {assistant_message}/n")

if __name__ == "__main__":
    run()