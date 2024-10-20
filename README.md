# Daily Email Sender with Flask and Flask-Mail

A Python script that sends daily emails to specified recipients using Flask and Flask-Mail.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Logging](#logging)
- [Error Handling](#error-handling)
- [Scheduling the Script](#scheduling-the-script)
- [Security Considerations](#security-considerations)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Introduction

This project provides a simple way to send daily emails to a list of recipients using Python, Flask, and Flask-Mail. It is designed to be run automatically (e.g., via a scheduled task or cron job) and can be customized to send any HTML content.

## Features

- Send HTML-formatted emails
- Configurable list of recipients
- Uses Gmail's SMTP server
- Can be scheduled to run daily
- Easy to configure and customize

## Prerequisites

- Python 3.x
- A Gmail account with an app password
- Basic knowledge of Python

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/salehitayem/SendEmailsUsingFlask-Python.git
    ```
2. **Navigate to the project directory:**
   ```bash
   cd SendEmailsUsingFlask-Python
   ```
3. **Create a virtual environment:**
   On Windows:
   ```bash
    python -m venv venv
   ```
   On macOS/Linux:
   ```bash
    python3 -m venv venv
   ```
4. **Activate the virtual environment:**
   On Windows:
   ```bash
   venv\Scripts\activate
   ```
   On macOS/Linux:
   ```bash
   source venv/bin/activate
   ```
5. **Install the required packages:**
   ```bash
   pip install -r req.txt
   ```

## Configuration

### 1. Set Up Gmail SMTP Access

To use Gmail's SMTP server, you need to configure your Gmail account to allow SMTP access.

**Important:** As of May 30, 2022, Google no longer supports the use of third-party apps or devices which ask you to sign in to your Google Account using only your username and password. Instead, you must use an App Password.

#### Steps to Generate an App Password:

1. **Enable Two-Factor Authentication:**

   - Go to your [Google Account Security Settings](https://myaccount.google.com/security).
   - Under "Signing in to Google," click on **"2-Step Verification"** and follow the prompts to set it up.

2. **Generate an App Password:**

   - After enabling 2-Step Verification, return to the **"Security"** page.
   - Click on **"App passwords."**
   - You may be prompted to enter your password again.
   - Under **"Select the app and device you want to generate the app password for,"** choose **"Mail"** as the app and **"Windows Computer"** (or your device) as the device.
   - Click **"Generate."**
   - Copy the 16-character app password provided. This is the password you'll use in your application.


### 2. Update `config.py`

Replace the placeholders with your actual email and app password:

```python
class Config:
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'your_email@gmail.com'  # Your Gmail address
    MAIL_PASSWORD = 'your_app_password'     # Your 16-character app password
    MAIL_DEFAULT_SENDER = ('Your Name', 'your_email@gmail.com')
  ```

### 3. Customize Recipients:
Edit the `recipients` list in `dailyMail.py`:
```python
recipients = ['recipient1@example.com', 'recipient2@example.com']
```

### 4. Customize Email Content:
Modify the `html_table` variable in `dailyMail.py` to change the email's HTML content:
```python
html_table = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            /* Your custom styles */
        </style>
    </head>
    <body>
        <h1>Your Custom Content</h1>
        <!-- Add more HTML content here -->
    </body>
</html>
"""
```

### 5. Subject Line
Update the subject line in `dailyMail.py`:
```python
msg = Message(
    subject='Your Email Subject',
    recipients=[recipient]
)
```
### Usage
  1. Run the Script Manually:
     ```bash
     python dailyMail.py
     ```
     This will send the emails to the specified recipients.
     
  3. Schedule the Script to Run Daily:
     - #On Windows#
       - Use the provided `run_daily_mail.bat` file.
       - Update the paths in `run_daily_mail.bat` to match your project directory.
       - Use Task Scheduler to run the batch file daily.
       Example `run_daily_mail.bat`:
      ```bash
      @echo on
      cd C:\path\to\your\project
      call venv\Scripts\activate
      python dailyMail.py
      echo Script finished.
      ```
  - #On macOS/Linux:#
    - Create a shell script similar to the batch file.
    - Use `cron` to schedule the script.

### Project Structure
  - `dailyMail.py`: Main script to send emails.
  - `config.py`: Configuration for email settings.
  - `req.txt`: Required Python packages.
  - `run_daily_mail.bat`: Batch file to run the script on Windows.


### Scheduling the Script

## On Windows
1. Update `run_daily_mail.bat`:
  Ensure the paths match your project directory:
  ```bash
  @echo on
  cd C:\path\to\your\project
  call venv\Scripts\activate
  python dailyMail.py
  echo Script finished.
```
2. Schedule with Task Scheduler:

  - Open Task Scheduler.
  - Click "Create Task."
  - Under the "General" tab, name your task.
  - Under the "Triggers" tab, click "New..." and set it to begin the task "On a schedule" daily at your desired time.
  - Under the "Actions" tab, click "New..." and set "Start a program" to your batch file.
  - Save the task.

## ON macOS/Linux
1. Create a Shell Script (`run_daily_mail.sh`):
   ```bash
   #!/bin/bash
    cd /path/to/your/project
    source venv/bin/activate
    python dailyMail.py
    ```
    Make it executable:
    ```bash
    chmod +x run_daily_mail.sh
    ```
2. Schedule with Cron:
   - Open the cron editor:
     ```bash
      crontab -e
     ```
   - Add a cron job (e.g., to run daily at 8 AM):
     ```bash
      0 8 * * * /path/to/run_daily_mail.sh
     ```


## Acknowledgments

- [Flask-Mail Documentation](https://flask-mail.readthedocs.io/en/latest/)
- [Flask Documentation](https://flask.palletsprojects.com/en/3.0.x/)
- [Python.org](https://www.python.org/)



### Contributing
Contributions are welcome! Please open an issue or submit a pull request.
   



