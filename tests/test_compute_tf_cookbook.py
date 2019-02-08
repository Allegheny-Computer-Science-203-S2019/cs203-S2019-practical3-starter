"""Test cases for the module that uses a cookbook programming style"""

# TODO: Add correct import statements
# TODO: Add test cases to adequately cover the program
# TODO: Run test coverage monitoring and reporting with pytest-cov


def test_read_file_populates_data_0():
    """Checks that reading the file populates global data variable"""
    # pylint: disable=len-as-condition
    assert len(compute_tf_cookbook.data) == 0
    compute_tf_cookbook.read_file("inputs/input.txt")
    assert len(compute_tf_cookbook.data) != 0
