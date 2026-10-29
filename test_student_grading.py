
import subprocess
import sys
import unittest
from pathlib import Path


class StudentGradingTests(unittest.TestCase):

    def test_program_starts_and_exits(self):
        program = Path(__file__).parent / "Student Grading.py"

        result = subprocess.run(
            [sys.executable, str(program)],
            input="2\n",
            text=True,
            capture_output=True,
            timeout=10
        )

        self.assertEqual(result.returncode, 0)
        self.assertIn(
            "Welcome to the Student Grade Evaluation System!",
            result.stdout
        )


if __name__ == "__main__":
    unittest.main()
