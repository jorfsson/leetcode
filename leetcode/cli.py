from argparse import ArgumentParser
from pathlib import Path

from .constants import DATA_URI, NEETCODE_150
from .services.problem_manager import ProblemManager


def create_parser() -> ArgumentParser:
    """Create and configure the CLI argument parser"""
    parser = ArgumentParser(
        description="LeetCode problem tracker with spaced repetition"
    )
    parser.add_argument(
        '--completed',
        action='store',
        dest='completed',
        type=str,
        help='Mark a problem as completed'
    )
    parser.add_argument(
        '--get-problem',
        action='store_true',
        dest='get_problem',
        help='Get next problem to solve (interactive mode)'
    )
    parser.add_argument(
        '--get-count',
        action='store',
        dest='get_count',
        type=str,
        help='Get completion count for a problem'
    )
    parser.add_argument(
        '--add-problem',
        action='store',
        dest='add_problem',
        nargs=2,
        metavar=('NAME', 'TAG'),
        help='Add a new problem with name and tag'
    )
    parser.add_argument(
        '--reset',
        action='store_true',
        dest='reset',
        help='Reset all problems to default state'
    )
    return parser


def main():
    """Main CLI entry point"""
    parser = create_parser()
    args = parser.parse_args()

    with open(DATA_URI / 'problems.json', 'r+') as jsonfile:
        manager = ProblemManager(jsonfile)

        if args.reset:
            manager.reset(NEETCODE_150)
            return

        if args.get_count:
            count = manager.get_count(args.get_count)
            print(f"Count for '{args.get_count}': {count}")
            return

        if args.get_problem:
            for name, data in manager.get_next_problem():
                print(f"\n{data['url']}")
                print(f"Tag: {data['tag']} | Count: {data['count']}")
                res = input("\nAction (completed/reset/exit): ").strip().lower()

                match res:
                    case 'completed':
                        count = manager.increment_count(name)
                        print(f"✓ Marked as completed! Total count: {count}")
                    case 'reset':
                        manager.reset(NEETCODE_150)
                        return
                    case 'exit':
                        return
                    case _:
                        continue

        if args.add_problem:
            manager.add_problem(args.add_problem[0], args.add_problem[1])

        if args.completed:
            count = manager.increment_count(args.completed)
            print(f"✓ Marked '{args.completed}' as completed! Total count: {count}")


if __name__ == "__main__":
    main()
