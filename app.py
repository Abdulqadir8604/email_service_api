from flask import Flask, request, render_template, jsonify
import yagmail


def send_email(recipient, subject, body):
    try:
        sender_email = "lamaqemailer@gmail.com"
        sender_password = "kenk oqub kbwk pyeo"
        yag = yagmail.SMTP(sender_email, sender_password)
        yag.send(recipient, subject, body)
        return True
    except:
        return False


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/email/email=<email>&subject=<subject>&body=<body>', methods=['GET'])
def show_email(email, subject, body):
    sent = send_email(email, subject, body)
    return jsonify({
        'recipient_email': email,
        'subject': subject,
        'body': body,
        'sent': sent
    })


@app.route('/send', methods=['POST'])
def send():
    email = request.form.get('email')
    subject = request.form.get('subject')
    body = request.form.get('body')

    sent = send_email(email, subject, body)

    return jsonify({
        'recipient_email': email,
        'subject': subject,
        'body': body,
        'sent': sent
    })


if __name__ == '__main__':
    app.run()
