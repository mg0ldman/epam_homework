from homework4.task_3_get_print_output import my_precious_logger


def test_my_precious_logger_stderr(capsys):
    """Testing that function writes string to stderr if
    it starts with an "error" substring"""
    my_precious_logger('error: file not found')
    captured = capsys.readouterr()
    assert captured.err == 'error: file not found'
    assert captured.out == ''


def test_my_precious_logger_stdout(capsys):
    """Testing that function writes string to stdout if
    it doesn't start with an "error" substring"""
    my_precious_logger('abc')
    captured = capsys.readouterr()
    assert captured.out == 'abc'
    assert captured.err == ''


def test_my_precious_logger_empty_str(capsys):
    """Testing that stderr and stdout remain empty if
     the string passed to the function is empty"""
    my_precious_logger('')
    captured = capsys.readouterr()
    assert captured.out == ''
    assert captured.err == ''
