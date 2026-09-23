"""
Email Address Extractor
------------------------
CodeAlpha Python Programming Internship - Task 3 (Automation)

Goal: Automate a repetitive real-life task -- scanning a text file for
email addresses and saving all unique ones to a separate output file.

Key concepts used: os, re, file handling.
"""

import os
import re

# Regex pattern that matches standard email address formats
EMAIL_PATTERN = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")


def extract_emails_from_file(input_path):
    """
    Read a text file and return a sorted list of unique email addresses
    found in it.
    """
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")

    with open(input_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    found_emails = EMAIL_PATTERN.findall(content)

    # Remove duplicates while keeping the list sorted and clean
    unique_emails = sorted(set(found_emails))

    return unique_emails


def save_emails_to_file(emails, output_path):
    """Write a list of email addresses to an output file, one per line."""
    with open(output_path, "w") as f:
        for email in emails:
            f.write(email + "\n")


def main():
    print("=" * 50)
    print("  EMAIL ADDRESS EXTRACTOR")
    print("=" * 50)

    input_path = input("Enter path to the input .txt file: ").strip()
    output_path = input(
        "Enter path for the output file (default: extracted_emails.txt): "
    ).strip()

    if not output_path:
        output_path = "extracted_emails.txt"

    try:
        emails = extract_emails_from_file(input_path)
    except FileNotFoundError as e:
        print(f"\nError: {e}")
        return

    if not emails:
        print("\nNo email addresses were found in the file.")
        return

    save_emails_to_file(emails, output_path)

    print(f"\nFound {len(emails)} unique email address(es):")
    for email in emails:
        print(f"  - {email}")

    print(f"\nSaved to '{output_path}'")


if __name__ == "__main__":
    main()
