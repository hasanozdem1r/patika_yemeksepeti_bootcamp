"""
This script created to apply CRUD operations on CSV files.
Hasan Özdemir 2021
"""

from csv import reader,DictReader,writer
from os import path

class FileOperations(object):
    
    def __init__(self,file_path:str,fields:list=None) -> None:
        """
        This is a FileInitialize class constructor and created to initialize important methods.
        """
        self.path=file_path
        self.fields=fields
        # seperate file name and extension
        self.file_name,self.file_extension=path.splitext(file_path)

    # tested for different csv files and it's works well.
    def read_data(self):
        """
        This method is used to read all data from csv files.
        """
        # read csv file
        if str(self.file_extension)=='.csv':
            # open csv data in read mood
            # always better to use context manager for file operations.
            with open(self.path, newline='', mode="r") as csv_file:
                csv_data = reader(csv_file, delimiter=';', quotechar='|')
                # print line by line
                for row in csv_data:
                    print(row)
        # read txt file
        elif str(self.file_extension)=='.txt':
            with  open(self.path,mode="r",encoding="utf-8") as file:
                for line in file:
                    print(line,end='')
        # other types
        else:
            print('Other data types is not supported for current version.')
    

    def search_data(self,search_text:str,row_number:int=0):
        """
        This method is used to search in csv file and return the all data if there is match
        """
        # read data
        csv_data = reader(open(self.path,mode="r",encoding="utf-8"),delimiter=' ', quotechar='|')
        # search and print if data is found
        for row in csv_data:
            print(type(row))
            break
            if row[row_number]==search_text:
                print(row)



def select_operation():
    while True:
        print('To show all data enter 1, to search data enter 2, to update data enter 3, to delete data enter 4, to exit from program enter 5')
        selection=int(input())
        if selection==1:
            # show all data
            pass
        elif selection==2:
            # search data
            pass
        elif selection==3:
            # update data
            pass
        elif selection==4:
            # delete data
            pass
        elif selection==5:
            # exit from terminal and stop loop
            break
        else:
            continue

if __name__=='__main__':
    file_obj=FileOperations('hasan.csv',[1,'Hasan','Özdemir','Computer Engineering'])
    #file_obj.read_data()
    file_obj.search_data('raspberry,Rubus',0)
    #file_obj.convert_csv_to_json('hasan1.csv')