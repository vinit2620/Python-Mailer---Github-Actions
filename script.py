import smtplib
from email.mime.text import MIMEText #MIMeText is a class that represents the text of the email
from email.mime.multipart import MIMEMultipart #MIMEMultipart is a class that represents
import os

def send_mail(workflow_name, repo_name):
    # Email details
    sender_email = os.getenv('SENDER_EMAIL')
    sender_password = os.getenv('SENDER_PASSWORD')
    receiver_email = os.getenv('RECEIVER_EMAIL')

    #Email message
    subject = f"Workflow {workflow_name} in repository {repo_name} has failed"
    body = f"The workflow {workflow_name} in the repository {repo_name} has failed . Please check the details.\n More details:\nRun_ID: {workflow_run_id}\nRepo: {repo_name}\nWorkflow: {workflow_name}\nBranch: {branch_name}\nEvent: {event_name}\nConclusion: {conclusion}"
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)

        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f'Error: {e}')

send_mail(os.getenv('WORKFLOW_NAME'), os.getenv('REPO_NAME'), os.getenv('WORKFLOW_RUN_ID'), os.getenv('BRANCH_NAME'), os.getenv('EVENT_NAME'), os.getenv('CONCLUSION'))
