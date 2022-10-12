import uuid
from flask import Flask

app = Flask(__name__)
instance_id = uuid.uuid4().hex


@app.route('/')
def hello_world():
    return {'msg': f'Hello from {instance_id}'}


if __name__ == '__main__':
    app.run(port=5000, host="0.0.0.0")
