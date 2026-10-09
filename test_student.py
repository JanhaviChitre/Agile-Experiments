"""Tests for student name, roll number and email validation."""
import pytest

from student import Student


def test_valid_student():
    s = Student("Janhavi Chitre", 6, "janhavi@example.com")
    assert s.name == "Janhavi Chitre"
    assert s.roll_no == 6
    assert s.email == "janhavi@example.com"


def test_empty_name_rejected():
    with pytest.raises(ValueError):
        Student("   ", 6, "janhavi@example.com")


def test_non_string_name_rejected():
    with pytest.raises(ValueError):
        Student(None, 6, "janhavi@example.com")


def test_zero_roll_no_rejected():
    with pytest.raises(ValueError):
        Student("Janhavi", 0, "janhavi@example.com")


def test_non_integer_roll_no_rejected():
    with pytest.raises(ValueError):
        Student("Janhavi", "six", "janhavi@example.com")


def test_valid_emails_accepted():
    for email in ["a@b.co", "first.last@college.edu", "user+tag@mail.org"]:
        assert Student("X", 1, email).email == email


def test_invalid_emails_rejected():
    for email in ["plainaddress", "missing@dot", "@nouser.com",
                  "user@.com", ""]:
        with pytest.raises(ValueError):
            Student("X", 1, email)
