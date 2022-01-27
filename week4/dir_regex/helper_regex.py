"""
This script is created to manage helper methods
@Hasan Özdemir 01/21/2022
"""

from dir_constants.project_constants import LOG_PATH
from dir_logging.project_logging import ProjectLogging


class HelperRegex(ProjectLogging):

    def __init__(self) -> None:
        """
        This method is created to initialize parent class methods
        return : None
        """
        ProjectLogging.__init__(self, log_file=LOG_PATH)

    def is_leap_year(self, year: str) -> bool:
        """
        This method is created to check year whether is leap nor not leap
        :param year: <int> year
        :return: <bool> Leap  or Not Leap
        """
        try:
            year = int(year)
            if (year % 400 == 0) and (year % 100 == 0) and year:
                return True
            elif (year % 4 == 0) and (year % 100 != 0):
                return True
            else:
                return False
        except ValueError as value_err:
            self.error_log(error_msg=str(value_err))
            return False


if __name__ == '__main__':
    try:
        # object initialization
        regex_obj = HelperRegex()
        # method calling
        regex_obj.is_leap_year('100')
    except Exception as error:
        log_obj = ProjectLogging(LOG_PATH)
        log_obj.error_log(error_msg=str(error))
