# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a LeetCode problem tracking system that manages progress through the NeetCode 150 problem set using a spaced repetition algorithm. The application tracks completion counts, calculates next revisit dates, and provides intelligent problem selection.

## Project Structure

- `leetcode/app.py` - Main application module containing:
  - `LeetCode` class - Core problem tracking logic with spaced repetition
  - `neetcode_150` dict - Categorized problem set by topic
  - CLI argument parser for interactive problem management
- `data/problems.json` - Problem database storing completion metadata (counts, revisit dates, timestamps, tags)
- `data/problems.txt` - List of LeetCode problem URLs
- `pyproject.toml` - Poetry configuration with dependencies

## Development Commands

### Running the Application

```bash
# Interactive mode - get next problem to solve
poetry run leetcode --get-problem

# Mark a problem as completed (increments count, updates revisit date)
poetry run leetcode --completed "problem-name"

# Check completion count for a problem
poetry run leetcode --get-count "problem-name"

# Reset the problems database to default state
poetry run leetcode --reset
```

### Package Management

```bash
# Install dependencies
poetry install

# Add new dependency
poetry add <package-name>
```

## Core Architecture

### Spaced Repetition System

The application implements a spaced repetition algorithm with intervals: 1, 3, 7, 14, 30, 60, 90 days. Problems are automatically scheduled for revisit based on completion count.

### Problem Search

The `search()` method in `leetcode/app.py:225` implements fuzzy matching with:
1. Exact match attempt
2. Normalized match (underscores → hyphens)
3. Regex-based fuzzy matching with 2-character error tolerance

### Problem Selection Strategy

`get_next_problem()` in `leetcode/app.py:286` yields problems in priority order:
1. Problems due for revisit (revisit_date <= today)
2. Uncompleted problems (count = 0, no revisit_date)

### Data Structure

Each problem in `problems.json` contains:
- `url` - LeetCode problem URL
- `updated_datetime` - Last modification timestamp
- `revisit_date` - Next scheduled review date (ISO format)
- `count` - Number of times completed
- `tag` - Problem category from NeetCode 150

## Key Implementation Details

- Problem names can use spaces or hyphens interchangeably due to normalization
- The fuzzy search allows approximate matching to handle typos
- Interactive mode (`--get-problem`) accepts commands: "completed", "reset", "exit"
- Revisit dates use a capped progression (max 90 days after 7th completion)
