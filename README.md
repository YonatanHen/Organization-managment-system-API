# API Documentation

## Overview

This API allows for the management of users, endpoints, and organizations. The API is built using Flask and SQLAlchemy, providing endpoints for creating, updating, deleting, and retrieving information about users, endpoints, and organizations.

## Base URL

`http://localhost:5000`

## APIs

## APIs

| API Name                             | Method  | Endpoint                                 | Response                                               | Description                                   |
|--------------------------------------|---------|------------------------------------------|--------------------------------------------------------|-----------------------------------------------|
| Add User                             | POST    | `/user/`                                 | `{"message": "User added successfully", "user": {"id": user.id, "name": user.name, "endpoint_id": user.endpoint_id, "organization_id": endpoint.organization_id}}` | Create a new user.                           |
| Update User                          | PUT     | `/user/<user_id>`                       | `{"message": "User updated successfully", "user": {"id": user.id, "name": user.name, "endpoint_id": user.endpoint_id, "organization_id": endpoint.organization_id}}` | Update an existing user by user ID.         |
| Delete User                          | DELETE  | `/user/<user_id>`                       | `{"message": "User deleted successfully", "user": {"id": user.id, "name": user.name, "endpoint_id": user.endpoint_id, "organization_id": endpoint.organization_id}}` | Delete a user by user ID.                   |
| Get User's Endpoint                  | GET     | `/user/<user_id>/endpoint`              | `{"id": endpoint.id, "name": endpoint.name, "organization_id": endpoint.organization_id}` | Retrieve the endpoint associated with a user.|
| Get User's Organization               | GET     | `/user/<user_id>/organization`          | `{"id": organization.id, "name": organization.name}` | Retrieve the organization associated with a user. |
| Add Endpoint                         | POST    | `/endpoint/`                             | `{"message": "Endpoint added successfully", "endpoint": {"id": endpoint.id, "name": endpoint.name, "organization_id": endpoint.organization_id}}` | Create a new endpoint.                       |
| Update Endpoint                      | PUT     | `/endpoint/<endpoint_id>`               | `{"message": "Endpoint updated successfully", "endpoint": {"id": endpoint.id, "name": endpoint.name, "organization_id": endpoint.organization_id}}` | Update an existing endpoint by endpoint ID.  |
| Delete Endpoint                      | DELETE  | `/endpoint/<endpoint_id>`               | `{"message": "Endpoint deleted successfully", "endpoint": {"id": endpoint.id, "name": endpoint.name, "organization_id": endpoint.organization_id}}` | Delete an endpoint by endpoint ID.           |
| Get User from Endpoint              | GET     | `/endpoint/<endpoint_id>/user/<user_id>`| `{"id": user.id, "name": user.name}`                 | Retrieve a user associated with an endpoint. |
| Get Users from Endpoint             | GET     | `/endpoint/<endpoint_id>/users`         | `[{"id": user.id, "name": user.name}, ...]`          | Retrieve all users associated with an endpoint.|
| Add Organization                     | POST    | `/organization/`                         | `{"message": "Organization added successfully", "organization": {"id": organization.id, "name": organization.name}}` | Create a new organization.                   |
| Update Organization                  | PUT     | `/organization/<organization_id>`       | `{"message": "Organization updated successfully", "organization": {"id": organization.id, "name": organization.name}}` | Update an existing organization by ID.       |
| Delete Organization                  | DELETE  | `/organization/<organization_id>`       | `{"message": "Organization deleted successfully", "organization": {"id": organization.id, "name": organization.name}}` | Delete an organization by ID.                |
| Get User from Organization           | GET     | `/organization/<organization_id>/user/<user_id>` | `{"id": user.id, "name": user.name, "endpoint_id": user.endpoint_id, "organization_id": endpoint.organization_id}` | Retrieve a user associated with an organization. |
| Get Users from Organization          | GET     | `/organization/<organization_id>/users` | `[{"id": user.id, "name": user.name, "endpoint_id": user.endpoint_id, "organization_id": endpoint.organization_id }, ...]` | Retrieve all users associated with an organization. |
| Get Endpoint from Organization       | GET     | `/organization/<organization_id>/endpoint/<endpoint_id>` | `{"id": endpoint.id, "name": endpoint.name, "organization_id": endpoint.organization_id}` | Retrieve an endpoint associated with an organization. |
| Get Endpoints from Organization      | GET     | `/organization/<organization_id>/endpoints` | `[{"id": endpoint.id, "name": endpoint.name}, ...]`  | Retrieve all endpoints associated with an organization. |

## Error Handling

All endpoints handle and return appropriate error messages and HTTP status codes in case of some errors. The error responses generally include the following:
- `400`: Bad Request.
- `404`: Resource or endpoint not found.
- `500`: Internal Server Error or DB-related Error.

## Conclusion

This API provides a comprehensive way to manage users, endpoints, and organizations in your application. For any questions or contributions, feel free to raise an issue or submit a pull request!
