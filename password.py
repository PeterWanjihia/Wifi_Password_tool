import sys
import pathlib

if len(sys.argv) != 2:
    print("Usage: python script.py <path>")
    sys.exit(1)

root = pathlib.Path(sys.argv[1])

if not root.exists():
    print(f"The path '{root}' does not exist.")
    sys.exit(1)

root = root.resolve()

print("Resolved Path:", root)
