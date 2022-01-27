"""
This script is created to prepare ProjectLogging class for further logging needs.
@ Hasan Özdemir 01/23/2022
"""
import logging
import logging.handlers
from dir_constants.project_constants import LOG_PATH


class ProjectLogging:

    def __init__(self, log_file: str) -> None:
        """
        This constructor is created to initialize logger object and format the log output
        :param log_file: <str> path of log file to write
        """
        super(ProjectLogging,self).__init__()
        # format the output
        self.log_format = "LEVEL : %(levelname)s || DATE_TIME : %(asctime)s || CODE_LINE : " \
                          "%(lineno)d || MESSAGE : %(message)s"
        # default settings for each logging level
        logging.basicConfig(filename=log_file,
                            filemode="a",
                            format=self.log_format)
        # create logger object
        self.log_obj = logging.getLogger()

    # CRITICAL LEVEL 50
    def critical_log(self, error_msg: str) -> str:
        """
        This method is created to log critical level of logs when it's raised
        :param error_msg: <str> Error message
        :return: None
        """
        self.log_obj.setLevel(logging.CRITICAL)
        self.log_obj.critical(error_msg)
        return 'CRITICAL'

    # ERROR LEVEL 40
    def error_log(self, error_msg: str) -> str:
        """
        This method is created to log error level of logs when it's raised
        :param error_msg: <str> Error message
        :return: None
        """
        self.log_obj.setLevel(logging.ERROR)
        self.log_obj.error(error_msg)
        return 'ERROR'

    # INFO LEVEL 20
    def info_log(self, info_msg: str) -> str:
        """
        This method is created to log info level of logs when it's successfully done
        :param info_msg: <str> Error message
        :return: None
        """
        self.log_obj.setLevel(logging.INFO)
        self.log_obj.info(info_msg)
        return 'INFO'


if __name__ == '__main__':
    log_obj = ProjectLogging(LOG_PATH)
    # test info log
    log_obj.info_log('I am INFO')
    # test critical log
    log_obj.critical_log('I am CRITICAL')
    # test error log
    log_obj.error_log('I am ERROR')
