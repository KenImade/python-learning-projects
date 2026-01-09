# Python Project-Based Learning

This repository contains my solutions and mini-project while studying Introducing Python, 3rd Edition by Bill Lubanovic.

Instead of only reading the book, I built small projects for each chapter and a full capstone project: a Personal Wealth Tracker, which grows as new concepts are learned.

## Goals of this Repository

- Reinforce Python concepts through hands-on practice
- Build progressively more complex programs
- Demonstrate understanding of:
  - Core Python syntax
  - Data structures
  - Functions and modules
  - File handling and databases
  - Object-oriented programming
  - APIs, scraping, concurrency and GUIs
- Finish with a real-world capstone project

## Repository Structure

```
introducing-python-projects/
│
├── chapter_01/
├── chapter_02/
├── chapter_03/
├── ...
├── chapter_27/
│
├── capstone_personal_wealth_tracker/
│   ├── data/
│   ├── database/
│   ├── src/
│   ├── tests/
│   └── README.md
│
└── README.md
```

Each chapter folder contains 3-5 mini-projects related to that chapter's topic.

## Chapter Project Roadmap

| Chapter | Topics                | Example Projects                    |
| ------- | --------------------- | ----------------------------------- |
| 1       | Running Python, print | Greeting script, math practice      |
| 2       | Types, variables      | Temp converter, shopping bill       |
| 3       | if / while / input    | Guessing game, ATM simulator        |
| 4       | Strings               | Palindrome checker, email validator |
| 5       | Lists, dicts, sets    | Contact book, grade tracker         |
| 6       | Loops                 | Word counter, dice statistics       |
| 7       | Functions             | Calculator module, converters       |
| 8       | Modules               | Quiz generator, password maker      |
| 9       | Files                 | To-do list with save/load           |
| 10      | Exceptions            | Safe calculator, input validation   |
| 11      | Classes               | BankAccount, inventory system       |
| 12      | Advanced OOP          | Shopping cart, custom errors        |
| 13      | Dates & time          | Countdown app, time tracker         |
| 14      | Serialization         | Config loader, object save          |
| 15      | Databases             | Expense tracker with SQLite         |
| 16      | Web APIs              | Weather app, currency converter     |
| 17      | Scraping              | Job scraper, price tracker          |
| 18      | Threads               | Background logger                   |
| 19      | Async                 | Async API requests                  |
| 20      | Multiprocessing       | Parallel prime finder               |
| 21      | Testing               | Unit tests for earlier projects     |
| 22      | Debugging             | Profiling scripts                   |
| 23      | Packaging             | CLI tools with argparse             |
| 24      | Documentation         | Docstrings, Sphinx                  |
| 25      | GUI                   | Tkinter calculator                  |
| 26      | Visualization         | Expense charts                      |
| 27      | Integration           | Final refactor & polish             |

**Exact projects may vary slightly, but each chapter contains multiple practical exercises.**

## Capstone Project - Personal Wealth Tracker

The capstone project is built gradually across chapters and then finalized at the end.

### Features

- Add income and expenses
- Categories and budgets
- Monthly and yearly summaries
- SQLite database storage
- CSV export
- Error handling and validation
- Optional:
  - Currency conversion via API
  - GUI dashboard
  - Charts and reports

### Tech Used

- Python standard library
- SQLite
- Requests (for APIs)
- Tkinter (for GUI)
- unittest / pytest for testing

Capstone code lives in:

```text
capstone_personal_wealth_tracker/
```

with its own README explaining setup and usage.

## How to Run Projects

Most scripts can be run with

```bash
python filename.py
```

Some later projects may require installing packages:

```bash
pip install -r requirments.txt
```

## What I'm Practicing

- Clean code and readable structure
- Meaningful variable and function names
- Error handling
- Modular design
- Incremental development

## Progress

(I update this as I go.)

- ✅ Chapter 1
- ✅ Chapter 2
- ⬜️ Chapter 3
- ⬜️ Chapter 4
- ⬜️ Chapter 5
- ⬜️ Chapter 6
- ⬜️ Chapter 7
- ⬜️ Chapter 8
- ⬜️ Chapter 9
- ⬜️ Chapter 10
- ⬜️ Chapter 11
- ⬜️ Chapter 12
- ⬜️ Chapter 13
- ⬜️ Chapter 14
- ⬜️ Chapter 15
- ⬜️ Chapter 16
- ⬜️ Chapter 17
- ⬜️ Chapter 18
- ⬜️ Chapter 19
- ⬜️ Chapter 20
- ⬜️ Chapter 21
- ⬜️ Chapter 22
- ⬜️ Chapter 23
- ⬜️ Chapter 24
- ⬜️ Chapter 25
- ⬜️ Chapter 26
- ⬜️ Chapter 27
- ⬜️ Capstone Final Version

## Book Reference

Lubanovic, Bill. Introducing Python: Modern Computing in Simple Packages, 3rd Edition. O’Reilly Media.

All projects are inspired by topics from the book but implemented independently.
