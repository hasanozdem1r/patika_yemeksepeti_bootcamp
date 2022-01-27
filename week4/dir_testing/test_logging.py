"""
This script is created to test logging classes functionality
@ Hasan Özdemir 01/23/2022
"""

from unittest import TestCase
from dir_constants.project_constants import LOG_PATH
from dir_logging.project_logging import ProjectLogging

class TestLogging(TestCase):

    def test_info_log(self):
        """
        Test functionality of method
        :return: None
        """
        test_obj=ProjectLogging(LOG_PATH)
        self.assertEqual(test_obj.info_log('hasan'),'INFO')

    def test_error_log(self):
        """
        Test functionality of method
        :return: None
        """
        test_obj=ProjectLogging(LOG_PATH)
        self.assertEqual(test_obj.error_log('hasan'),'ERROR')

    def test_critical_log(self):
        """
        Test functionality of method
        :return: None
        """
        test_obj=ProjectLogging(LOG_PATH)
        self.assertEqual(test_obj.critical_log('hasan'),'CRITICAL')
