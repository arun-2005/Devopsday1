import subprocess
import sys


def run_lint(path="."):
    """Run flake8 lint checks on the given path (file or directory)."""
    result = subprocess.run(
        [
            "flake8",
            path,
            "--max-line-length=100",
            "--exclude=venv,__pycache__",
        ],
        capture_output=True,
        text=True,
    )

    if result.stdout:
        print(result.stdout)

    if result.stderr:
        print(result.stderr)

    if result.returncode != 0:
        print("❌ Lint check failed")
        sys.exit(1)

    print("✅ Lint check passed")


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    run_lint(target)