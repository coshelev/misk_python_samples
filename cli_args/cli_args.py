// Command line argments processing. See https://habr.com/ru/post/725186/
import argparse

parser = argparse.ArgumentParser(prog='get_square',description='A CLI to calculate the square of an integer.')
parser.add_argument("num", type=int, help='An integer that needs to get the square value.')
parser.add_argument('--verbose',help='Print more info.')

args = parser.parse_args()

if args.verbose:
    print(f'The square of {args.num} is {args.num**2}')
else:
    print(args.num**2)
