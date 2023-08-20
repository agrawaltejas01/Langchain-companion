from lib.config import Config 

import openai



print(Config.openAiApiKey)
openai.api_key = Config.openAiApiKey


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,         
    )
    return response.choices[0].message["content"]

def run_get_completion():
    userInput = input()

    if userInput == "-1":
        print("bye!")

    while userInput != "-1":
        response = get_completion(userInput)

        print("Response -> ")
        print(response)

        print("----------------------")
        print("Prompt ->")
        userInput = input()
