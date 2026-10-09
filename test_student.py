"""Tests for student name and roll number validation."""
import pytest

from student import Student


def test_valid_student():
    s = Student("Janhavi Chitre", 6)
    assert s.name == "Janhavi Chitre"
    assert s.roll_no == 6


def test_empty_name_rejected():
    with pytest.raises(ValueError):
        Student("   ", 6)


def test_non_string_name_rejected():
    with pytest.raises(ValueError):
        Student(None, 6)


def test_zero_roll_no_rejected():
    with pytest.raises(ValueError):
        Student("Janhavi", 0)


def test_non_integer_roll_no_rejected():
    with pytest.raises(ValueError):
        Student("Janhavi", "six")
