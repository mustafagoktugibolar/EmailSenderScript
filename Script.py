import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time

# Email credentials and settings
SMTP_SERVER = 'smtp.your-email-provider.com'  # e.g., 'smtp.gmail.com' for Gmail
SMTP_PORT = 587  # or 465 for SSL
EMAIL_ADDRESS = 'your-email@example.com'
EMAIL_PASSWORD = 'your-email-password'

# Function to send email
def send_email():
    # Email content
    to_address = 'recipient@example.com' # Recipient's email address
    subject = 'Daily Report' # Email subject
    body = 'This is your daily report.' # Email body

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_address
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server and send the email
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, to_address, msg.as_string())
        server.close()
        print('Email sent successfully.')
    except Exception as e:
        print(f'Failed to send email: {e}')

# Schedule the email to be sent daily
schedule.every().day.at("08:00").do(send_email)  # Adjust the time as needed

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
