"""Run the sample programs and check representative expected output."""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CASES = [('12_attendance_recovery', ['Result: 15 consecutive classes', 'Result: Impossible to reach 100%', 'Result: Invalid input']), ('13_atm_transaction_sequence', ['Summary: accepted = 3, rejected = 3, balance = 350', 'withdrawal limit exceeded']), ('16_multi-day_water_tank_simulation', ['First threshold interval: 1', 'Total overflow: 15; total shortage: 30']), ('27_hollow_diamond_pattern', ['Dimension: 4', '*     *', 'Invalid dimension; use 1 to 20']), ('28_repeated_transaction_detection', ['SUSPICIOUS: T01 7000 duplicate ID, above threshold', 'Summary: suspicious = 2, invalid = 2']), ('29_password_policy_validation', ['Good7!xy ACCEPTED', 'AAAabc1! REJECTED: three repeated characters', 'MyPassword1! REJECTED: prohibited substring']), ('31_examination_answer_evaluation', ['Anu: correct 4, incorrect 1, unanswered 1, score 15', 'Bala: correct 6, incorrect 0, unanswered 0, score 24', 'Deepa INVALID response']), ('35_character_run_compression', ["encoded: '3A2B4C'; lengths: 9 -> 6", "encoded: '12A'; lengths: 12 -> 3"]), ('37_monthly_calendar_generator', ['Mo Tu We Th Fr Sa Su', '       1  2  3  4  5', 'Invalid calendar settings']), ('42_student_marks_matrix_analysis', ['Bala: total 195, average 65.00', 'Science: average 33.33 LOW', 'Top performer: Bala (195)'])]

for folder, expected_lines in CASES:
    result = subprocess.run([sys.executable, str(ROOT / folder / "solution.py")], capture_output=True, text=True, timeout=10)
    if result.returncode != 0:
        raise AssertionError(folder + " failed: " + result.stderr)
    for expected in expected_lines:
        if expected not in result.stdout:
            raise AssertionError(folder + " missing: " + expected)
    print("PASS", folder)
print("All 10 sample checks passed.")
