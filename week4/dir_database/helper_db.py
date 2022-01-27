"""
This script is created to manage helper methods
@Hasan Özdemir 01/21/2022
"""

from datetime import datetime
from argparse import ArgumentParser
from dir_logging.project_logging import ProjectLogging
from dir_constants.project_constants import LOG_PATH

class HelperDb(ProjectLogging):

    def __init__(self,log_file:str) -> None:
        """
        This constructor is created to get named command line args and initialize parent constructor
        return : None
        """
        # initialize logger obj
        super(HelperDb,self).__init__(log_file=LOG_PATH)

        #ProjectLogging.__init__(self,log_file=log_file)

        # initialize Argument parser
        parser = ArgumentParser()
        # prepare named arguments
        try:
            parser.add_argument('--file', help='Json file path', type=str,default=None)
            parser.add_argument('--db', help='Database file path', type=str,default=None)
            # get the named command line arguments
            self.json_path = parser.parse_args().file
            self.db_path = parser.parse_args().db
        except Exception as general_err:
            self.error_log(str(general_err))

    def time_formatting(self) -> str:
        """
        This method is created to format datetime for yyyy_dd_mm format
        :return: <str> formatted datetime
        """
        now = datetime.now()
        date_time = str(now.strftime("%Y_%d_%m"))
        return date_time

    def create_table_str(self, table_name: str) -> str:
        """
        This method is created to provide create table sql dialect
        :param table_name: <str> table name
        :return: <str> table sql dialect
        """
        # create table dialect
        create_table_str = (f"\n"
                            f"        CREATE TABLE IF NOT EXISTS {table_name}(\n"
                            f"         id int primary key(id),\n"
                            f"         username varchar(25) not null,\n"
                            f"         p_name varchar(25) not null,\n"
                            f"         p_b_year varchar(25) not null,\n"
                            f"         p_b_month varchar(25) not null,\n"
                            f"         p_b_day varchar(25) not null,\n"
                            f"         p_address varchar(150) not null,\n"
                            f"         p_l_lat varchar(25) not null\n"
                            f"         p_l_long varchar(25) not null,\n"
                            f"         api_key varchar(100) not null\n"
                            f"        )\n"
                            f"        ")
        return create_table_str

    def push_data_str(self,table_name:str)->str:
        """
        This method is created to provide insert data sql dialect
        :return: <str> sql dialect
        """
        push_str= (f"INSERT INTO {table_name } (id,username,p_name,p_b_year,p_b_month,\n"
                   f"                    p_b_day,p_address,p_l_lat,p_l_long,api_key) \n"
                   f"                    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ")
        return push_str

if __name__ == '__main__':
    # CASE : python helper_db.py
    # CASE_2 : python helper_db.py --file hasan.db --db hasan.db
    help_obj = HelperDb(log_file=LOG_PATH)
    # Test time_formatting
    print(help_obj.time_formatting())
    # Test connection_str
    print(help_obj.create_table_str('hasan'))