from parse_google_doc import parse_google_doc
from summarise_with_gpt import summarise_with_gpt
from dotenv import load_dotenv
import os
# Load environment variables from .env file
load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
doc_link = os.getenv('DOC_LINK')

# Enter the path to your service account credentials JSON file here
credentials_file = 'credentials.json'

def main():
    # Call the parse_google_doc() function to retrieve the text tokens
    
    text_tokens = parse_google_doc(doc_link, credentials_file,max_words_per_token=512)
    summary = summarise_with_gpt(text_tokens,openai_api_key)
    
    print (summary)
        

if __name__ == "__main__":
    main()