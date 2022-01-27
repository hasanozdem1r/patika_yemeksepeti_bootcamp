"""
This script is created to test is_leap_year method
@Hasan Özdemir 01/22/2022
"""
from dir_regex.helper_regex import HelperRegex

def test_leap_year(year:str)->None:
    """
    This method is created to test leap year method
    :param year: <str> year
    :return: None
    """
    """
    Checks leap year
    >>> HelperRegex.is_leap_year(self=None,year=2012)
    True
    >>> HelperRegex.is_leap_year(self=None,year=1988)
    True
    >>> HelperRegex.is_leap_year(self=None,year=2000)
    True
    >>> HelperRegex.is_leap_year(self=None,year=2021)
    False
    >>> HelperRegex.is_leap_year(self=None,year=2024)
    True
    """


if __name__=='__main__':
    from doctest import testmod
    testmod()
