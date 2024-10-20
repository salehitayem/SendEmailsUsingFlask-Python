from flask import Flask
from config import Config
from flask_mail import Mail, Message


app = Flask(__name__)


app.config.from_object(Config)

mail = Mail(app)

# create you email contant
def send_daily_email():
  
    html_table = """
    <!DOCTYPE html>
    <html>
        <head>
            <style>
                
            </style>
        </head>
        <body>
            
        design your email
                   
        <tbody>
    """

    recipients = ['email@email.com', 'email2@email.com']

    # Send emails
    for recipient in recipients:
        msg = Message(
            subject='subject',
            recipients=[recipient]
        )
        msg.html = html_table
        mail.send(msg)
        print(f"Email sent to {recipient}")



if __name__ == '__main__':
    with app.app_context():
        send_daily_email()