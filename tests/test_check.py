"""Unit tests"""

import shlex

import pytest

from check_file_exists import main

test_cases_sys_exit = [
    (
        "",  # No argument passed
        "the following arguments are required: -f/--file",
    ),
    (
        "-f tests/test_files/emptyfile.txt",
        "one of the arguments --present --not-present is required",
    ),
    (
        "-f tests/test_files/emptyfile.txt --present",
        "one of the arguments --warning/-w --critical/-c is required",
    ),
    (
        "-f tests/test_files/emptyfile.txt --present --warning",
        "OK: File tests/test_files/emptyfile.txt: is present",
    ),
    (
        "-f tests/test_files/emptyfile.txt --present --critical",
        "OK: File tests/test_files/emptyfile.txt: is present",
    ),
    (
        "-f tests/test_files/emptyfile.txt --not-present --warning",
        "WARNING: File tests/test_files/emptyfile.txt: is present",
    ),
    (
        "-f tests/test_files/emptyfile.txt --not-present --critical",
        "CRITICAL: File tests/test_files/emptyfile.txt: is present",
    ),
    (
        "-f tests/test_files/missingfile.txt --present --warning",
        "WARNING: File tests/test_files/missingfile.txt: is not present",
    ),
    (
        "-f tests/test_files/missingfile.txt --present --critical",
        "CRITICAL: File tests/test_files/missingfile.txt: is not present",
    ),
    (
        "-f tests/test_files/missingfile.txt --not-present --warning",
        "OK: File tests/test_files/missingfile.txt: is not present",
    ),
    (
        "-f tests/test_files/missingfile.txt --not-present --critical",
        "OK: File tests/test_files/missingfile.txt: is not present",
    ),
]


@pytest.mark.parametrize("command, expected_output", test_cases_sys_exit)
def test_checks_sys_exit(capsys, command, expected_output):
    with pytest.raises(SystemExit):
        main(shlex.split(command))
    captured = capsys.readouterr()
    output = captured.out + captured.err
    assert expected_output in output
