import openai
import os
from transformers import pipeline

def summarise_with_gpt3(text_tokens):
    # Set up the OpenAI API credentials
    openai.api_key = os.environ["OPENAI_API_KEY"]

    # Set up the GPT-3 API parameters
    model_engine = "text-davinci-002"
    max_tokens = 1024
    stop_sequence = "\n"

    # Initialize the summarization pipeline
    summarization_pipeline = pipeline(
        task="summarization",
        model="t5-small",
        tokenizer="t5-small",
        framework="pt"
    )

    # Send each text token as a prompt to the GPT-3 API and print the summary
    for i, token in enumerate(text_tokens):
        prompt = token + "\n\n"
        response = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=max_tokens,
            stop=stop_sequence
        )
        summary = summarization_pipeline(response.choices[0].text.strip(), max_length=100, min_length=30, do_sample=False)
        print(f"Token {i+1} summary: {summary[0]['summary_text'].strip()}\n")
