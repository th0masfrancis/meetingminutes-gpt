import openai
import os

def summarise_with_gpt(text_tokens,openai_api_key):
    # Set up the OpenAI API credentials
    openai.api_key = openai_api_key

    # Set up the GPT-3 API parameters
    model_engine = "text-davinci-003"
    max_tokens = 1024 #What is the funtion of this variable
    stop_sequence = "\n"

    # Send each text token as a prompt to the GPT-3 API and print the response
    summary_response =[]
    for i, token in enumerate(text_tokens):
       prompt = "Summarise following meeting transcript: " + token + "\n\n"
       print (prompt)
       try:
            response = openai.Completion.create(
                engine=model_engine,
                prompt=prompt,
                max_tokens=max_tokens,
                stop=stop_sequence
            )
            # Some of the responses are empty.
            # TODO retry if response.choices[0].text.strip() is null
            
            summary_response.append(response.choices[0].text.strip())
       except Exception as e:
            print(f"Error occurred while processing token {i}: {e}")
            summary_response.append("ERROR - CHATGPT TIME")
    
    return summary_response
        
