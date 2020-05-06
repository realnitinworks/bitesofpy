import pytest

from workouts import print_workout_days

@pytest.mark.parametrize("test_input, expected", [
    ("upper", "Mon, Thu"),
    ("lower", "Tue, Fri"),
    ("30 min", "Wed"),
    ("cardio", "Wed"),
    ("body", "Mon, Tue, Thu, Fri"),
    ("#1", "Mon, Tue"),
    ("#2", "Thu, Fri")
])
def test_print_workout_days(test_input, expected, capsys):
    print_workout_days(test_input)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


def test_no_matching_workout(capsys):
    print_workout_days("invalid")
    captured = capsys.readouterr()
    assert captured.out.strip() == "No matching workout"
