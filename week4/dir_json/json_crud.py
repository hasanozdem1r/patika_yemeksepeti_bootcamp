"""
This script is created make CRUD operations on dir_json files.
@Hasan Özdemir 01/18/2022
"""
from json import load
from helper_json import HelperJson

from dir_constants.project_constants import LOG_PATH, JSON_PATH


class JsonCrud(HelperJson):

    def __init__(self,log_file:str) -> None:
        """
        This constructor is used to initialize json_data list object
        """
        super(JsonCrud,self).__init__(log_file=log_file)
        self.json_data: list = list()

    def read_json(self, json_path: str) -> list:
        """
        This method is used to read data from dir_json files
        :param json_path: <str> path of dir_json file to read
        :return: <list> data fetched from given dir_json file
        """
        try:
            with open(json_path) as json_file:
                json_data = load(json_file)
                # loop through dir_json items
                for item in json_data:
                    # check the key is that existed
                    if item['id'] and item['email'] and item['username'] and item['profile']['name'] and \
                            item['profile']['dob'] and item['profile']['address'] and item["apiKey"]\
                            and item['profile']['location']['lat'] and item['profile']['location']['long']:
                        # fetch all field from dir_json separately
                        data_seperated = self.fetch_dict(item)
                        # append to list
                        self.json_data.append(data_seperated)
                        # context manager, close the file automatically but let's make it sure for closing file
                json_file.close()
            # log process successfully done
            self.info_log('Data fetched successfully')
            # return fetched data
            return self.json_data

        # if file is not found log to projects_logs.log file
        except FileNotFoundError as file_error:
            # file not found error raised
            self.error_log(str(file_error))
            # return null list
            return []

        except KeyError as key_error:
            # key error raised
            self.error_log(str(key_error))
            # return null list
            return []


if __name__ == '__main__':
    j_obj = JsonCrud(log_file=LOG_PATH)
    # Test Info Log
    j_obj.read_json(JSON_PATH)
    # Test File Not Found Log
    j_obj.read_json('hasan.xyz')
