# check\_file\_exists

Checks to see if a file exists or not. Alerts when the conditions are NOT met.

## Usage:

```
usage: check_file_exists.py [-h] -f FILENAME (--present | --not-present)
                            (--warning | --critical)

Check if a file does (not) exist and/or if the attributes are as expected

options:
  -h, --help            show this help message and exit
  -f FILENAME, --file FILENAME
                        File to work on

Presence check:
  Check for present or not present

  --present             Return OK if file is present, otherwise return a
                        failure
  --not-present         Return OK if file is not present, otherwise return a
                        failure

Alert severity:
  Set the severity of the alert

  --warning, -w         Severity of the alert will be WARNING
  --critical, -c        Severity of the alert will be CRITICAL
```

## Examples:
  * Critical severity alert when the file exists but should not

    check_file_exists --filename foo --not-present -c

  * Warning severity alert when the file does not exist but should

    check_file_exists --filename foo --present -w

## Sample Nagios configuration

This will fire a Nagios alert if the file `/run/reboot-required` exists.

```
define command {
    command_name        check-reboot-required
    command_line        $USER1$/check_file_exists.py --file /run/reboot-required --not-present --critical
}
```
