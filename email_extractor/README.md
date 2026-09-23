# CodeAlpha Email Address Extractor

A Python automation script that scans a text file for email addresses and saves all unique ones to a new file. Built for the CodeAlpha Python Programming Internship (Task 3 - Task Automation).

## Features
- Scans any `.txt` file for email addresses using regex
- Removes duplicates automatically
- Saves results to a clean output file, one email per line
- Includes a `sample_input.txt` for testing

## Key Concepts Used
- `os` (file existence checks)
- `re` (regular expressions for pattern matching)
- File handling

## How to Run
```bash
python email_extractor.py
```
You'll be prompted for:
1. The path to your input `.txt` file (try `sample_input.txt`)
2. The path for the output file (press Enter to use the default `extracted_emails.txt`)

## Example
Input (`sample_input.txt`) contains scattered email addresses in normal text.
Output (`extracted_emails.txt`):
```
admin@company.co
john.doe@example.com
sara_smith123@company.co
support+billing@my-startup.io
```

## Internship
Built as part of the [CodeAlpha](https://www.codealpha.tech) Python Programming Internship.
