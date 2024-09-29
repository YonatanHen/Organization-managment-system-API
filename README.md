# Overview
This organization management system is a web application designed to facilitate the management of organizations, users, and endpoints within a streamlined framework. This application aims to provide an intuitive and efficient interface for managing organizational resources, making it easier for IT administrators to interact with the data they need.

### ERD:
![image](https://github.com/user-attachments/assets/92febd11-5f29-4ba8-8785-4a0d4486988c)

## Tech Stack
- Python v3.12.5
- Flask
- SQLAlchemy
- PostgreSQL DB
- Docker
- unittest

** Tasks were managed in a GitHub [Project](https://github.com/users/YonatanHen/projects/4) associated with this repository.

## Installation & Setup Instructions
Installation and setup scripts were created under the `shell` folder in this project.

### Create The Virtual Environment
First, create a .env file with the following content:

```plaintext
ENVIRONMENT='PRODUCTION'
PSQL_USERNAME=<PSQL production DB connection username>
PSQL_PASSWORD=<PSQL production DB connection password>
PSQL_URL=<PSQL production DB connection URL>
```

For example (based on the credentials and URL in the `db_setup.sh`): 
```plaintext
PSQL_USERNAME='postgres'
PSQL_PASSWORD='password'
PSQL_URL='localhost:5432/postgres'
```

Run the `shell/create_venv.sh` shell script to create a virtual environment called task-env, and install the application's dependencies listed in the `requirements.txt` file:
```plaintext
blinker==1.8.2
click==8.1.7
colorama==0.4.6
Flask==3.0.3
greenlet==3.1.1
itsdangerous==2.2.0
Jinja2==3.1.4
MarkupSafe==2.1.5
psycopg2==2.9.9
python-dotenv==1.0.1
SQLAlchemy==2.0.35
typing_extensions==4.12.2
Werkzeug==3.0.4
```

### DB Setup
Please make sure the Docker Desktop is running, then run the `shell/db_setup.sh` shell script to create a Docker volume and a container running PSQL DB, exposed to port `5432` (change the credentials and URL in case they are different from those described in the example above).

### Rerun Virtual Environment and DB
Simply run the `shell/start_venv.sh` script.

### Run Server
Simply run the `shell/start.sh` script which runs the Flask API server on localhost, port `5000`.

# API Documentation
#### Base URL
`http://localhost:5000`

| API Name                             | Method  | Endpoint                                 | Payload                                               | Response                                               | Description                                   |
|--------------------------------------|---------|------------------------------------------|------------------------------------------------------|--------------------------------------------------------|-----------------------------------------------|
| Add User                             | POST    | `/user/`                                 | `{"name": <string>, "ep_id": <int>}`         | `{"message": "User added successfully", "user": {"id": user.id, "name": user.name, "endpoint_id": user.endpoint_id, "organization_id": endpoint.organization_id}}` | Create a new user.                           |
| Update User                          | PUT     | `/user/<user_id>`                       | `{"name": <string>\|"ep_id": <int>}`         | `{"message": "User updated successfully", "user": {"id": user.id, "name": user.name, "endpoint_id": user.endpoint_id, "organization_id": endpoint.organization_id}}` | Update an existing user by user ID.         |
| Delete User                          | DELETE  | `/user/<user_id>`                       | N/A                                                  | `{"message": "User deleted successfully", "user": {"id": user.id, "name": user.name, "endpoint_id": user.endpoint_id, "organization_id": endpoint.organization_id}}` | Delete a user by user ID.                   |
| Get User's Endpoint                  | GET     | `/user/<user_id>/endpoint`              | N/A                                                  | `{"id": endpoint.id, "name": endpoint.name, "organization_id": endpoint.organization_id}` | Retrieve the endpoint associated with a user.|
| Get User's Organization               | GET     | `/user/<user_id>/organization`          | N/A                                                  | `{"id": organization.id, "name": organization.name}` | Retrieve the organization associated with a user. |
| Add Endpoint                         | POST    | `/endpoint/`                             | `{"name": <string>, "org_id": <int>\|"org_name": <string>}`     | `{"message": "Endpoint added successfully", "endpoint": {"id": endpoint.id, "name": endpoint.name, "organization_id": endpoint.organization_id}}` | Create a new endpoint.                       |
| Update Endpoint                      | PUT     | `/endpoint/<endpoint_id>`               | `{"name": <string>\|"org_id": <int>\|"org_name": <string>}`     | `{"message": "Endpoint updated successfully", "endpoint": {"id": endpoint.id, "name": endpoint.name, "organization_id": endpoint.organization_id}}` | Update an existing endpoint by endpoint ID.  |
| Delete Endpoint                      | DELETE  | `/endpoint/<endpoint_id>`               | N/A                                                  | `{"message": "Endpoint deleted successfully", "endpoint": {"id": endpoint.id, "name": endpoint.name, "organization_id": endpoint.organization_id}}` | Delete an endpoint by endpoint ID.           |
| Get User from Endpoint              | GET     | `/endpoint/<endpoint_id>/user/<user_id>`| N/A                                                  | `{"id": user.id, "name": user.name, "endpoint_id": user.endpoint_id, "organization_id": endpoint.organization_id}`                 | Retrieve a user associated with an endpoint. |
| Get Users from Endpoint             | GET     | `/endpoint/<endpoint_id>/users`         | N/A                                                  | `[{"id": user.id, "name": user.name, "endpoint_id": user.endpoint_id, "organization_id": endpoint.organization_id}, ...]`          | Retrieve all users associated with an endpoint.|
| Add Organization                     | POST    | `/organization/`                         | `{"name": <string>}`                                | `{"message": "Organization added successfully", "organization": {"id": organization.id, "name": organization.name}}` | Create a new organization.                   |
| Update Organization                  | PUT     | `/organization/<organization_id>`       | `{"name": <string>}`                                | `{"message": "Organization updated successfully", "organization": {"id": organization.id, "name": organization.name}}` | Update an existing organization by ID.       |
| Delete Organization                  | DELETE  | `/organization/<organization_id>`       | N/A                                                  | `{"message": "Organization deleted successfully", "organization": {"id": organization.id, "name": organization.name}}` | Delete an organization by ID.                |
| Get User from Organization           | GET     | `/organization/<organization_id>/user/<user_id>` | N/A                                                  | `{"id": user.id, "name": user.name, "endpoint_id": user.endpoint_id, "organization_id": endpoint.organization_id}` | Retrieve a user associated with an organization. |
| Get Users from Organization          | GET     | `/organization/<organization_id>/users` | N/A                                                  | `[{"id": user.id, "name": user.name, "endpoint_id": user.endpoint_id, "organization_id": endpoint.organization_id }, ...]` | Retrieve all users associated with an organization. |
| Get Endpoint from Organization       | GET     | `/organization/<organization_id>/endpoint/<endpoint_id>` | N/A                                                  | `{"id": endpoint.id, "name": endpoint.name, "organization_id": endpoint.organization_id}` | Retrieve an endpoint associated with an organization. |
| Get Endpoints from Organization      | GET     | `/organization/<organization_id>/endpoints` | N/A                                                  | `[{"id": endpoint.id, "name": endpoint.name, "organization_id": endpoint.organization_id}, ...]`  | Retrieve all endpoints associated with an organization. |

# Testing
Similarly to the application setup, all of the commands needed for testing purposes were created, and present in `shell\testing`.

### Initial Setup
Please edit the .env file as follows:
```plaintext
#Set the ENVIRONMENT value to 'PRODUCTION' if you want to run the production DB. Otherwise, testing DB will be selected.
ENVIRONMENT=<'TESTING'|any other text which is not 'PRODUCTION'>

#Production environment variables
PSQL_USERNAME=<PSQL production DB connection username>
PSQL_PASSWORD=<PSQL production DB connection password>
PSQL_URL=<PSQL production DB connection URL>
#Testing environment variables
PSQL_TEST_USERNAME=<PSQL testing DB connection username>
PSQL_TEST_PASSWORD=<PSQL testing DB connection password>
PSQL_TEST_URL=<PSQL testing DB connection URL>
```

For example (based on the credentials and URL in the `test_db_setup.sh`): 
```plaintext
ENVIRONMENT='TESTING'
.
.
.
PSQL_USERNAME='postgres'
PSQL_PASSWORD='password'
PSQL_URL='localhost:5433/postgres'
```

Then, run the `test_db_setup.sh` to initialize the test DB. In order to restart the existing PSQL DB container, you can run the `start_test_db.sh`

### Running Tests:
Simply run the `run_tests.sh` that triggers the `tests.py` file in the project's root folder.

# .env File Example:
```plaintext
#Set ENVIRONMENT value to 'PRODUCTION' if you want to run the production DB. Otherwise, testing DB will be selected.
ENVIRONMENT='PRODUCTION'

#Production environment variables
PSQL_USERNAME='postgres'
PSQL_PASSWORD='password'
PSQL_URL='localhost:5432/postgres'

#Testing environment variables
PSQL_TEST_USERNAME='postgres'
PSQL_TEST_PASSWORD='password'
PSQL_TEST_URL='localhost:5433/postgres'
```
