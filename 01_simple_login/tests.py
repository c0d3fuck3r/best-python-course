from io import StringIO
import sys
import unittest
from unittest import mock

from simple_login import main


class TestSimpleLogin(unittest.TestCase):

    # decorators are applied bottom up
    @mock.patch('simple_login.print')
    @mock.patch('simple_login.input')
    def test_denied(self, _input, _print):
        _input.side_effect = ["admin", "some_password"]

        main()

        _print.assert_has_calls([
            mock.call.print("Access denied")
        ])

    @mock.patch('simple_login.print')
    @mock.patch('simple_login.input')
    def test_granted(self, _input, _print):
        _input.side_effect = ["admin", "qwerty"]

        main()

        _print.assert_has_calls([
            mock.call.print("Access granted")
        ])

    @mock.patch('simple_login.print')
    @mock.patch('simple_login.input')
    def test_empty_input(self, _input, _print):
        _input.side_effect = ["", "admin", "", "qwerty"]

        main()

        _print.assert_has_calls([
            mock.call.print("Access granted")
        ])

if __name__ == '__main__':
    unittest.main()
