import pytest
from testfixtures import TempDirectory

import file_functions


def test_print_file(capfd):
    with TempDirectory() as tempdir:
        temp_file = 'test.text'
        test_line = b'Hello'
        tempdir.write(temp_file, test_line)
        file_path = tempdir.path + '\\' + temp_file
        file_functions.print_file(file_path)
    out, err = capfd.readouterr()
    assert out == 'HELLO\n'
