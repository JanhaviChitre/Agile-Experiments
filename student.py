"""Student Management System - student record with validation."""
import re

EMAIL_PATTERN = re.compile(
    r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
)


class Student:
    """A student record with validated name, roll number and email."""

    def __init__(self, name, roll_no, email):
        self.name = self.validate_name(name)
        self.roll_no = self.validate_roll_no(roll_no)
        self.email = self.validate_email(email)

    @staticmethod
    def validate_name(name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string.")
        return name.strip()

    @staticmethod
    def validate_roll_no(roll_no):
        if not isinstance(roll_no, int) or isinstance(roll_no, bool) \
                or roll_no <= 0:
            raise ValueError("Roll number must be a positive integer.")
        return roll_no

    @staticmethod
    def validate_email(email):
        if not isinstance(email, str) or not EMAIL_PATTERN.match(email):
            raise ValueError(f"Invalid email address: {email!r}")
        return email

    def __repr__(self):
        return (f"Student(name={self.name!r}, roll_no={self.roll_no}, "
                f"email={self.email!r})")
