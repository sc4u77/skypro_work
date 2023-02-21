import pytest
from utils import get_data, get_filtered_data,get_last_values, get_formatted_data


def test_get_data(test_link):
    assert len(get_data(test_link)[0]) > 0
    assert get_data('https://wrong.url.com/')[0] is None
    assert get_data('https://github.com/archipov-proA/lesson_11_2')[0] is None
    assert get_data('https://github.com/archipov-proA/lesson_11_3')[0] is None



def test_get_filtered_data(test_data):
    assert len(get_filtered_data(test_data)) == 4
    assert len(get_filtered_data(test_data, filtered_empty_from=True)) == 2


def test_get_last_values(test_data):
    data = get_last_values(test_data, 4)
    assert data[0]['date'] == '2020-07-03T18:35:29.512364'
    assert len(data) == 4

def test_det_formatted_data(test_data):
    data = get_formatted_data(test_data)
    assert data = ' '


