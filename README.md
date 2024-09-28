# API Documentation

## Overview

This API allows for the management of users, endpoints, and organizations. The API is built using Flask and SQLAlchemy, providing endpoints for creating, updating, deleting, and retrieving information about users, endpoints, and organizations.

## Base URL

http://localhost:5000

## APIs

## APIs

| API Name                             | Endpoint                                 | Method  | Response                                               | Description                                   |
|--------------------------------------|------------------------------------------|---------|--------------------------------------------------------|-----------------------------------------------|
| Add User                             | `/user/`                                 | POST    | `{"message": "User added successfully", "user": {"id": user.id, "name": user.name, "endpoint_id": user.endpoint_id, "organization_id": endpoint.organization_id}}` | Create a new user.                           |
| Update User                          | `/user/<user_id>`                       | PUT     | `{"message": "User updated successfully", "user": {"id": user.id, "name": user.name, "endpoint_id": user.endpoint_id, "organization_id": endpoint.organization_id}}` | Update an existing user by user ID.         |
| Delete User                          | `/user/<user_id>`                       | DELETE  | `{"message": "User deleted successfully", "user": {"id": user.id, "name": user.name, "endpoint_id": user.endpoint_id, "organization_id": endpoint.organization_id}}` | Delete a user by user ID.                   |
| Get User's Endpoint                  | `/user/<user_id>/endpoint`              | GET     | `{"id": endpoint.id, "name": endpoint.name, "organization_id": endpoint.organization_id}` | Retrieve the endpoint associated with a user.|
| Get User's Organization               | `/user/<user_id>/organization`          | GET     | `{"id": organization.id, "name": organization.name}` | Retrieve the organization associated with a user. |
| Add Endpoint                         | `/endpoint/`                             | POST    | `{"message": "Endpoint added successfully", "endpoint": {"id": endpoint.id, "name": endpoint.name, "organization_id": endpoint.organization_id}}` | Create a new endpoint.                       |
| Update Endpoint                      | `/endpoint/<endpoint_id>`               | PUT     | `{"message": "Endpoint updated successfully", "endpoint": {"id": endpoint.id, "name": endpoint.name, "organization_id": endpoint.organization_id}}` | Update an existing endpoint by endpoint ID.  |
| Delete Endpoint                      | `/endpoint/<endpoint_id>`               | DELETE  | `{"message": "Endpoint deleted successfully", "endpoint": {"id": endpoint.id, "name": endpoint.name, "organization_id": endpoint.organization_id}}` | Delete an endpoint by endpoint ID.           |
| Get User from Endpoint              | `/endpoint/<endpoint_id>/user/<user_id>`| GET     | `{"id": user.id, "name": user.name}`                 | Retrieve a user associated with an endpoint. |
| Get Users from Endpoint             | `/endpoint/<endpoint_id>/users`         | GET     | `[{"id": user.id, "name": user.name}, ...]`          | Retrieve all users associated with an endpoint.|
| Add Organization                     | `/organization/`                         | POST    | `{"message": "Organization added successfully", "organization": {"id": organization.id, "name": organization.name}}` | Create a new organization.                   |
| Update Organization                  | `/organization/<organization_id>`       | PUT     | `{"message": "Organization updated successfully", "organization": {"id": organization.id, "name": organization.name}}` | Update an existing organization by ID.       |
| Delete Organization                  | `/organization/<organization_id>`       | DELETE  | `{"message": "Organization deleted successfully", "organization": {"id": organization.id, "name": organization.name}}` | Delete an organization by ID.                |
| Get User from Organization           | `/organization/<organization_id>/user/<user_id>` | GET | `{"id": user.id, "name": user.name, "endpoint_id": user.endpoint_id, "organization_id": endpoint.organization_id}` | Retrieve a user associated with an organization. |
| Get Users from Organization          | `/organization/<organization_id>/users` | GET     | `[{"id": user.id, "name": user.name, "endpoint_id": user.endpoint_id, "organization_id": endpoint.organization_id }, ...]` | Retrieve all users associated with an organization. |
| Get Endpoint from Organization       | `/organization/<organization_id>/endpoint/<endpoint_id>` | GET | `{"id": endpoint.id, "name": endpoint.name, "organization_id": endpoint.organization_id}` | Retrieve an endpoint associated with an organization. |
| Get Endpoints from Organization      | `/organization/<organization_id>/endpoints` | GET | `[{"id": endpoint.id, "name": endpoint.name}, ...]`  | Retrieve all endpoints associated with an organization. |

## Error Handling

All endpoints handles and return appropriate error messages and HTTP status codes in case of errors. The error responses generally include the following:
- `400`: Bad Request.
- `500`: Internal Server Error or DB-related Error.

## Conclusion

This API provides a comprehensive way to manage users, endpoints, and organizations in your application. For any questions or contributions, feel free to raise an issue or submit a pull request!
