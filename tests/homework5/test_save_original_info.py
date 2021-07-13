from homework5.save_original_info import custom_sum


def test_save_original_info_docstring():
    """Testing that decorator saves the docstring from an original function"""
    assert custom_sum.__doc__ == "This function can sum" \
                                 " any objects which has __add__"


def test_save_original_info_name():
    """Testing that decorator saves the name of an original function"""
    assert custom_sum.__name__ == 'custom_sum'


def test_save_original_info_test_data(capsys):
    """Testing that the capabilities of the function are saved as well"""
    without_print = custom_sum.__original_func
    without_print(1, 2, 3, 4)
    custom_sum([1, 2, 3], [4, 5])
    captured = capsys.readouterr()
    assert captured.out == '10\n' \
                           '[1, 2, 3, 4, 5]\n'
