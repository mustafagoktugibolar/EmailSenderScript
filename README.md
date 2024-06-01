# Email Sender Script

This is a simple script that allows you to send routine emails using Python.

## Prerequisites

- Python 3.x
- SMTP server credentials (e.g., Gmail SMTP)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/mustafagoktugibolar/EmailSenderScript.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Open the `config.py` file and update the SMTP server credentials and other settings.

2. Run the script:

    ```bash
    python3 email_sender.py
    ```

3. Set Up a Cron Job or Task Scheduler

To ensure this script runs daily, you can use cron jobs on Unix-based systems or Task Scheduler on Windows.

### On Unix-based Systems (Linux, macOS)

1. Open the crontab file:

```bash
    crontab -e
```
2. Add a new line to schedule the script to run daily at a specific time. For example, to run the script at 8 AM every day:
```bash
    0 8 * * * /usr/bin/python3/Script.py
```

### On Windows

1. Open Task Scheduler.
2. Create a new task.
3. Set the trigger to daily and specify the time.
4. Set the action to start a program, and provide the path to your Python executable and your script.

## Additional Notes
* Ensure that you keep your email credentials secure. For production use, consider using environment variables or a more secure method for storing credentials.
* You can customize the email body, add attachments, and handle errors more gracefully as needed.

This script will now send an email every day at the specified time. You can expand and customize it according to your specific needs, such as generating reports dynamically and attaching files.


## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
