from name_function import get_formatted_name

def test_first_last_name():
    '''Do name like rock start work?'''
    formatted_name = get_formatted_name('rock', 'star')
    assert formatted_name == 'Rock Star'
