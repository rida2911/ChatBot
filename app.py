from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

otp_store = {}  # Store OTPs temporarily for verification

# Route to serve the main HTML file
@app.route('/')
def index():
    return render_template('index.html')

# Endpoint to generate and send OTP
@app.route('/request_otp', methods=['POST'])
def request_otp():
    data = request.get_json()
    email = data.get('email')
    otp = random.randint(1000, 9999)  # Simple OTP generation
    otp_store[email] = otp
    return jsonify({'message': f"OTP sent to {email}. Please enter it to verify."})

# Endpoint to verify OTP and answer question
@app.route('/verify_otp_and_ask', methods=['POST'])
def verify_otp_and_ask():
    data = request.get_json()
    email = data.get('email')
    otp = data.get('otp')
    question = data.get('question')

    # Check if the OTP matches
    if otp_store.get(email) == int(otp):
        if 'java' in question.lower():
            return jsonify({'answer': "I will not answer Java questions."})
        else:
            answer = get_programming_answer(question)
            return jsonify({'answer': answer})
    else:
        return jsonify({'message': "Invalid OTP. Please try again."})

def get_programming_answer(question):
    # Basic placeholder for actual programming answers
    return f"This is a generic answer for your question: '{question}'"

if __name__ == '__main__':
    app.run(debug=True)

