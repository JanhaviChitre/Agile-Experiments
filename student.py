"""Student Management System - student record with validation."""


class Student:
    """A student record with validated name and roll number."""

    def __init__(self, name, roll_no):
        self.name = self.validate_name(name)
        self.roll_no = self.validate_roll_no(roll_no)

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

    def __repr__(self):
        return f"Student(name={self.name!r}, roll_no={self.roll_no})"
