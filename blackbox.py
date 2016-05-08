from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/tasks', methods=['GET'])
def list_tasks():
    return 'List of tasks.'


@app.route('/tasks/<int:task_id>')
def get_task(task_id):
    return 'Task: %d' % task_id


@app.route('/tasks', methods=['POST'])
def add_tasks():
    return 'Add new task.'


@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    return 'Update task: %d' % task_id


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    return 'Delete task: %d' % task_id


if __name__ == '__main__':
    app.debug = True
    app.run()
