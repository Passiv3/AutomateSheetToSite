# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import openpyxl.utils.exceptions as openpyxl_exceptions
from selenium import webdriver
from openpyxl import load_workbook

driver = webdriver.Chrome()


def entrypoint():
    print("Enter the name of the mileage sheet. Don't forget the .xlsx extension: ")
    file_name = input()
    wb = read_file(file_name)
    if wb is None:
        print("read_file failed, exiting program...")
    else:
        pass


def read_file(name):
    try:
        wb = load_workbook(filename=name)
        print("File loaded successfully")
        return wb
    except FileNotFoundError:
        print("File not found")
        return None
    except openpyxl_exceptions.InvalidFileException:
        print("Incorrect Format")
        return None
    #finally:
     #   return None

def parse_for_data(workbook, worksheet_number):
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    entrypoint()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
