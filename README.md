# API Documentation

## Overview

This API allows for the management of users, endpoints, and organizations. The API is built using Flask and SQLAlchemy, providing endpoints for creating, updating, deleting, and retrieving information about users, endpoints, and organizations.

## Base URL

http://localhost:5000

## APIs

| Endpoint                                 | Method  | Response                                              
|------------------------------------------|---------|----------------------------------------------------------------------------------------------------------|
| `/user/`                                 | POST    | `{"message": "User added successfully", "user": {"id": user.id, "name": user.name, "endpoint_id": user.endpoint_id, "organization_id": endpoint.organization_id }}`
| `/user/<user_id>`                         | PUT     | `{"message": "User updated successfully", "user": {"id": user.id, "name": user.name, "endpoint_id": user.endpoint_id, "organization_id": endpoint.organization_id }}`
| `/user/<user_id>`                         | DELETE  | `{"message": "User deleted successfully", "user": {"id": user.id, "name": user.name, "endpoint_id": user.endpoint_id, "organization_id": endpoint.organization_id }}`
| `/user/<user_id>/endpoint`                | GET     | `{"id": endpoint.id, "name": endpoint.name, "organization_id": endpoint.organization_id}`
| `/user/<user_id>/organization`            | GET     | `{"id": organization.id, "name": organization.name}`
| `/endpoint/`                             | POST    | `{"message": "Endpoint added successfully", "endpoint": {"id": endpoint.id, "name": endpoint.name, "organization_id": endpoint.organization_id}}`
| `/endpoint/<endpoint_id>`                     | PUT     | `{"message": "Endpoint updated successfully", "endpoint": {"id": endpoint.id, "name": endpoint.name, "organization_id": endpoint.organization_id}`
| `/endpoint/<endpoint_id>`                     | DELETE  | `{"message": "Endpoint deleted successfully", "endpoint": {"id": endpoint.id, "name": endpoint.name, "organization_id": endpoint.organization_id}}`
| `/endpoint/<endpoint_id>/user/<user_id>` | GET     | `{"id": user.id, "name": user.name}`
| `/endpoint/<endpoint_id>/users`               | GET     | `[{"id": user.id, "name": user.name}, ...]`
| `/organization/`                         | POST    | `{"message": "Organization added successfully", "organization": {"id": organization.id, "name": organization.name}}`
| `/organization/<organization_id>`                 | PUT     | `{"message": "Organization updated successfully", "organization": {"id": organization.id, "name": organization.name}}`
| `/organization/<organization_id>`                 | DELETE  | `{"message": "Organization deleted successfully", "organization": {"id": organization.id, "name": organization.name}}`
| `/organization/<organization_id>/user/<user_id>` | GET | `{"id": user.id, "name": user.name, "endpoint_id": user.endpoint_id, "organization_id": endpoint.organization_id }`
| `/organization/<organization_id>/users`           | GET     | `[{"id": user.id, "name": user.name, "endpoint_id": user.endpoint_id, "organization_id": endpoint.organization_id }, ...]`
| `/organization/<organization_id>/endpoint/<endpoint_id>` | GET | `{"id": endpoint.id, "name": endpoint.name, "organization_id": endpoint.organization_id}`
| `/organization/<organization_id>/endpoints`       | GET     | `[{"id": endpoint.id, "name": endpoint.name}, ...]`


## Error Handling

All endpoints handles and return appropriate error messages and HTTP status codes in case of errors. The error responses generally include the following:
- `400`: Bad Request.
- `500`: Internal Server Error or DB-related Error.

## Conclusion

This API provides a comprehensive way to manage users, endpoints, and organizations in your application. For any questions or contributions, feel free to raise an issue or submit a pull request!
