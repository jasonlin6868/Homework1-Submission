from openai import OpenAI

# Create a client that points to Ollama's local API endpoint
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"  # required param, but unused
)

response = client.chat.completions.create(
    model="llama2",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello! Who won the world series in 2020?"}
    ]
)

print(response.choices[0].message.content)
