# Here’s a simple script to automate sending emails based on their extension
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, body, to_email):
    from_email = "your_email@gmail.com"
    password = "your_password"

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()

send_email("Test Subject", "This is a test email body", "recipient@example.com")



# Here’s a simple script to move files from one folder to another based on their extension:
import os
import shutil

# Define the source and destination directories
source_dir = '/path/to/source/folder'
dest_dirs = {
    'images': '/path/to/images/folder',
    'documents': '/path/to/documents/folder',
    'music': '/path/to/music/folder'
}

# Create destination directories if they don't exist
for dir in dest_dirs.values():
    if not os.path.exists(dir):
        os.makedirs(dir)

# Function to move files based on their extension
def move_files():
    for filename in os.listdir(source_dir):
        src_file = os.path.join(source_dir, filename)
        
        if filename.endswith(('.png', '.jpg', '.jpeg', '.gif')):
            shutil.move(src_file, dest_dirs['images'])
        elif filename.endswith(('.pdf', '.docx', '.txt')):
            shutil.move(src_file, dest_dirs['documents'])
        elif filename.endswith(('.mp3', '.wav')):
            shutil.move(src_file, dest_dirs['music'])

move_files()
