"""
This script is created to check for various input is valid or invalid with support of RegEx
@Hasan Özdemir 01/19/2022
"""

from re import match
from helper_regex import HelperRegex
from dir_constants.project_constants import LOG_PATH


class RegexOperations(HelperRegex):

    def __init__(self) -> None:
        HelperRegex.__init__(self)

    def is_valid_mail(self, email_address: str) -> bool:
        """
        This method is created to check email is valid nor invalid
        :param email_address: <str> email address to check is valid nor invalid
        :return: <bool> Valid or Invalid
        """
        # Verify that there is an @ symbol with something before it
        email_pattern = r"^(.+)(\@)(\w+)(\.)(\w{3,4})$"
        email_address = str(email_address)
        if match(email_pattern, email_address):
            return True
        else:
            return False

    def is_valid_username(self, username: str) -> bool:
        """
        This method is created to check username is valid nor invalid
        :param username: <str> username to check is valid nor invalid
        :return: <bool> Valid or Invalid
        """
        # A string between 3 and 20 characters, allowing alphanumeric characters and hyphens and underscores
        username_pattern = r"^[a-zA-Z0-9_-]{3,20}$"
        if match(username_pattern, username):
            return True
        else:
            return False

    def is__valid_name_surname(self, name: str, surname: str) -> bool:
        """
        This method is created to check name and surname are valid nor invalid
        :param name: <str> name to check is valid nor invalid
        :param surname: <str> surname to check is valid nor invalid
        :return: <bool> Valid or Invalid
        """
        # A string between 3 and 20 characters, allowing only characters
        name_surname_pattern = r"^[a-zA-Z]{3,20}$"
        if match(name_surname_pattern, name) and match(name_surname_pattern, surname):
            return True
        else:
            return False

    def is_valid_username_email(self, username: str, mail: str) -> bool:
        """
        This method is created to check username whether is a part of mail or not 
        :param username: <str> username 
        :param mail : <str> user email
        :return : <bool> Valid or Invalid
        """
        # # create substring with username
        # -> min 3 character must match
        sub_username = [username[:i + 3] for i in range(len(username) - 3)]
        # Ex : johndoe@xyz.com
        # johndoe: username xyz : domain
        # take username from email
        email_username = mail[:mail.index('@')]
        if any([True if item in email_username else False for item in sub_username]):
            return True
        else:
            return False

    def is_valid_namesurname_username(self, name: str, surname: str, username: str) -> bool:
        """
        This method is created to check name or surname whether is a part of username or not 
        :param name: <str> name 
        :param surname: <str> surname 
        :param username : <str> user username
        :return : <bool> Valid or Invalid
        """
        # create substring with name & surname
        # -> min 4 character must match
        sub_name = [name[i:i + 4] for i in range(len(name) - 4)]
        sub_surname = [surname[i:i + 4] for i in range(len(surname) - 4)]
        # check any part of substring is passing in username
        if (any([True if item in username else False for item in sub_name])) or (
                any([True if item in username else False for item in sub_surname])):
            return True
        else:
            return False

    def is_valid_birth_year(self, birth_year: str) -> bool:
        """
        This method is created to check year whether is valid or not
        :param birth_year: <str> Year of birth 
        :return : <bool> Valid or Invalid
        """
        try:
            # check is digit
            birth_year = int(birth_year)
            # check whether is logical nor not
            if 1900 <= birth_year <= 2022:
                return True
            return False
        except ValueError as type_err:
            # log error
            self.error_log(str(type_err))

    def is_valid_birth_month(self, birth_month: str) -> bool:
        """
        This method is created to check month whether is valid or not
        :param birth_month: <str> Year of month 
        :return : <bool> Valid or Invalid
        """
        try:
            # check is digit
            birth_month = int(birth_month)
            # check whether is logical nor not
            if 1 <= birth_month <= 12:
                return True
            return False
        except ValueError as type_err:
            # log error
            self.error_log(str(type_err))

    def is_valid_birthday(self, birth_year: str, birth_month: str, birthday: str) -> bool:
        """
        This method is created to check birthday whether is valid or not
        :param birth_year: <str> Year of birth 
        :param birth_month: <str> Year of month 
        :param birthday: <str> Year of day
        :return : <bool> Valid or Invalid
        """
        try:
            day_of_month: dict = {1: 31, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
            # if leap year assign February 29 days
            if self.is_leap_year(birth_year):
                day_of_month[2] = 29
            # if not leap year assign February 28 days
            else:
                day_of_month[2] = 28
            birthday = int(birthday)
            if 0 < birthday <= day_of_month[int(birth_month)]:
                return True
            else:
                return False
        except Exception as type_err:
            # log error
            self.error_log(str(type_err))


if __name__ == '__main__':
    regex_obj = RegexOperations()
    # todo method testing TBD
    regex_obj.is_valid_birth_year("asa")
