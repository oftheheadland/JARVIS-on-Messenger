import modules


def test_math():
    assert ('math' == modules.process_query('math 4*4')[0])
    assert ('math' == modules.process_query('distance between earth and sun math')[0])
    assert ('math' == modules.process_query('10 times 10 math')[0])
    assert ('math' != modules.process_query('what is 5 * 3')[0])
    assert ('math' != modules.process_query('something random')[0])

