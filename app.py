from flask import Flask, request, render_template, jsonify
import yagmail


def send_email(recipient, subject, body):
    try:
        sender_email = "lamaqemailer@gmail.com"
        sender_password = "dcdf xayd nigi eqov"
        yag = yagmail.SMTP(sender_email, sender_password)
        yag.send(recipient, subject, body)
        return jsonify({"success": True})
    except:
        return jsonify({"error": "Email could not be sent"})


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/email/email=<email>&subject=<subject>&body=<body>', methods=['GET'])
def show_email(email, subject, body):
    message = send_email(email, subject, body)
    return jsonify({
        'recipient_email': email,
        'subject': subject,
        'body': body,
        'message': message
    })


@app.route('/send', methods=['POST'])
def send():
    email = request.form.get('email')
    subject = request.form.get('subject')
    body = request.form.get('body')

    message = send_email(email, subject, body)

    return jsonify({
        'recipient_email': email,
        'subject': subject,
        'body': body,
        'message': message
    })


if __name__ == '__main__':
    app.run()
