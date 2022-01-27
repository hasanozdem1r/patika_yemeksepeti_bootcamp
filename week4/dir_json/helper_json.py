"""
This script is created to manage helper methods
@Hasan Özdemir 01/21/2022
"""

from argparse import ArgumentParser
from sys import argv
from dir_logging.project_logging import ProjectLogging

class HelperJson(ProjectLogging):

    def __init__(self,log_file):
        super(HelperJson, self).__init__(log_file=log_file)
        # initialize Argument parser
        parser=ArgumentParser()
        # prepare named arguments
        parser.add_argument('--file',help='Json file path',type=str)
        parser.add_argument('--db',help='Database file path',type=str)
        # get the named command line arguments
        self.json_path=parser.parse_args().file
        self.db_path=parser.parse_args().db

    def fetch_dict(self,item)->list:
        """
        This method used to fetch each item of dir_json file
        :param item: <dict> Each item of dir_json
        """
        try:
            id=item['id']
            username=item['username']
            p_name=item['profile']['name']
            p_dob=item['profile']['dob']
            p_address=item['profile']['address']
            p_l_lat=item['profile']['location']['lat']
            p_l_long=item['profile']['location']['long']
            api_key=item['apiKey']
            # return fetched item as list
            return [id,username,p_name,p_dob,p_address,p_l_lat,p_l_long,api_key]
        except KeyError as error:
            # TODO 
            pass