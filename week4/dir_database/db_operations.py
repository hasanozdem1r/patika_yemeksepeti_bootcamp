"""
This script is created to manage dir_database opeations
@Hasan Özdemir 01/21/2022
"""

import sqlite3 as sql
from contextlib import contextmanager
from helper_db import HelperDb

class Database(HelperDb):

    def __init__(self) -> None:
        # inherit from HelperDb class
        super(Database,self).__init__()
        #HelperDb.__init__(self,log_file=LOG_PATH)
        # inherit from JsonCrud class
        #JsonCrud.__init__(self,log_file=LOG_PATH)

    # if you want to test in further you can use this built-in method
    def __str__(self) -> list:
        return [self.json_path,self.db_path]

    @contextmanager
    def connect_database(self,database:str)->bool:
        """
        This method created to connect to database with context manager decorator
        :param database: <str> path of database
        :return: <bool> True or False
        """
        #instantiate connection obj __init__ method
        connect_obj=None

        connect_obj=sql.connect(
            database=database
        )
        try:
            # connect to database __enter__ method
            yield connect_obj
            self.info_log('Database connection successful')
            return True
        except Exception as connection_err:
            # rollback chances
            connect_obj.rollback()
            self.critical_log(str(connection_err))
            return False
        finally:
            # close connection __exit__ method
            connect_obj.close()
            self.info_log('Database connection closed')

    def create_automatic_table(self)->str:
        """
        This method created to create automatic table with context manager decorator
        :return: <str> table name
        """
        table_name=f"customer_{self.time_formatting()}"
        create_table_dialect=self.create_table_str(table_name=table_name)

        with self.connect_database(database=self.db_path) as connection:
            db_cursor=connection.cursor()
            db_cursor.execute(create_table_dialect)
        self.info_log('Database successfully created')
        return table_name

    def push_data_to_db(self,table_name:str,data:list):
        # fetched data from json
        if len(data)==8:
            data=tuple(data)
            insert_query:str=self.push_data_str(table_name=table_name)
            with self.connect_database(database=self.db_path) as connection:
                db_cursor=connection.cursor()
                db_cursor.execute(insert_query,data)
                connection.commit()
                db_cursor.close()
        else:
            self.error_log('Table field is missing')
if __name__=='__main__':
    db_object=Database()
    #print(db_object.__str__())
    db_object.create_automatic_table()


# how to run 
# open cmd in current project folder
# test_case1: python main.py --file hasan.db --db hasan.db
# test_case2: python main.py --file hasan1.db --db hasan1.db