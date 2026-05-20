from datetime import datetime


def log_action(message):

    with open("logs/audit.log", "a") as file:

        timestamp = datetime.now()

        file.write(
            f"[{timestamp}] {message}\n"
        )