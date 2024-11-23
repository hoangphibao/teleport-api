import smtplib
from email.message import EmailMessage

# Email configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'hoangphibao321@gmail.com'
EMAIL_PASSWORD = 'gnac imtu ioyx zsyj'

def send_email(to_email, subject, body):
    # Create the email
    msg = EmailMessage()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.set_content(body)

    # Send the email
    try:
        print("Email sending...")
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
            smtp.starttls()  # Secure the connection
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
            print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
