from homework3.task03 import make_filter

sample_data = [
     {
         "name": "Bill",
         "last_name": "Gilbert",
         "occupation": "was here",
         "type": "person",
     },
     {
         "is_dead": True,
         "kind": "parrot",
         "type": "bird",
         "name": "polly"
     }
]


def test_make_filter_late_binding():
    """Testing that function keyword_filter_func saves
    all arguments within the loop, not only the last ones"""
    keywords = {'name': 'polly', 'type': 'bird'}
    results = {}
    for key, value in keywords.items():
        def keyword_filter_func(key=key, value=value):
            results[key] = value
        keyword_filter_func()
    assert results == keywords


def test_make_filter_with_data():
    """Testing that the function returns a
    correct result with some sample data"""
    assert make_filter(name='polly', type='bird').apply(sample_data) == \
           [{'is_dead': True, 'kind': 'parrot',
             'type': 'bird', 'name': 'polly'}]
