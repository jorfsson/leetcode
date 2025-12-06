"""
LeetCode problem tracker with spaced repetition.

This module provides backward compatibility by importing the CLI main function.
For new code, import from leetcode.cli instead.
"""

from .cli import main

if __name__ == "__main__":
    main()
