js_string_line = '{"BytesReceived": 11257, "DestinationIP": "173.194.39.154", "DestinationPort": 80, "EventCategory": "webfilter", "EventInfo": "URL has been visited", "EventSourceID": "FG224B3907501199", "EventSourceName": "FHY", "EventSourceGroup": "N/A", "PolicyID": "86", "ServiceName": "http", "SessionID": "62551133", "SourceIP": "192.168.1.133", "SourcePort": 52906, "SourceUserName": "HULYA.OZASLAN", "TimeGenerated": "2013-03-15 15:59:21", "URLBaseDomain": "googlesyndication.com", "VirtualDomain": "root"}'

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
    }}


def parse_func(line):
    x = line.replace(": ", ", ")
    x=x.replace("\"","")
    x=x.replace("}","")
    x=x.replace("{","")
    js_string_list = x.split(", ")
    global parsed_results
    parsed_results = {
        'Bytes': {
            'Received': js_string_list[1]
        },
        'Destination': {
            'IP': js_string_list[3],
            'Port': js_string_list[5]
        },
        'Event': {
            'Category': js_string_list[7],
            'Info': js_string_list[9]
        },
        'EventSource': {
            'ID': js_string_list[11],
            'Name': js_string_list[13],
            'Group': js_string_list[15]
        },
        'Policy': {
            'ID': js_string_list[17]
        },
        'Service': {
            'Name': js_string_list[19]
        },
        'Session': {
            'ID': js_string_list[21]
        },
        'Source': {
            'IP': js_string_list[23],
            'Port': js_string_list[25],
            'UserName': js_string_list[27]
        },
        'Time': {
            'Generated': js_string_list[29]
        },
        'URL': {
            'BaseDomain': js_string_list[31]
        },
        'Virtual': {
            'Domain': js_string_list[33],
            'DataType':'log'
        }}
    
    return parsed_results