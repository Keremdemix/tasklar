

import re       # regular expression yazmamızı saglayan python modulu

test_data = '''
    This
    is
    test
    1.1.1.1
    May 19 15:00:00
    192.168.1.2
    10.10.1
    <data class="">test</data>
    1923435430
    2001:0db8:0000:0000:0000:ff00:0042:8329
    10.0.2.15
    <ul></>

'''


def match_ip_address():
    ip_regexp = ""                                # write your regular expression here
    match = re.findall(ip_regexp, test_data)
    if not match:
        print('not matched', test_data)

    assert ('10.0.2.15' in match)
    assert ('1.1.1.1' in match)
    assert ('10.10.1' not in match)


match_ip_address()
