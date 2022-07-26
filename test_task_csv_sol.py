import unittest
import task_csv_sol



class Test_csv_match (unittest.TestCase):
    
  def test_csv_bytes_match (self):
    self.assertEqual(task_csv_sol.parsed_result2['Bytes'],task_csv_sol.parsed_result['Bytes'])

  def test_csv_Destination_match (self):
    self.assertEqual(task_csv_sol.parsed_result2['Destination'],task_csv_sol.parsed_result['Destination'])

  def test_csv_Event_match (self):
    self.assertEqual(task_csv_sol.parsed_result2['Event'],task_csv_sol.parsed_result['Event'])
  
  def test_csv_EventSource_match (self):
    self.assertEqual(task_csv_sol.parsed_result2['EventSource'],task_csv_sol.parsed_result['EventSource'])

  def test_csv_Policy_match (self):
    self.assertEqual(task_csv_sol.parsed_result2['Policy'],task_csv_sol.parsed_result['Policy'])

  def test_csv_Service_match (self):
    self.assertEqual(task_csv_sol.parsed_result2['Service'],task_csv_sol.parsed_result['Service'])

  def test_csv_Session_match (self):
    self.assertEqual(task_csv_sol.parsed_result2['Session'],task_csv_sol.parsed_result['Session'])

  def test_csv_Source_match (self):
    self.assertEqual(task_csv_sol.parsed_result2['Source'],task_csv_sol.parsed_result['Source'])

  def test_csv_Time_match (self):
    self.assertEqual(task_csv_sol.parsed_result2['Time'],task_csv_sol.parsed_result['Time'])

  def test_csv_URL_match (self):
    self.assertEqual(task_csv_sol.parsed_result2['URL'],task_csv_sol.parsed_result['URL'])

  def test_csv_Virtual_match (self):
    self.assertEqual(task_csv_sol.parsed_result2['Virtual'],task_csv_sol.parsed_result['Virtual'])

  def test_csv_DataType_match (self):
    self.assertEqual(task_csv_sol.parsed_result2['DataType'],task_csv_sol.parsed_result['DataType'])


if __name__=='__main__':
  unittest.main()