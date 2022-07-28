csv_line = '2013-03-15 15:59:21,FHY,FG224B3907501199,N/A,192.168.1.133,52906,173.194.39.154,80,root,11257,http,googlesyndication.com,62551133,URL has been visited,webfilter'

key_value_line = 'date=2013-03-15 15:59:21,esname=FHY,esid=FG224B3907501199,es_group=N/A,src=192.168.1.133,spt=52906,dst=173.194.39.154,dpt=80,vdom=root,rcv=11257,proto=http,url=googlesyndication.com,sid=62551133,info=URL has been visited,cat=webfilter'

js_string_line = '{"BytesReceived": 11257, "DestinationIP": "173.194.39.154", "DestinationPort": 80, "EventCategory": "webfilter", "EventInfo": "URL has been visited", "EventSourceID": "FG224B3907501199", "EventSourceName": "FHY", "EventSourceGroup": "N/A", "PolicyID": "86", "ServiceName": "http", "SessionID": "62551133", "SourceIP": "192.168.1.133", "SourcePort": 52906, "SourceUserName": "HULYA.OZASLAN", "TimeGenerated": "2013-03-15 15:59:21", "URLBaseDomain": "googlesyndication.com", "VirtualDomain": "root"}'


parsed_result = {
    'Bytes': {
        'Received': 11257
    },
    'Destination': {
        'IP': '173.194.39.154',
        'Port': '80'
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
        'Port': '52906',
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
    }}


def parse_func(text):
    csv_list = text.split(",")
    global parsed_results
    parsed_results = {
        'Bytes': {
            'Received': csv_list[9]
        },
        'Destination': {
            'IP': csv_list[6], 'Port': csv_list[7]
        },
        'Event': {
            'Category': csv_list[14],  'Info': csv_list[13]
        },
        'EventSource': {
            'ID': csv_list[2], 'Name': csv_list[1], 'Group': csv_list[3]
        },
        'Policy': {
            'ID': '86'
        },
        'Service': {
            'Name': csv_list[10]
        },
        'Session': {
            'ID': csv_list[12]
        },
        'Source': {
            'IP': csv_list[4], 'Port': csv_list[5], 'UserName': 'HULYA.OZASLAN'
        },
        'Time': {
            'Generated': csv_list[0]
        },
        'URL': {
            'BaseDomain': csv_list[11]
        },
        'Virtual': {
            'Domain': csv_list[8], 'DataType': 'log'
        }}
    return parsed_results
