import os
from setuptools import setup


def read(f_name):
    return open(os.path.join(os.path.dirname(__file__), f_name)).read()

setup(
    name = "Yemeksepeti_4th_Week_Project",
    version = "0.0.1",
    author = "Hasan Özdemir",
    author_email = "hasann.ozdemirr58@gmail.com",
    description = "YemekSepeti Bootcamp 4th Week Project",
    license = "MIT",
    keywords = "python regex sqlite",
    url = "https://github.com/Yemeksepeti-Python-Bootcamp/pythonfiletool_regex_json_hasan_ozdemir",
    packages=['dir_constants', 'dir_data','dir_database','dir_json','dir_logging','dir_regex','dir_testing'],
    long_description=read('README.md'),
    classifiers=[
        "Topic :: YemekSepeti Bootcamp",
        "License :: OSI Approved :: MIT License",
    ],
)