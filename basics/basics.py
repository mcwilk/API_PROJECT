from flask import jsonify, Flask, make_response, request


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    # print(request.headers)
    # print(request.method)
    # print(request.path)
    # print(request.url)
    # print(request.headers["Authorization"])
    print(request.headers["Content-Type"])
    print(request.json)
    print(request.json["name"])
    print(request.json.get("name"))

    # response = make_response({'id': 1, 'title': 'Title 1'})
    # response.headers['Content-Type'] = 'application/json' # Not necessary
    # response.status_code = 201

    response = jsonify({'error': 'Not found!'})
    response.status_code = 404
    # print(response.json)

    # return "Hello from Flask!"
    return response


if __name__ == '__main__':
    app.run(debug=True)
