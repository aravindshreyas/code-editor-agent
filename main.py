import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types
from functions.get_files_info import get_files_info

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    #print("API Key:", api_key)

    client = genai.Client(api_key=api_key)
    if len(sys.argv)>1:
        user_prompt = sys.argv[1]
    if len(sys.argv) == 1:
        print('No prompt provided.')
        sys.exit(1)
    verbose_flag=False
    if len(sys.argv) == 3 and sys.argv[2]=='--verbose':
        verbose_flag=True
   
   
    messages = [
        types.Content(
            role="user",
            parts=[types.Part(
                text=user_prompt
            )]
        )
    ]

    response = client.models.generate_content(

        model='gemini-2.0-flash-001',contents=user_prompt
    
    )

    
    if response.text is None:
        print("No text returned in the response.")
        return
    
    
    print(response.text)

    if verbose_flag:
        print(f'Prompt Tokens: {response.usage_metadata.prompt_token_count}')
        print(f'Response Tokens: {response.usage_metadata.candidates_token_count}')

print(get_files_info("calculator","pkg"))
#main()
