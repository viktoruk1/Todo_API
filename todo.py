from bottle import Bottle, request, response

app = Bottle()

todos = {}

@app.get('/')
def home():
    return "Welcome to the TODO API! Use /todo to create a TODO, /todos to get all TODOs, and /todo/toggle/<todo_id> to toggle a TODO."

@app.post('/todo')
def create_todo():
    """
    Create a TODO item.
    The request body should contain 'id' and 'task'.
    """
    data = request.json
    todo_id = data.get('id')
    task = data.get('task')

    todos[todo_id] = {'task': task, 'done': False}

    response.status = 201
    return {'message': 'TODO created successfully', 'todo': todos[todo_id]}

@app.get('/todos')
def get_todos():
    """
    Get all TODO items.
    """
    return {'todos': todos}

@app.post('/todo/toggle/<todo_id>')
def toggle_todo(todo_id):
    """
    Toggle the 'done' status of a TODO item.
    """
    if todo_id in todos:
        todos[todo_id]['done'] = not todos[todo_id]['done']
        return {'message': 'TODO status toggled', 'todo': todos[todo_id]}
    else:
        response.status = 404
        return {'message': 'TODO not found'}
    
if __name__ == '__main__':
    app.run(host='localhost', port=8080)