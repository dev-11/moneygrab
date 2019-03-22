import argparse
import sys


def get_moneygrab_parser():
    parser = argparse.ArgumentParser("moneygrab CLI")
    parser.add_argument("company")
    return parser


def run_moneygrab(args):
    pass


if __name__ == "__main__":
    moneygrab_parser = get_moneygrab_parser()
    args = moneygrab_parser.parse_args(sys.argv[1:])
    run_moneygrab(args=args)
