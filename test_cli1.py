import pytest

from pgbackup import cli

url = "postgres://bob@example.com:5432/db_one"

@pytest.fixture()
def parser():
    return cli.create_parser()

def test_parser_without_driver(parser):

    with pytest.raises(SystemExit):
        parser.parse_args([url])

def test_parser_with_driver(parser):

    with pytest.raises(SystemExit):
        parser.parse_args([url, "--driver", "local"])

def test_parser_with_driver_and_destination(parser):
    args = parser.parse_args([url, "--driver", "local", "/some/path"])

    assert args.driver == "local"
    assert args.destination == "/some/path"

def test_parser_with_unknown_drivers(parser):
       with pytest.raises(SystemExit):
        parser.parse_args([url, "--driver", "azure", "destination"])

def test_parser_with_known_drivers(parser):

    for driver in ['local', 's3']:
        assert parser.parse_args([url, "--driver", driver, "destination"])