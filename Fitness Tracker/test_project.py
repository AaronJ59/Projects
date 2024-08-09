import pytest
from project import get_exercise_info, check_format, make_table
import os
from datetime import date
from unittest.mock import patch, mock_open
from tabulate import tabulate


def test_get_exercise_info(monkeypatch):

    inputs = iter(["135", "3", "10"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    result = get_exercise_info('randomexercise')

    assert result == ("135", "3", "10", date.today(), "randomexercise.csv")


def test_make_table():

    with patch("os.path.isfile", return_value=True):
        dates = date.today()
        csv_data = f"Weight(lb),Sets,Reps,Date\n130,3,10,{dates}"

        with patch("builtins.open", mock_open(read_data=csv_data)):

            output = make_table("example_exercise")

            headers = ["Weight(lb)", "Sets", "Reps", "Date"]
            rows = [["130", "3", "10", dates]]

            assert output == tabulate(rows, headers, tablefmt="grid")

    with patch("os.path.isfile", return_value=False):

        assert make_table("example_exercise") == "Exercise does not exist"


def test_check_format(monkeypatch):
    date_example = date.today()
    tuple_example = ("155", "3", "10", date_example, "example_exericse.csv")
    output = ("155", "3", "10", date_example, "example_exericse.csv")

    assert check_format(tuple_example) == output


    tuple_example = ("155", "n", "10", date_example, "example_exericse.csv")
    input = "3"
    monkeypatch.setattr('builtins.input', lambda _: input)
    output = ("155", "3", "10", date_example, "example_exericse.csv")

    assert check_format(tuple_example) == output