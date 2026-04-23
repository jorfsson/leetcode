default:
    just --list

get:
    poetry run leetcode --get-problem

get-category *CATEGORIES:
    poetry run leetcode --get-problem --categories {{CATEGORIES}}

completed PROBLEM:
    poetry run leetcode --completed "{{PROBLEM}}"

count PROBLEM:
    poetry run leetcode --get-count "{{PROBLEM}}"

add:
    poetry run leetcode --add-problem

reset:
    poetry run leetcode --reset

install:
    poetry install
