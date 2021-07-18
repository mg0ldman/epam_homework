from unittest.mock import patch

import pytest

from homework4.task_2_mock_input import count_dots_on_i


def test_count_dots_on_i_positive():
    """Testing that function returns a correct result with a sample data
     from mock object"""
    with patch('requests.get') as mock_get:
        url = 'https://www.multitran.com/'
        mock_get.return_value.text = 'sample text with letters'
        assert count_dots_on_i(url) == 1


def test_count_dots_on_i_exception():
    """Testing that ValueError is raised
    in case of any network error"""
    with patch('requests.get') as mock_get:
        url = 'https://www.multitran.com/'
        mock_get.side_effect = ValueError(f"Unreachable {url}")
        with pytest.raises(ValueError, match=f"Unreachable {url}"):
            count_dots_on_i(url)
