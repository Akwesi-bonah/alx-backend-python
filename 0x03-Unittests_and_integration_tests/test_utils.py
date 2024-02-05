#!/usr/bin/env python3
""" Tests for utils module"""
import unittest
from parameterized import parameterized
from typing import Dict, Tuple, Union
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """Tests for accessing nested map"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)])
    def test_access_nested_map(
            self, nested_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, int],) -> None:
        """Test case for accessing nested map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)])
    def test_access_nested_map_exception(
            self, nested_map: Dict,
            path: Tuple[str],
            exception: Exception,) -> None:
        """Test for KeyError exception in accessing nested map"""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ Tests for get_json """
    @parameterized.expand([
        ("http://example.com", {"payload": True},),
        ("http://holberton.io", {"payload": False},)])
    def test_get_json(
            self,
            test_url: str,
            test_payload: Dict) -> None:
        """ Test get_json """
        req_attr = {"json.return_value": test_payload}
        with patch("requests.get", return_value=Mock(**req_attr)) as get_req:
            self.assertEqual(get_json(test_url), test_payload)
            get_req.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Tests the `memoize` function."""
    def test_memoize(self) -> None:
        """Tests `memoize`'s output."""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(
                TestClass,
                "a_method",
                return_value=lambda: 42,
                ) as memo_fxn:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
            memo_fxn.assert_called_once()