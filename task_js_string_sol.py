import json
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
    js_dict=(json.loads(line))
    global parsed_results
    parsed_results = {
        'Bytes': {
            'Received': js_dict['BytesReceived']
        },
        'Destination': {
            'IP': js_dict['DestinationIP'],
            'Port': js_dict['DestinationPort']
        },
        'Event': {
            'Category': js_dict['EventCategory'],
            'Info': js_dict['EventInfo']
        },
        'EventSource': {
            'ID': js_dict['EventSourceID'],
            'Name': js_dict['EventSourceName'],
            'Group': js_dict['EventSourceGroup']
        },
        'Policy': {
            'ID': js_dict['PolicyID']
        },
        'Service': {
            'Name': js_dict['ServiceName']
        },
        'Session': {
            'ID': js_dict['SessionID']
        },
        'Source': {
            'IP': js_dict['SourceIP'],
            'Port': js_dict['SourcePort'],
            'UserName': js_dict['SourceUserName']
        },
        'Time': {
            'Generated': js_dict['TimeGenerated']
        },
        'URL': {
            'BaseDomain': js_dict['URLBaseDomain']
        },
        'Virtual': {
            'Domain': js_dict['VirtualDomain'],
            'DataType': 'log'
        }}
    return parsed_results
