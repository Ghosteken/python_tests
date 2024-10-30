import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465  # Using SSL
EMAIL_ADDRESS = 'aigberuan6@gmail.com'
EMAIL_PASSWORD = 'ebbipubecvdmzeam' 

recipients = [
    "aigberuan@gmail.com" 
]

def send_email():
    subject = "Test Email"
    body = "This is a test email sent from a Python script."

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = 'Anonymous Sender <no-reply@example.com>'  # Use a custom name and masked email
    msg['Reply-To'] = 'no-reply@example.com'  # Custom Reply-To address
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            
            # Send the email to all recipients
            for recipient in recipients:
                msg['To'] = recipient
                server.sendmail(EMAIL_ADDRESS, recipient, msg.as_string())
                print(f"Email sent to {recipient}")
    except Exception as e:
        print(f"Failed to send email: {e}")


send_email()
