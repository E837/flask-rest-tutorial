'''main flask file'''

from flask import Flask, jsonify, request

app = Flask(__name__)

questions = []


@app.route('/questions')
def get_questions():
    '''get /questions'''
    return jsonify({'questions': questions})


@app.route('/questions', methods=['POST'])
def create_question():
    '''post /questions'''
    request_data = request.get_json()
    question = {
        'name': request_data['name'],
        'images': [],
    }
    questions.append(question)
    return jsonify(question)


app.run(debug=True)
