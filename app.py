from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from models import insert_event, get_latest_events
from datetime import datetime

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    event_type = request.headers.get("X-GitHub-Event")

    if event_type == "push":
        author = data['pusher']['name']
        to_branch = data['ref'].split('/')[-1]
        insert_event("push", author, to_branch=to_branch)

    elif event_type == "pull_request":
        pr = data['pull_request']
        action = data['action']
        author = pr['user']['login']
        from_branch = pr['head']['ref']
        to_branch = pr['base']['ref']

        if action == "opened":
            insert_event("pull_request", author, from_branch=from_branch, to_branch=to_branch, timestamp=pr['created_at'])
        elif action == "closed" and pr['merged']:
            insert_event("merge", author, from_branch=from_branch, to_branch=to_branch, timestamp=pr['merged_at'])

    return '', 200

@app.route('/events', methods=['GET'])
def events():
    return jsonify(get_latest_events())

if __name__ == '__main__':
    app.run(debug=True)
