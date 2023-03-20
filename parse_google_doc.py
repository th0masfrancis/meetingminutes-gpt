import re
from google.oauth2 import service_account
from googleapiclient.discovery import build

def parse_google_doc(doc_link, credentials_file, max_words_per_token=2000):
    # Authenticate with the Google Docs API using a service account
    creds = service_account.Credentials.from_service_account_file(
        credentials_file,
        scopes=['https://www.googleapis.com/auth/documents.readonly']
    )
    docs_service = build('docs', 'v1', credentials=creds)

    # Retrieve the Google Doc content
    document = docs_service.documents().get(documentId=doc_link).execute()

    # Extract the text from the Google Doc
    doc_content = document.get('body').get('content')
    text = ""
    for elem in doc_content:
        if 'paragraph' in elem:
            for content in elem.get('paragraph').get('elements'):
                if 'textRun' in content:
                    text += content.get('textRun').get('content')

    # Split the text into tokens of maximum length max_words_per_token
    text_tokens = []
    while len(text) > max_words_per_token:
        # Find the last word boundary before max_words_per_token
        split_idx = re.search(r'\W', text[:max_words_per_token][::-1]).start()
        text_tokens.append(text[:max_words_per_token-split_idx].strip())
        text = text[max_words_per_token-split_idx:].strip()
    text_tokens.append(text.strip())

    return text_tokens
