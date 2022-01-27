"""
This script is created to execute program. 
@Hasan Özdemir 01/21/2022
"""
from dir_json.json_crud import JsonCrud
from dir_regex.regex_operations import RegexOperations
from dir_database.db_operations import Database
from dir_constants.project_constants import LOG_PATH

def run_project():
    db_obj=Database()
    reg_obj=RegexOperations()
    js_obj=JsonCrud(log_file=LOG_PATH)

    # create table
    created_table_name: str = db_obj.create_automatic_table()
    # fetch data
    fetched_data=js_obj.read_json(json_path=js_obj.json_path)
    for data in fetched_data:
        db_obj.push_data_to_db(db_obj.create_table_str(table_name=created_table_name),data=data)

if __name__=='__main__':
    run_project()