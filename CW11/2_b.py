import argparse
import os
from pathlib import Path

parser = argparse.ArgumentParser()

parser.add_argument("-p", "--path")

arg = parser.parse_args()

# target_dir = Path(arg.path)

# for entry in target_dir.iterdir():
#     print(entry.name)

# target_dir = os.listdir(arg.path)

for entry in os.listdir(arg.path):
    print(entry)
