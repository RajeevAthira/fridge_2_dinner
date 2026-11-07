from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()  # loads ANTHROPIC_API_KEY from .env

client = Anthropic() # picks up the key automatically

response = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=500,
    messages=[
        {
            "role": "user",
            "content": "Suggest a dinner using eggs, spinach and rice."
        }
    ]
    
)
print(response.content[0].text)
print("Tokens:", response.usage.input_tokens, "in /", response.usage.output_tokens, "out")