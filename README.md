TODO APP + Bottle + Python + Local Dictionary
# TODO API
This is a simple TODO API built with the Bottle framework in Python. It allows you to create, retrieve, and toggle TODO items. The data is stored in-memory using a dictionary, making it a lightweight and easy-to-use solution for managing TODOs.

## Features
- Create a TODO item
- Get all TODO items
- Toggle the 'done' status of a TODO item

## Requirements
- Python 3.x
- Bottle framework

The server is started by running python todo.py.
The app.run(host='localhost', port=8080) line (line 45) starts the Bottle web server, listening on localhost and port 8080.

Creating a TODO:
curl -X POST http://localhost:8080/todo -H "Content-Type: application/json" -d '{"id": "1", "task": "Install Bottle"}'
When you use the curl command to create a TODO, it sends a POST request to the /todo endpoint.
The create_todo function (line 12) handles the request, extracts the id and task from the request body, and stores the TODO in the todos dictionary.
A response is returned indicating the TODO was created successfully.

Getting All TODOs:
curl http://localhost:8080/todos
When you use the curl command to get all TODOs, it sends a GET request to the /todos endpoint.
The get_todos function (line 26) handles the request and returns the entire todos dictionary.

Toggling a TODO:
curl -X POST http://localhost:8080/todo/toggle/1
When you use the curl command to toggle a TODO, it sends a POST request to the /todo/toggle/<todo_id> endpoint.
The toggle_todo function (line 34) handles the request, checks if the TODO with the given todo_id exists, toggles its 'done' status, and returns the updated TODO.

## Screenshot

![Output on Terminal](docs/screenshot1.png)

![Output on Browser] (docs/screenshot2.png)
