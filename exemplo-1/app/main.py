from openai import OpenAI

client = OpenAI()
model = "gpt-3.5-turbo"
response = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "system", "content": "Nesse momento você é um especialista em programacao java. Nao envie texto apenas necessito do codigo 'code'"},
        {"role": "user", "content": "poderia me criar uma classe com um metodo para calcular um fatorial ?"},
    ],
)
print(response)