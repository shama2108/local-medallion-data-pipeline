import subprocess
import os
import sys

print("--- Step 1: Generating Fresh Bronze Data ---")
# sys.executable ensure karta hai ki virtual environment wala python hi use ho
subprocess.run([sys.executable, "generator.py"], check=True)

print("\n--- Step 2: Running dbt Transformations & Tests ---")
os.chdir("my_pipeline")
subprocess.run(["dbt", "run"], check=True)
subprocess.run(["dbt", "test"], check=True)

print("\n--- Pipeline Completed Successfully! 🚀 ---")