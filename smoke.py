from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model = "gpt-4o-mini",
    messages = [{"role" : "user" , "content" : "Say 'setup works' and nothing else."}],
)

print(response.choices[0].message.content)