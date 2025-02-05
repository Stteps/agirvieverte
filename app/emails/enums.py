from enum import Enum


class EmailSendingStrategy(Enum):
    LOCAL = "local"
    PRODUCTION = "production"  # Example of email sending service, can be other thing such as "mailtrap"
