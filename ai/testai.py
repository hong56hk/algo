import openai

API_KEY = ''

client = openai.OpenAI(api_key=API_KEY)

# models = client.models.list()

# for model in models.data:
#   print(model.id)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, ChatGPT!"}
    ]
)

print(response.choices[0].message.content)
