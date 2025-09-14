import sys
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command")
    parser.add_argument("benefit_slug")
    parser.add_argument("--no-write-if-unchanged", action="store_true")
    parser.add_argument("--fake-llm", action="store_true")
    args = parser.parse_args()

    if args.command == "harvest":
        print(f"harvest called for: {args.benefit_slug}")
        sys.exit(0)
    else:
        print("Unknown command")
        sys.exit(1)

if __name__ == "__main__":
    main()