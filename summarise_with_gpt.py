import openai
import os

def summarise_with_gpt(text_tokens):
    # Set up the OpenAI API credentials
    openai.api_key = os.environ["OPENAI_API_KEY"]

    # Set up the GPT-3 API parameters
    model_engine = "text-davinci-002"
    max_tokens = 1024
    stop_sequence = "\n"

    # Send each text token as a prompt to the GPT-3 API and print the response
    for i, token in enumerate(text_tokens):
        prompt = token + "\n\n"
        response = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=max_tokens,
            stop=stop_sequence
        )
        print(f"Response {i+1}: {response.choices[0].text.strip()}\n")
