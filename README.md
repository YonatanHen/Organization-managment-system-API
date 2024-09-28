# API Documentation

## Overview

This API allows for the management of users, endpoints, and organizations. The API is built using Flask and SQLAlchemy, providing endpoints for creating, updating, deleting, and retrieving information about users, endpoints, and organizations.

## Base URL

http://localhost:5000


## User Endpoints

| Endpoint                       | Method | Response Example                                         | Potential Errors                                      |
|-------------------------------|--------|---------------------------------------------------------|------------------------------------------------------|
| `/user/`                      | POST   | ```json {"message": "User added successfully", "user": {"id": 1, "name": "John Doe", "endpoint_id": 1}} ``` | 400: Missing "name" field.<br>500: Database error occurred. |
| `/user/<int:id>`              | PUT    | ```json {"message": "User updated successfully", "user": {"id": 1, "name": "John Smith", "endpoint_id": 2}} ``` | 400: Some fields in the payload are missing.<br>500: Database error occurred. |
|                               | DELETE | ```json {"message": "User deleted successfully", "user": {"id": 1, "name": "John Smith"}} ``` | 500: Database error occurred.                         |
| `/user/<int:id>/endpoint`     | GET    | ```json {"id": 1, "name": "User Endpoint", "organization_id": 1}``` | 500: Database error occurred.                         |
| `/user/<int:id>/organization`  | GET    | ```json {"id": 1, "name": "Organization Name"}```   | 500: Database error occurred.                         |

## Endpoint Endpoints

| Endpoint                       | Method | Response Example                                         | Potential Errors                                      |
|-------------------------------|--------|---------------------------------------------------------|------------------------------------------------------|
| `/endpoint/`                  | POST   | ```json {"message": "Endpoint added successfully", "endpoint": {"id": 1, "name": "New Endpoint"}}``` | 400: Missing "name" field.<br>500: Database error occurred. |
| `/endpoint/<int:id>`          | PUT    | ```json {"message": "Endpoint updated successfully", "endpoint": {"id": 1, "name": "Updated Endpoint"}}``` | 400: Some fields in the payload are missing.<br>500: Database error occurred. |
|                               | DELETE | ```json {"message": "Endpoint deleted successfully", "endpoint": {"id": 1, "name": "Updated Endpoint"}}``` | 500: Database error occurred.                         |
| `/endpoint/<int:id>/users`    | GET    | ```json [{"id": 1, "name": "User One"}, {"id": 2, "name": "User Two"}]``` | 500: Database error occurred.                         |

## Organization Endpoints

| Endpoint                       | Method | Response Example                                         | Potential Errors                                      |
|-------------------------------|--------|---------------------------------------------------------|------------------------------------------------------|
| `/organization/`              | POST   | ```json {"message": "Organization added successfully", "organization": {"id": 1, "name": "New Organization"}}``` | 400: Missing "name" field.<br>500: Database error occurred. |
| `/organization/<int:id>`      | PUT    | ```json {"message": "Organization updated successfully", "organization": {"id": 1, "name": "Updated Organization"}}``` | 400: The "name" field is required.<br>500: Database error occurred. |
|                               | DELETE | ```json {"message": "Organization deleted successfully", "organization": {"id": 1, "name": "Updated Organization"}}``` | 500: Database error occurred.                         |
| `/organization/<int:id>/users` | GET    | ```json [{"id": 1, "name": "User One"}, {"id": 2, "name": "User Two"}]``` | 500: Database error occurred.                         |
| `/organization/<int:id>/endpoints` | GET | ```json [{"id": 1, "name": "Endpoint One"}, {"id": 2, "name": "Endpoint Two"}]``` | 500: Database error occurred.                         |

## Error Handling

All endpoints return appropriate error messages and HTTP status codes in case of errors. The error responses generally include:
- `400`: Bad Request.
- `500`: Internal Server Error.

## Conclusion

This API provides a comprehensive way to manage users, endpoints, and organizations in your application. For any questions or contributions, feel free to raise an issue or submit a pull request!
