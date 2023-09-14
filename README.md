# Person_api Project

This is a Django-based REST API project for managing persons. The API supports CRUD operations for person records.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Running the Project Locally](#running-the-project-locally)
- [API Documentation](#api-documentation)
  - [Endpoints](#endpoints)
  - [Request/Response Format](#requestresponse-format)
  - [Sample Usage](#sample-usage)
- [UML Diagrams](#uml-diagrams)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed
- Django and required dependencies installed (see [requirements.txt](requirements.txt))
- A database (SQLite) configured in your Django project settings

## Setup

1. Clone this repository to your local machine:
   git clone https://github.com/Paschal-ike/Person_api.git

2. Open a terminal or command prompt and navigate to the project directory.

3. Install the dependencies using the following command:
    pip install -r requirements.txt

4. Create and apply database migrations:
    python manage.py makemigrations
    python manage.py migrate

## Running the Project Locally
- python manage.py runserver

## API Documentation
    - Endpoints
        /api/: Creates a new person.
        /api/<int:person_id>: Retrieves, updates, or deletes a person.

    - Request/Response Format
    
## create person:
POST /api HTTP/1.1
Content-Type: application/json

{
  "name": "Person Name"
}

HTTP/1.1 201 Created
Content-Type: application/json

{
  "message": "Person created successfully"
}

## Get person:
GET /api/1 HTTP/1.1
Accept: application/json

HTTP/1.1 200 OK
Content-Type: application/json

{
  "person": {
    "id": 1,
    "name": "Person Name"
  }
}

## Update Person
PUT /api/1 HTTP/1.1
Content-Type: application/json

{
  "name": "Updated Name"
}

HTTP/1.1 200 OK
Content-Type: application/json

{
  "message": "Person updated successfully"
}

## Delete Person
DELETE /api/persons/1 HTTP/1.1

HTTP/1.1 204 No Content


## Sample Usage

- To create a new person, you can send a POST request to the /api endpoint with the person's name in the request body.

- To get a person, you can send a GET request to the /api/<int:person_id> endpoint, where <int:person_id> is the ID of the person.

- To update a person, you can send a PUT request to the /api/<int:person_id> endpoint with the person's updated information in the request body.

- To delete a person, you can send a DELETE request to the /api/<int:person_id> endpoint.
