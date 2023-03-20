from parse_google_doc import parse_google_doc
from summarise_with_gpt import summarise_with_gpt

# Enter the Google Doc link here
doc_link = "https://docs.google.com/document/d/16BOwSn412GhlYEzpBxh_plbRhYXMpMtAGFCsKaWmVDM/edit?usp=sharing"

# Enter the path to your service account credentials JSON file here
credentials_file = "credentials.json" #rename samplecredentials file


def main():
     # Call the parse_google_doc() function to retrieve the text tokens
    text_tokens = parse_google_doc(doc_link, credentials_file)

    # Print the text tokens
    for i, token in enumerate(text_tokens):
        print(f"Token {i+1}: {token}")
    
    summarise_with_gpt(text_tokens)
        

if __name__ == "__main__":
    main()