import unittest
import excel_task

class Test_csv_match (unittest.TestCase):
    def test_csv_dest(self):
        excel_task.new_func()
        self.assertEqual(
            excel_task.dest['103001']["Context"], 'VPN')
        self.assertEqual(    
            excel_task.dest['103001']["SubType"], 'Error')
        self.assertEqual(    
            excel_task.dest['103001']["Type"], 'IPSec')
        self.assertEqual(
            excel_task.dest['103002']["Context"], 'VPN')
        self.assertEqual(    
            excel_task.dest['103002']["SubType"], 'Error')
        self.assertEqual(    
            excel_task.dest['103002']["Type"], 'IPSec')
        self.assertEqual(
            excel_task.dest['103003']["Context"], 'VPN')
        self.assertEqual(    
            excel_task.dest['103003']["SubType"], 'Error')
        self.assertEqual(    
            excel_task.dest['103003']["Type"], 'IPSec')       
        self.assertEqual(
            excel_task.dest['103004']["Context"], 'VPN')
        self.assertEqual(    
            excel_task.dest['103004']["SubType"], 'Error')
        self.assertEqual(    
            excel_task.dest['103004']["Type"], 'IPSec') 

if __name__ == '__main__':
    unittest.main()
