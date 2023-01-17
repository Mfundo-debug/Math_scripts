from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Set up the API client
service = build('forms', 'v1', credentials=credentials)

# Define the form and form item IDs
form_id = 'YOUR_FORM_ID'
form_item_id = 'YOUR_FORM_ITEM_ID'

# Define the form response
form_response = {
    'formItemId': form_item_id,
    'formResponse': {
        'response': {
            'email': 'parent@example.com',
            'name': 'Parent',
            'childName': 'Child'
        }
    }
}

# Submit the form response
try:
    response = service.forms().createResponse(formId=form_id, body=form_response).execute()
    print(f'Successfully submitted form response with ID: {response["responseId"]}')
except HttpError as error:
    print(f'An error occurred: {error}')
