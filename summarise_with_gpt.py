import openai
import os

def summarise_with_gpt(text_tokens,openai_api_key):
    # Set up the OpenAI API credentials
    openai.api_key = openai_api_key
    
    # Initialize the conversation history with a message from the chatbot
    message_log = [
        {"role": "system", "content": "You are a helpful business assistant."}
    ]
    
    # Set a flag to keep track of whether this is the first request in the conversation
    first_request = True

    # Set up the GPT-3.5 API parameters
    model_engine = "gpt-3.5-turbo"
    max_tokens = 800 # The maximum number of tokens (words or subwords) in the generated response
    stop_sequence = None

    # Send each text token as a prompt to the GPT-3 API and print the response
    summary_response =[]
    for i, token in enumerate(text_tokens):
        print (i)
        if first_request:
            message_log.append({"role": "user", "content": "Can you summarise following meeting transcript"+ token})
            # Set the flag to False so that this branch is not executed again
            first_request = False
        else:
            message_log.append({"role": "user", "content": token})
            try:
                    response = openai.ChatCompletion.create(
                        model=model_engine,
                        messages=message_log,
                        max_tokens=max_tokens,
                        stop=stop_sequence,
                        temperature=0.7,
                    )
                    summary_response.append(response['choices'][0]['message']['content'])
                    # Some of the responses are empty.
                    # Find the first response from the chatbot that has text in it (some responses may not have text)
                    
                    # Add the chatbot's response to the conversation history and print it to the console
                    message_log.append({"role": "assistant", "content": response['choices'][0]['message']['content']})
            
            
            except Exception as e:
                    print(f"Error occurred while processing token {i}: {e}")
                    summary_response.append("ERROR - CHATGPT ERROR")
            
    return summary_response
        
