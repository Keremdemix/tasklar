import re



csv_line = '2013-03-15 15:59:21,FHY,FG224B3907501199,N/A,192.168.1.133,52906,173.194.39.154,80,root,11257,http,googlesyndication.com,62551133,URL has been visited,webfilter'

key_value_line = 'date=2013-03-15 15:59:21,esname=FHY,esid=FG224B3907501199,es_group=N/A,src=192.168.1.133,spt=52906,dst=173.194.39.154,dpt=80,vdom=root,rcv=11257,proto=http,url=googlesyndication.com,sid=62551133,info=URL has been visited,cat=webfilter'

js_string_line = '{"BytesReceived": 11257, "DestinationIP": "173.194.39.154", "DestinationPort": 80, "EventCategory": "webfilter", "EventInfo": "URL has been visited", "EventSourceID": "FG224B3907501199", "EventSourceName": "FHY", "EventSourceGroup": "N/A", "PolicyID": "86", "ServiceName": "http", "SessionID": "62551133", "SourceIP": "192.168.1.133", "SourcePort": 52906, "SourceUserName": "HULYA.OZASLAN", "TimeGenerated": "2013-03-15 15:59:21", "URLBaseDomain": "googlesyndication.com", "VirtualDomain": "root"}'


parsed_result = {
  'Bytes': {
    'Received': '11257'
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
    'Group':'N/A'  
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
    'Domain': 'root'
  },
  'DataType': {
    'log'
  }
}




parsed_result2={
  'Bytes':{
    'Received':re.findall('\d+',csv_line)[18]
  },
  'Destination':{
    'IP':re.findall('\d{3}\D\d{3}\D\d{2}\D\d{3}',csv_line)[0],
    'Port':re.findall('\d{2}',csv_line)[22]
  },
  'Event':{
    'Category':re.findall(r'N/A|\w+' ,csv_line)[29],
    'Info':re.findall('URL has\D+ed',csv_line)[0]
  },
  'EventSource':{
    'ID':re.findall('\w{16}', csv_line)[0],
    'Name':re.findall('[A-Z]{3}',csv_line)[0],
    'Group':re.findall(r'N/A|\w+',csv_line)[8]
  },
  'Policy': {
    'ID': '86'
  },
  'Service':{
    'Name':re.findall('\w+',csv_line)[22]
  },
  'Session':{
    'ID':re.findall('\d{8}',csv_line)[1]
  },
  'Source': {
    'IP':re.findall('\d{3}\D\d{3}\D\d\D\d{3}',csv_line)[0] ,
    'Port':re.findall('(6553[0-5]|655[0-2]\d|65[0-4]\d\d|6[0-4]\d{3}|5\d{4}|49[2-9]\d\d|491[6-9]\d|4915[2-9])',csv_line)[1] ,
    'UserName':'HULYA.OZASLAN'
  },
  'Time': {
    'Generated': re.findall('\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}',csv_line)[0]
  },
  'URL': {
    'BaseDomain':re.findall('\w+\.\w+' ,csv_line)[4]
  },
  'Virtual': {
    'Domain':re.findall('\w+',csv_line)[20]
  },
   'DataType': {
    'log'
  }
} 
