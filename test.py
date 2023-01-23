import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--compress", action="store_true",
                    help="Compress File")
argL = parser.parse_args()

print(argL.compress)