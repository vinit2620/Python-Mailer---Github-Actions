Python Mailer for GitHub Actions

This Python script sends an email notification when a GitHub Actions workflow fails. It uses Gmail’s SMTP server and environment variables to securely manage credentials.

Features

Sends an email to a specified recipient when a workflow fails.

Includes workflow name, repository name, and workflow run ID in the email.

Uses environment variables for email credentials for better security.

Requirements

Python 3.x

Gmail account with App Password enabled (2-Step Verification required)

Environment variables:

SENDER_EMAIL – The Gmail address used to send the email.

SENDER_PASSWORD – The app password generated from your Gmail account.

RECEIVER_EMAIL – The recipient email address.

WORKFLOW_NAME – Name of the GitHub Actions workflow.

REPO_NAME – GitHub repository name.

WORKFLOW_RUN_ID – Workflow run ID.
