# FizzBuzz - Django Rest Framework API

## Getting Started
Create and activate a virtual environment \
`python3 -m venv venv` \
`source env/bin/activate`

Install packages and dependencies \
`pip install -r requirements.txt`

Change directory to project and sync database \
`cd drf_api` \
`python manage.py migrate`

Run dev server \
`python manage.py runserver`

## Testing
Use the Browsable API to test the API endpoints in the browser:
- GET a list of all FizzBuzz objects or POST to create a new FizzBuzz at `http://127.0.0.1:8000/fizzbuzz/`
- GET a specific FizzBuzz object by fizzbuzz_id at `http://127.0.0.1:8000/fizzbuzz/<fizzbuzz_id>/`

Run a suite of unit tests via the CLI with the following command: \
`python manage.py test`

## Documentation
### FizzBuzz Properties
| Key | Date Type | Description |
| ----------- | ----------- | ----------- |
| fizzbuzz_id | char(36) | String representation of ID number. Incremented for each new FizzBuzz and assigned by server at creation. |
| creation_date | datetime(6) | Representation of the UTC time at FizzBuzz creation. |
| useragent | char(200) | String representation of the HTTP User-Agent header value for the browser request sent to create the FizzBuzz. |
| message | text | String representation of the message sent in the request body to create the FizzBuzz. |

### API Endpoints
GET a list of all FizzBuzz objects \
Path: `http://127.0.0.1:8000/fizzbuzz/` \
Path Parameters: None \
Response Content-Type: application/json \
Example Response Body:
```
```
Response Status Codes:
- 200 OK - Success! A list of all FizzBuzz objects was returned.

GET a single FizzBuzz object by ID \
Path: `http://127.0.0.1:8000/fizzbuzz/<fizzbuzz_id>/` \
Path Parameters: fizzbuzz_id \
Response Content-Type: application/json \
Example Response Body:
```
```
Response Status Codes:
- 200 OK - Success! The FizzBuzz object with a matching fizzbuzz_id was returned.
- 404 Not Found - This FizzBuzz could not be located and likely doesn't exist.

POST a message to create a new FizzBuzz object \
Path: `http://127.0.0.1:8000/fizzbuzz/` \
Path Parameters: None \
Request Content-Type: application/json \
Example Request Body:
```
```
Response Content-Type: application/json \
Example Response Body:
```
```
Response Status Codes:
- 201 Created - Success! A new FizzBuzz object was created and returned.
- 400 Bad Request - The request body or headers did not contain the required information or the request body contained additional fields that are not allowed. Only the "message" field is allowed in a POST request body. The request must have a User-Agent header value.
- 500 Internal Server Error - The request was properly formed, but the server failed to create a new FizzBuzz.

