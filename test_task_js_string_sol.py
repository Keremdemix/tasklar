import unittest
import task_js_string_sol

class Test_csv_match (unittest.TestCase):
    def test_csv_parsed_results(self):
        task_js_string_sol.parse_func(task_js_string_sol.js_string_line)
        self.assertEqual(
            task_js_string_sol.parsed_results['Bytes']['Received'], '11257')
        self.assertEqual(
            task_js_string_sol.parsed_results['Destination']['Port'], '80')
        self.assertEqual(
            task_js_string_sol.parsed_results['Destination']['IP'], '173.194.39.154')
        self.assertEqual(
            task_js_string_sol.parsed_results['Event']['Category'], 'webfilter')
        self.assertEqual(
            task_js_string_sol.parsed_results['Event']['Info'], 'URL has been visited')
        self.assertEqual(
            task_js_string_sol.parsed_results['EventSource']['ID'], 'FG224B3907501199')
        self.assertEqual(
            task_js_string_sol.parsed_results['EventSource']['Name'], 'FHY')
        self.assertEqual(
            task_js_string_sol.parsed_results['EventSource']['Group'], 'N/A')
        self.assertEqual(
            task_js_string_sol.parsed_results['Policy']['ID'], '86')
        self.assertEqual(
            task_js_string_sol.parsed_results['Service']['Name'], 'http')
        self.assertEqual(
            task_js_string_sol.parsed_results['Session']['ID'], '62551133')
        self.assertEqual(
            task_js_string_sol.parsed_results['Source']['IP'], '192.168.1.133')
        self.assertEqual(
            task_js_string_sol.parsed_results['Source']['Port'], '52906')
        self.assertEqual(
            task_js_string_sol.parsed_results['Source']['UserName'], 'HULYA.OZASLAN')
        self.assertEqual(
            task_js_string_sol.parsed_results['Time']['Generated'], '2013-03-15 15:59:21')
        self.assertEqual(
            task_js_string_sol.parsed_results['URL']['BaseDomain'], 'googlesyndication.com')
        self.assertEqual(
            task_js_string_sol.parsed_results['Virtual']['Domain'], 'root')
        self.assertEqual(
            task_js_string_sol.parsed_results['Virtual']['DataType'], 'log')

if __name__ == '__main__':
     unittest.main()
