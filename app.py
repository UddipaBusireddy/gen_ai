from flask import Flask, render_template, request
from transformers import pipeline
app = Flask(__name__)
generator = pipeline("text-generation", model="gpt2")
@app.route('/')
def form():
    return render_template('application_form.html')

@app.route('/submit', methods=['POST'])
def submit():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    address = request.form.get('address')
    user_details = (f"Generate a friendly and professional paragraph summarizing an application for "
                    f"{first_name} {last_name}, with email {email}, phone number {phone}, and address {address}.")
    try:
        response = generator(user_details, max_length=150, num_return_sequences=1)
        generated_paragraph = response[0]["generated_text"]
    except Exception as e:
        generated_paragraph = f"Error generating response: {e}"
    return render_template('submission_success.html', paragraph=generated_paragraph)

if __name__ == '__main__':
    app.run(debug=True,port=5001)
