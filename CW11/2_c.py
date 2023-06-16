import argparse
import os
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path")
parser.add_argument("-s", "--size")
arg = parser.parse_args()


if arg.size:
    for entry in os.listdir(arg.path):
        if os.path.isfile(entry):   
            entry_siz = os.path.getsize(entry)
            print(f"{entry} (Sized. {entry_siz}) KB")
        else:
            print(entry)

else:
    for entry in os.listdir(arg.path):
        print(entry)

# for entry in os.listdir(arg.path):
#     # entry_siz = os.path.getsize(entry)
#     # print(f"{entry} (Sized. {entry_siz}) KB")
#     if os.path.isfile(entry):   
#         entry_siz = os.path.getsize(entry)
#         print(f"{entry} (Sized. {entry_siz}) KB")
#     else:
#         print(entry)

