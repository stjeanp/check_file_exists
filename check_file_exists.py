#!/usr/bin/env python3
"""
Checks to see if a file exists or not. Alerts when the conditions are NOT met.
"""

import argparse
import os
from typing import Any
import sys


states = {
    "OK": 0,
    "WARNING": 1,
    "CRITICAL": 2,
    "UNKNOWN": 3,
    "DEPENDENT": 4,
}


def exit_with_message(message: str, state: str) -> None:
    """
    Exit with a message and state to conform to Nagios plugin expectations

    :param message: The message that will be outputted
    :type message: str
    :param state: The state of the check
    :type state: str

    :return: Nothing
    :rtype: None
    """

    print(f"CHECK_FILE: {state}: {message}")
    sys.exit(states[state])


def handle_args(args: Any = None) -> argparse.Namespace:
    """
    Parse the command line args

    :param args: The command line args
    :type args: Any

    :return: The parsed command line args
    :rtype: argparse.Namespace
    """
    parser = argparse.ArgumentParser(
        description="Check if a file does (not) exist and/or if the attributes are as expected",
    )

    parser.add_argument(
        "-f", "--file", dest="filename", help="File to work on", required=True
    )

    exists_group = parser.add_argument_group(
        "Presence check", "Check for present or not present"
    )
    present_or_not = exists_group.add_mutually_exclusive_group(required=True)
    present_or_not.add_argument(
        "--present",
        default=True,
        dest="exists",
        help="Return OK if file is present, otherwise return a failure",
        action="store_true",
    )
    present_or_not.add_argument(
        "--not-present",
        default=False,
        dest="exists",
        help="Return OK if file is not present, otherwise return a failure",
        action="store_false",
    )

    sev_group = parser.add_argument_group(
        "Alert severity", "Set the severity of the alert"
    )
    crit_warn = sev_group.add_mutually_exclusive_group(required=True)
    crit_warn.add_argument(
        "--warning",
        "-w",
        dest="severity",
        help="Severity of the alert will be WARNING",
        action="store_const",
        const="WARNING",
    )
    crit_warn.add_argument(
        "--critical",
        "-c",
        dest="severity",
        help="Severity of the alert will be CRITICAL",
        action="store_const",
        const="CRITICAL",
    )

    return parser.parse_args(args)


def main(args: Any = None) -> None:
    """
    Our main entrypoint: parse the args, run the check

    :param args: Command line args
    :type args: Any

    :return: Nothing
    :rtype: None
    """
    args = handle_args(args)

    file_exists = os.path.exists(args.filename)

    message = f"File {args.filename}: is{(' not' if not file_exists else '')} present"

    if file_exists == args.exists:
        mystate = "OK"
    else:
        mystate = args.severity

    exit_with_message(message, mystate)


if __name__ == "__main__":
    main()  # pragma: no cover
