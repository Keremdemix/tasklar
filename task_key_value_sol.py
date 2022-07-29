key_value_line = 'date=2013-03-15 15:59:21,esname=FHY,esid=FG224B3907501199,es_group=N/A,src=192.168.1.133,spt=52906,dst=173.194.39.154,dpt=80,vdom=root,rcv=11257,proto=http,url=googlesyndication.com,sid=62551133,info=URL has been visited,cat=webfilter'

parsed_result = {
    'Bytes': {
        'Received': 11257
    },
    'Destination': {
        'IP': '173.194.39.154',
        'Port': 80
    },
    'Event': {
        'Category': 'webfilter',
        'Info': 'URL has been visited'
    },
    'EventSource': {
        'ID': 'FG224B3907501199',
        'Name': 'FHY',
        'Group': 'N/A'
    },
    'Policy': {
        'ID': '86'
    },
    'Service': {
        'Name': 'http'
    },
    'Session': {
        'ID': '62551133'
    },
    'Source': {
        'IP': '192.168.1.133',
        'Port': 52906,
        'UserName': 'HULYA.OZASLAN'
    },
    'Time': {
        'Generated': '2013-03-15 15:59:21'
    },
    'URL': {
        'BaseDomain': 'googlesyndication.com'
    },
    'Virtual': {
        'Domain': 'root',
        'DataType': 'log'
    }
}


def parse_func(line):
    res = {}
    for sub in key_value_line.split(","):
        x = sub.split('=', 1)
        res[x[0]] = x[1]

    global parsed_results

    parsed_results = {'Bytes': {
        'Received': res['rcv']
    },
        'Destination': {
            'IP': res['dst'],
            'Port': res['dpt']
    },
        'Event': {
            'Category': res['cat'],  'Info': res['info']
    },
        'EventSource': {
            'ID': res['esid'], 'Name': res['esname'], 'Group': res['es_group']
    },
        'Policy': {
            'ID': '86'
    },
        'Service': {
            'Name': res['proto']
    },
        'Session': {
            'ID': res['sid']
    },
        'Source': {
            'IP': res['src'], 'Port': res['spt'], 'UserName': 'HULYA.OZASLAN'
    },
        'Time': {
            'Generated': res['date']
    },
        'URL': {
            'BaseDomain': res['url']
    },
        'Virtual': {
            'Domain': res['vdom'], 'DataType': 'log'
    }}
    return parsed_results
