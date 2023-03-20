import re
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.errors import HttpError



# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/documents.readonly']

def parse_google_doc(doc_link, credentials_file, max_words_per_token=1024):
    
    DOCUMENT_ID = doc_link
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credentials_file, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('docs', 'v1', credentials=creds)
        # Retrieve the documents contents from the Docs service.
        document = service.documents().get(documentId=DOCUMENT_ID).execute()

        print('The title of the document is: {}'.format(document.get('title')))
        
    except HttpError as err:
        print(err)
        


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
    
    print(len(text_tokens))

    return text_tokens
