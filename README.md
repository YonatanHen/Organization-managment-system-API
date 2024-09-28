# API Documentation

## Overview

This API allows for the management of users, endpoints, and organizations. The API is built using Flask and SQLAlchemy, providing endpoints for creating, updating, deleting, and retrieving information about users, endpoints, and organizations.

## Base URL

http://localhost:5000

## APIs

| Endpoint                                 | Method  | Response Example                                              | Potential Errors                                      |
|------------------------------------------|---------|--------------------------------------------------------------|------------------------------------------------------|
| `/user/`                                 | POST    | `{"message": "User added successfully", "user": user}`     | 400: Missing "name" field<br>500: Database error    |
| `/user/<int:id>`                         | PUT     | `{"message": "User updated successfully", "user": user}`    | 400: Missing fields<br>500: Database error           |
| `/user/<int:id>`                         | DELETE  | `{"message": "User deleted successfully", "user": user}`    | 500: Database error                                   |
| `/user/<int:id>/endpoint`                | GET     | `{"id": endpoint.id, "name": endpoint.name}`               | 500: Database error                                   |
| `/user/<int:id>/organization`            | GET     | `{"id": organization.id, "name": organization.name}`       | 500: Database error                                   |
| `/endpoint/`                             | POST    | `{"message": "Endpoint added successfully", "endpoint": endpoint}` | 400: Missing "name" field<br>500: Database error   |
| `/endpoint/<int:id>`                     | PUT     | `{"message": "Endpoint updated successfully", "endpoint": endpoint}` | 400: Missing fields<br>500: Database error          |
| `/endpoint/<int:id>`                     | DELETE  | `{"message": "Endpoint deleted successfully", "endpoint": endpoint}` | 500: Database error                                  |
| `/endpoint/<int:ep_id>/user/<int:user_id>` | GET     | `{"id": user.id, "name": user.name}`                        | 500: Database error                                   |
| `/endpoint/<int:id>/users`               | GET     | `[{"id": user.id, "name": user.name}, ...]`                | 500: Database error                                   |
| `/organization/`                         | POST    | `{"message": "Organization added successfully", "organization": organization}` | 400: Missing "name" field<br>500: Database error   |
| `/organization/<int:id>`                 | PUT     | `{"message": "Organization updated successfully", "organization": organization}` | 400: Missing fields<br>500: Database error          |
| `/organization/<int:id>`                 | DELETE  | `{"message": "Organization deleted successfully", "organization": organization}` | 500: Database error                                  |
| `/organization/<int:org_id>/user/<int:user_id>` | GET | `{"id": user.id, "name": user.name}`                        | 500: Database error                                   |
| `/organization/<int:id>/users`           | GET     | `[{"id": user.id, "name": user.name}, ...]`                | 500: Database error                                   |
| `/organization/<int:org_id>/endpoint/<int:ep_id>` | GET | `{"id": endpoint.id, "name": endpoint.name}`               | 500: Database error                                   |
| `/organization/<int:id>/endpoints`       | GET     | `[{"id": endpoint.id, "name": endpoint.name}, ...]`        | 500: Database error                                   |


## Error Handling

All endpoints return appropriate error messages and HTTP status codes in case of errors. The error responses generally include:
- `400`: Bad Request.
- `500`: Internal Server Error.

## Conclusion

This API provides a comprehensive way to manage users, endpoints, and organizations in your application. For any questions or contributions, feel free to raise an issue or submit a pull request!
