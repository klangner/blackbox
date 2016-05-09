from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/tasks', methods=['GET'])
def list_tasks():
    tasks = [{'id': 1, 'name': 'Task 1'}, {'id': 2, 'name': 'Task 2'}, {'id': 3, 'name': 'Task 3'}]
    return json.dumps(tasks)


@app.route('/tasks/<int:task_id>')
def get_task(task_id):
    task = {'id': task_id, 'name': 'Task 1'}
    return json.dumps(task)


@app.route('/tasks', methods=['POST'])
def add_tasks():
    task = {'id': -1, 'name': 'Task 1'}
    return json.dumps(task)


@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = {'id': task_id, 'name': 'Task 1'}
    return json.dumps(task)


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    return 'Delete task: %d' % task_id


if __name__ == '__main__':
    app.debug = True
    app.run()
