# -*- coding: utf-8 -*-
"""
Automated Test Runner for all 101 Python Mini Projects.
Validates:
1. Syntax and compilation for all main.py files
2. Execution of every script using its specific archetype inputs/flags
3. Complete 100% pass verification
"""

import sys
import os
import subprocess
import py_compile
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
PROJECTS_DIR = BASE_DIR / "projects"

# Match each project number to its archetype/test strategy
# Custom 1-10, Archetype 1-6
ARCHETYPES = {
    1: "custom_1", 2: "custom_2", 3: "custom_3", 4: "custom_4", 5: "custom_5",
    6: "custom_6", 7: "custom_7", 8: "custom_8", 9: "custom_9", 10: "custom_10"
}
for num in range(11, 102):
    ARCHETYPES[num] = ((num - 11) % 6) + 1

def main():
    print("=" * 70)
    print("        RUNNING TEST SUITE ACROSS ALL 101 PYTHON PROJECTS")
    print("=" * 70)

    project_folders = sorted(list(PROJECTS_DIR.iterdir()))
    total = len(project_folders)
    if total != 101:
        print(f"[!] Warning: Expected 101 project folders, found {total}")

    passed_compilation = 0
    passed_execution = 0

    for p_folder in project_folders:
        folder_name = p_folder.name
        num = int(folder_name[:3])
        main_py = p_folder / "main.py"

        if not main_py.exists():
            print(f"[{num:03d}/101] FAIL: missing main.py")
            continue

        # 1. Compilation
        try:
            py_compile.compile(str(main_py.resolve()), doraise=True)
            passed_compilation += 1
        except Exception as e:
            print(f"[{num:03d}/101] SYNTAX ERROR: {e}")
            continue

        # 2. Execution parameters
        arch = ARCHETYPES.get(num)
        cmd = [sys.executable, "main.py"]
        input_data = ""

        if arch == "custom_1":
            input_data = "master123\n5\n"
        elif arch == "custom_2":
            input_data = "2\n2026-11\n4\n"
        elif arch == "custom_3":
            input_data = "demo_files\ny\n"
        elif arch == "custom_4":
            input_data = ""
        elif arch == "custom_5":
            input_data = "2\n3\n1\nTester\n"
        elif arch == "custom_6":
            cmd.append("--test")
        elif arch == "custom_7":
            input_data = "London\n"
        elif arch == "custom_8":
            input_data = "2\npython\n4\n"
        elif arch == "custom_9":
            input_data = "2\n4\n"
        elif arch == "custom_10":
            input_data = "3\n4\n"
        elif arch == 1:
            # SQLite record tracker: List (2), Exit (5)
            input_data = "2\n5\n"
        elif arch == 2:
            # File searcher: query "python"
            input_data = "python\n"
        elif arch == 3:
            # CSV audit: file "sample.csv"
            input_data = "sample.csv\n"
        elif arch == 4:
            # Flask API: self test mode
            cmd.append("--test")
        elif arch == 5:
            # CSV dataset profiler: file "sample.csv"
            input_data = "sample.csv\n"
        elif arch == 6:
            # Backup sync: dry run
            cmd.append("--dry-run")

        try:
            res = subprocess.run(
                cmd,
                input=input_data,
                text=True,
                capture_output=True,
                cwd=str(p_folder.resolve()),
                timeout=12
            )
            if res.returncode == 0:
                passed_execution += 1
            else:
                print(f"[{num:03d}/101] FAIL {folder_name} (returncode {res.returncode})")
                if res.stderr:
                    print(f"       stderr: {res.stderr[:200]}")
        except subprocess.TimeoutExpired:
            print(f"[{num:03d}/101] TIMEOUT {folder_name}")
        except Exception as e:
            print(f"[{num:03d}/101] ERROR {folder_name}: {e}")

    print("\n" + "=" * 70)
    print("TEST RESULTS SUMMARY:")
    print(f"  Total Projects:     {total}")
    print(f"  Passed Compilation: {passed_compilation}/{total} ({passed_compilation/total*100:.1f}%)")
    print(f"  Passed Execution:   {passed_execution}/{total} ({passed_execution/total*100:.1f}%)")
    print("=" * 70)

    if passed_compilation == total and passed_execution == total:
        print("[SUCCESS] ALL 101 PROJECTS WORK CORRECTLY WITH ZERO ERRORS!")
        return 0
    else:
        print(f"[FAIL] {total - passed_execution} projects need attention.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
