# crm_integration/views.py

import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
import random


@api_view(['GET'])
def update_custom_field(request):
    # Replace <token> with your actual API token
    headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2NhdGlvbl9pZCI6IkpOVEpTV04ya0tkRVZkMElFbEZhIiwiY29tcGFueV9pZCI6ImJmb1Q3MkNWcm9oMlg4ZWZPUmdRIiwidmVyc2lvbiI6MSwiaWF0IjoxNjYxNDE2NzQzNTcxLCJzdWIiOiJQcVJEWDZqMjdXempXRUNsQm92eCJ9.u6WPtyudfB9R4nLnLbBZ6i9KquDeK6WnIOZxKAeE9Hg'
    }

    # Fetch the contacts API to get a random contact ID
    contacts_url = "https://rest.gohighlevel.com/v1/contacts"
    contacts_response = requests.get(contacts_url, headers=headers)

    if contacts_response.status_code != 200:
        return Response({'error': f'Failed to fetch contacts API. Status code: {contacts_response.status_code}'}, status=contacts_response.status_code)

    contacts_data = contacts_response.json()
    contacts_list = contacts_data.get('contacts', [])
    if not contacts_list:
        return Response({'error': 'No contacts found.'}, status=404)

    random_contact = contacts_list[0]  # Take the first contact as a random contact
    contact_id = random_contact['id']

    # Fetch the custom fields API to find the custom field ID for "DFS Booking Zoom Link"
    custom_fields_url = "https://rest.gohighlevel.com/v1/custom-fields"
    custom_fields_response = requests.get(custom_fields_url, headers=headers)

    if custom_fields_response.status_code != 200:
        return Response({'error': f'Failed to fetch custom fields API. Status code: {custom_fields_response.status_code}'}, status=custom_fields_response.status_code)

    custom_fields_data = custom_fields_response.json()
    custom_fields_list = custom_fields_data.get('customFields', [])
    if not custom_fields_list:
        return Response({'error': 'No custom fields found.'}, status=404)

    custom_field_id = None
    for custom_field in custom_fields_list:
        if custom_field['name'] == 'DFS Booking Zoom Link':
            custom_field_id = custom_field['id']
            break

    if not custom_field_id:
        return Response({'error': 'Custom field "DFS Booking Zoom Link" not found.'}, status=404)

    # Update the custom field with the given custom field ID for the random contact
    update_url = f"https://rest.gohighlevel.com/v1/contacts/{contact_id}"
    payload={}
    headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2NhdGlvbl9pZCI6IkpOVEpTV04ya0tkRVZkMElFbEZhIiwiY29tcGFueV9pZCI6ImJmb1Q3MkNWcm9oMlg4ZWZPUmdRIiwidmVyc2lvbiI6MSwiaWF0IjoxNjYxNDE2NzQzNTcxLCJzdWIiOiJQcVJEWDZqMjdXempXRUNsQm92eCJ9.u6WPtyudfB9R4nLnLbBZ6i9KquDeK6WnIOZxKAeE9Hg'
    }

    before_response = requests.request("GET", update_url, headers=headers, data=payload)
    before_response =before_response.json()
    before_response=before_response["contact"]["customField"]



    payload = {
        "customField": {
            custom_field_id: "TEST"
        }
    }

    update_response = requests.put(update_url, headers=headers, json=payload)

    if update_response.status_code == 200:
        data =update_response.json()
        data=data["contact"]["customField"]
        return Response({'before': before_response, 'After': data})
    else:
        return Response({'error': f'Failed to update custom field. Status code: {update_response.status_code}'}, status=update_response.status_code)

@api_view(['GET'])
def get_contacts(request):

    url = "https://rest.gohighlevel.com/v1/contacts"

    payload={}
    headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2NhdGlvbl9pZCI6IkpOVEpTV04ya0tkRVZkMElFbEZhIiwiY29tcGFueV9pZCI6ImJmb1Q3MkNWcm9oMlg4ZWZPUmdRIiwidmVyc2lvbiI6MSwiaWF0IjoxNjYxNDE2NzQzNTcxLCJzdWIiOiJQcVJEWDZqMjdXempXRUNsQm92eCJ9.u6WPtyudfB9R4nLnLbBZ6i9KquDeK6WnIOZxKAeE9Hg'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    data =response.json()

    return  Response(data)
