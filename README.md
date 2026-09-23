# Expense Tracker

A simple command-line expense tracker written in Python. Add, list, edit, and
delete expenses, and see a summary of your spending by category — all stored
locally in a JSON file. Built as a Python fundamentals project.

## Features

- Add expenses with an item name, amount, category, and date
- List all expenses in a clean, aligned table
- Edit or delete any entry by number
- Summary of total spending, broken down by category
- Input validation — rejects non-numeric amounts and out-of-range selections
- Data persists between runs in `expenses.json`

## Requirements

- Python 3.12 or newer
- No third-party packages — uses only the Python standard library

## Setup

Clone the repo and set up a virtual environment:

    git clone https://github.com/FrostBlazeX/expense-tracker.git
    cd expense-tracker

    python -m venv .venv

    # Windows (PowerShell):
    .venv\Scripts\Activate.ps1

    # macOS / Linux:
    source .venv/bin/activate

## Usage

Run the app from the terminal:

    python tracker.py

Then follow the on-screen menu:

    1) Add  2) List  3) Edit  4) Delete  5) Summary  6) Quit

## Project structure

    expense-tracker/
    |- tracker.py        # the application
    |- requirements.txt  # dependencies (none yet - standard library only)
    |- .gitignore        # ignores .venv, __pycache__, and expenses.json
    |- expenses.json     # created at runtime, not tracked by git

## Roadmap

Part of a wider Python + AI-engineering learning path. Planned next steps:
stronger validation, automated tests, and eventually an API layer.
