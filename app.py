from flask import Flask, render_template, request, jsonify
from chatbot import predict_class, get_response, intents

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.form['message']
    ints = predict_class(user_message)
    res = get_response(ints, intents)
    return jsonify({"message": res})

if __name__ == '__main__':
    app.run(debug=True)
