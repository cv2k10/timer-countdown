import unittest
from unittest.mock import patch, mock_open
import timer1

class TestTimerFunctions(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data='{"timer_value": 10}')
    def test_load_config(self, mock_file):
        """
        Test the `load_config` function of the `timer1` module.

        This test case mocks the `open` function to simulate reading a JSON file. It verifies that the `load_config` function
        returns the expected value by asserting that `timer1.load_config()` returns `10`. Additionally, it checks that
        the `open` function is called with the correct arguments by asserting that `mock_file.assert_called_with('config.json', 'r')`
        is `True`.

        Parameters:
        - `self` (TestTimerFunctions): The current test case instance.
        - `mock_file` (MagicMock): A mock object that simulates the behavior of the `open` function.

        Returns:
        - None
        """
        self.assertEqual(timer1.load_config(), 10)
        mock_file.assert_called_with('config.json', 'r')

    @patch('time.sleep', return_value=None)
    @patch('timer1.system_beep', return_value=None)
    @patch('builtins.print')
    def test_countdown_timer(self, mock_print, mock_beep, mock_sleep):
        """
        Test the countdown_timer function from the timer1 module.

        This test function mocks the time.sleep, timer1.system_beep, and builtins.print functions to test the countdown_timer function.
        It calls the countdown_timer function with a timer value of 5 seconds and the system_beep function as the beep_function parameter.
        It asserts that the mock_print function is called 6 times (5 countdown prints + 1 finished print) and that the mock_beep function is called once.

        Parameters:
            self (TestTimerFunctions): The test case instance.
            mock_print (MagicMock): The mock object for the builtins.print function.
            mock_beep (MagicMock): The mock object for the timer1.system_beep function.
            mock_sleep (MagicMock): The mock object for the time.sleep function.

        Returns:
            None
        """
        timer1.countdown_timer(5, timer1.system_beep)
        self.assertEqual(mock_print.call_count, 6)  # 5 countdown prints + 1 finished print
        mock_beep.assert_called_once()

    @patch('os.system')
    def test_system_beep(self, mock_os_system):
        """
        Test the system_beep function from the timer1 module.

        This test function mocks the os.system function to validate that system_beep calls os.system with the correct arguments.

        Parameters:
            self (TestTimerFunctions): The test case instance.
            mock_os_system (MagicMock): The mock object for the os.system function.

        Returns:
            None
        """
        timer1.system_beep()
        mock_os_system.assert_called_with('afplay /System/Library/Sounds/Ping.aiff')

if __name__ == '__main__':
    unittest.main()
