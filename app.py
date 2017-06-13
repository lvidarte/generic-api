from flask import Flask, request, jsonify

app = Flask(__name__)
data = {}

@app.route("/<name>", methods=['GET', 'POST'])
def endpoint(name):
    if request.method == 'POST':
        if name not in data:
            data[name] = []
        data[name].append(request.get_json(force=True))
        return jsonify({'result': 'ok'})
    else:
        return jsonify(data[name] if name in data else [])

if __name__ == '__main__':
    app.run(port=8080)
