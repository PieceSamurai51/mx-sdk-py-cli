import pytest

from multiversx_sdk_cli.cli_shared import parse_proxy_headers
from multiversx_sdk_cli.errors import ArgumentsNotProvidedError


def test_parse_proxy_headers_accepts_valid_headers():
    headers = parse_proxy_headers(["Authorization=Bearer token", "X-Api-Key=abc"])

    assert headers == {"Authorization": "Bearer token", "X-Api-Key": "abc"}


def test_parse_proxy_headers_rejects_empty_key():
    with pytest.raises(ArgumentsNotProvidedError):
        parse_proxy_headers(["=value"])


def test_parse_proxy_headers_rejects_whitespace_only_key():
    with pytest.raises(ArgumentsNotProvidedError):
        parse_proxy_headers(["   =value"])
