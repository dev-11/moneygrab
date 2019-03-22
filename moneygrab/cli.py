import argparse
import sys
import yaml
from moneygrab.spider import run_spider


def get_moneygrab_parser():
    parser = argparse.ArgumentParser("moneygrab CLI")
    parser.add_argument("company")
    return parser


def run_moneygrab(args):
    with open("../config.yaml", "r") as config_file:
        config = yaml.safe_load(config_file)

    run_spider(config["companies"][args.company])


if __name__ == "__main__":
    moneygrab_parser = get_moneygrab_parser()
    args = moneygrab_parser.parse_args(sys.argv[1:])
    run_moneygrab(args=args)
