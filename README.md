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
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |

### API Endpoints
GET a list of all FizzBuzz objects
Path:
Path Parameters: 
Response Content Type:
Example Response Body:
Response Status Codes:

GET a single FizzBuzz object by ID
Path:
Path Parameters: 
Response Content Type:
Example Response Body:
Response Status Codes:

POST a message to create a new FizzBuzz object
Path:
Path Parameters: 
Request Content Type:
Example Request Body:
Response Content Type:
Example Response Body:
Response Status Codes:
