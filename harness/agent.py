import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

if(os.getenv("KIMI_API_KEY")):
    MODEL = "kimi-k2.6"
    client = OpenAI(api_key = os.getenv("KIMI_API_KEY"),
                    base_url = os.getenv("KIMI_BASE_URL"))

    EXTRA_BODY = {"thinking" : {"type" : "disabled"}}
else:
    MODEL = "gpt-4o-mini"
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """ You are a coding assistant running in the terminal and help the software engineers in building code.

You are precise and give pointed answers. You dont have access to any tools right now and if there is something you can'd do please say
so plainly.

Your code examples are given within proper code indents.
"""

def run():
    """RUn the agent's conversation loop until the user quits"""

    # The conversation history. This is the entire memory of the agent.
    # Every turn, we append to it and send the whole thing to the model.

    messages =  [{"role" : "system", "content" : SYSTEM_PROMPT}]

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

        print(f"\nagent> {assistant_message}\n")

if __name__ == "__main__":
    run()