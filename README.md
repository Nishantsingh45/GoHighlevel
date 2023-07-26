# GoHighlevel
# Update Custom Field - Django View Function

## Description

This Django view function, `update_custom_field`, is designed to interact with the GoHighLevel API to update a custom field for a contact and provide the before and after values of the custom field in a REST API format.

## Functionality

1. The view function fetches a list of contacts using a GET request to the GoHighLevel API.
2. It selects the first contact from the list (you can modify this logic to choose a random contact).
3. The `contact_id` is extracted from the selected contact data.
4. The function then makes another GET request to the GoHighLevel API to fetch a list of custom fields.
5. It searches for a custom field with the name "DFS Booking Zoom Link" in the list of custom fields and extracts its `custom_field_id`.
6. If the custom field is not found, the function returns an error response with a status code of 404.
7. The view function makes a PUT request to the GoHighLevel API to update the custom field with the `custom_field_id` for the selected contact.
8. If the update is successful (status code 200), it makes another GET request to fetch the updated contact data.
9. The function prepares a JSON response containing the custom field values before and after the update.
10. The JSON response is returned as the API result, showing the before and after custom field values in a REST API format.

## Link for the video explaination
 - https://www.loom.com/share/b43e25b00bcf40479c2c2f9428c6b410?sid=1601d7d0-3fac-4a14-99fe-b75dc3b0af51

## Dependencies

- Django: The web framework used to develop the Django app.
- Requests: A Python library used to send HTTP requests to the GoHighLevel API.

## Note

- You may need to install the `requests` library if you haven't already. You can install it using pip:

```bash
pip install requests
