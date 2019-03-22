import argparse
import sys
import yaml

from moneygrab.scraper import scrape_local_pages
from moneygrab.spider import run_spider


def get_moneygrab_parser():
    parser = argparse.ArgumentParser("moneygrab CLI")
    parser.add_argument("command", choices=["spider", "scrape"])
    parser.add_argument("company")
    return parser


def run_moneygrab(args):
    with open("../config.yaml", "r") as config_file:
        config = yaml.safe_load(config_file)

    company_config = config["companies"][args.company]
    if args.command == "spider":
        run_spider(company_config)
    elif args.command == "scrape":
        scrape_local_pages(company_config)
    else:
        raise ValueError(f"Unexpected command {args.command}")


if __name__ == "__main__":
    moneygrab_parser = get_moneygrab_parser()
    moneygrab_args = moneygrab_parser.parse_args(sys.argv[1:])
    run_moneygrab(args=moneygrab_args)
