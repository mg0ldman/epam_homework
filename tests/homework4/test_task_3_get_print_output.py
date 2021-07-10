from homework4.task_3_get_print_output import my_precious_logger


def test_my_precious_logger_stderr(capsys):
    my_precious_logger('error: file not found')
    captured = capsys.readouterr()
    assert captured.err == 'error: file not found'
    assert captured.out == ''


def test_my_precious_logger_stdout(capsys):
    my_precious_logger('abc')
    captured = capsys.readouterr()
    assert captured.out == 'abc'
    assert captured.err == ''


def test_my_precious_logger_empty_str(capsys):
    my_precious_logger('')
    captured = capsys.readouterr()
    assert captured.out == ''
    assert captured.err == ''
