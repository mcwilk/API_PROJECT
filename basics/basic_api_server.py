from flask import jsonify, Flask, request


POSTS = [
    {
        'id': 1,
        'title': 'Title1',
        'text': 'Sample text 1'
    },
    {
        'id': 2,
        'title': 'Title3',
        'text': 'Sample text 3'
    },
    {
        'id': 3,
        'title': 'Title3',
        'text': 'Sample text 3'
    },
    {
        'id': 4,
        'title': 'Title4',
        'text': 'Sample text 4'
    }
]


app = Flask(__name__)


@app.route('/posts', methods=['GET', 'POST'])
def items():
    response_data = {
        'success': True,
        'data': []
    }

    if request.method == 'GET':
        response_data['data'] = POSTS

        return jsonify(response_data)

    elif request.method == 'POST':
        body = request.json

        if not ('id' in body and 'title' in body and 'text' in body):
            response_data['success'] = False
            response_data['error'] = "Please provide all required fields"
            response = jsonify(response_data)
            response.status_code = 400

        else:
            POSTS.append(body)
            response_data['data'] = POSTS
            response = jsonify(response_data)
            response.status_code = 201  # Created

        return response


@app.route('/posts/<int:post_id>')
def item(post_id):
    response_data = {
        'success': True,
        'data': []
    }

    try:
        item = [post for post in POSTS if post['id'] == post_id][0]

    except IndexError:
        response_data['success'] = False
        response_data['error'] = "Not found"
        response = jsonify(response_data)
        response.status_code = 404

    else:
        response_data['data'] = item
        response = jsonify(response_data)

    return response


@app.errorhandler(404)
def not_found(error):
    response_data = {
        'success': False,
        'data': [],
        'error': 'Not found'
    }
    response = jsonify(response_data)
    response.status_code = 404

    return response


if __name__ == '__main__':
    app.run(debug=True)
