from unittest.mock import patch

import pytest

from multiversx_sdk_cli.config_env import (
    InvalidEnvironmentValue,
    _prepare_value_for_storage,
    get_proxy_headers,
)


def test_get_proxy_headers_supports_json_object_values_with_spaces():
    get_proxy_headers.cache_clear()

    with patch("multiversx_sdk_cli.config_env._get_raw_env_value", return_value={"Authorization": "Bearer token"}):
        assert get_proxy_headers() == {"Authorization": "Bearer token"}


def test_get_proxy_headers_supports_legacy_space_separated_format():
    get_proxy_headers.cache_clear()

    with patch(
        "multiversx_sdk_cli.config_env._get_raw_env_value",
        return_value="X-Api-Key=abc X-Custom-Header=value",
    ):
        assert get_proxy_headers() == {"X-Api-Key": "abc", "X-Custom-Header": "value"}


def test_prepare_proxy_headers_value_stores_json_object():
    value = '{"Authorization": "Bearer token", "X-Custom-Header": "value with spaces"}'

    assert _prepare_value_for_storage("proxy_headers", value) == {
        "Authorization": "Bearer token",
        "X-Custom-Header": "value with spaces",
    }


def test_prepare_proxy_headers_value_rejects_invalid_json_object():
    with pytest.raises(InvalidEnvironmentValue):
        _prepare_value_for_storage("proxy_headers", '{"Authorization": 123}')
