import pytest
import testfixtures

import file_functions


def test_print_file(capfd):
    """Testing the extract file content function, testing: for successful reads and missing files"""
    # Testing for a successful read by using tempDirectory to create a file and read the contents
    with testfixtures.TempDirectory() as tempDir:
        temp_filename = "testFile"
        test_line = b'This is a test file for extract msg file content function.'
        tempDir.write(temp_filename, test_line)
        file_path = tempDir.path + '/' + temp_filename
        file_functions.print_file(file_path)
    out, err = capfd.readouterr()
    assert out == "This is a test file for extract msg file content function.\n"
    # Testing for a missing file by passing a file that does not exist
    missing_file = 'missing_file.txt'
    with pytest.raises(FileNotFoundError) as file_error:
        file_functions.print_file(missing_file)
    assert file_error.type is FileNotFoundError
