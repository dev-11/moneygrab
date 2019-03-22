import pytest

from moneygrab.cli import get_moneygrab_parser


def test_parser():
    parser = get_moneygrab_parser()
    company_name = "fake_corp"
    args = parser.parse_args([company_name])
    assert args.company == company_name
