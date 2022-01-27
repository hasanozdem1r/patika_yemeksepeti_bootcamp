"""
This script is created to test HelperDb class.
@ Hasan Özdemir 01/23/2022
"""

from unittest import TestCase
from dir_database.helper_db import HelperDb

class TestDbHelper(TestCase,HelperDb):

    def test_output_type_test_formatting(self)->None:
        """
        This method test the return type of time_formatting method
        :return: None
        """
        output_type=type(self.time_formatting())
        return self.assertEqual(output_type,str)


    def test_output_type_push_data(self)->None:
        """
        This method test the return type of connection_str method
        :return: None
        """
        output_type=type(self.connection_str(table_name='table_name'))
        return self.assertEqual(output_type,str)

    def test_output_type_push_data_str(self)->None:
        """
        This method test the return type of push_data_str method
        :return: None
        """
        output_type=type(self.push_data_str())
        return self.assertEqual(output_type,str)
