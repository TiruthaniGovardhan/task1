from flask import Flask, request, render_template, redirect, url_for
from cryptography.fernet import Fernet

app = Flask(__name__)

# Generate a key for encryption and decryption
# You must use the same key for encryption and decryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    plain_text = request.form['text']
    encrypted_text = cipher_suite.encrypt(plain_text.encode()).decode()
    return render_template('result.html', result=encrypted_text, action="Encrypted")

@app.route('/decrypt', methods=['POST'])
def decrypt():
    encrypted_text = request.form['text']
    try:
        decrypted_text = cipher_suite.decrypt(encrypted_text.encode()).decode()
        return render_template('result.html', result=decrypted_text, action="Decrypted")
    except Exception as e:
        return render_template('result.html', result=str(e), action="Decryption Error")

if __name__ == '__main__':
    app.run(debug=True)
