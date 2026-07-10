import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")
if api_key == None:
    raise RuntimeError('Your API Key is null.')

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

def main():
    print("Hello from faregoai!")
    
    #This is how we get a user prompt. If you add --verbose as an argument, it provides additional information
    parser = argparse.ArgumentParser(description="FaregoAI Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    
    messages = [{"role": "user","content": args.user_prompt,}]
    response = client.chat.completions.create(model = 'openrouter/free', messages = messages)
    
    #Print all the things!
    if response.usage == None:
        raise RuntimeError('Failed API Request')
    else:
        if args.verbose:
            print(f'User prompt: {args.user_prompt}')
            print(f'Prompt tokens: {response.usage.prompt_tokens}')
            print(f'Response tokens: {response.usage.completion_tokens}')
        print(f'Response: {response.choices[0].message.content}')

if __name__ == "__main__":
    main()
