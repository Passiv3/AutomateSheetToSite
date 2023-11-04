import unittest
import main as openpyxl_section


class TestOpenPyXL(unittest.TestCase):
    file_name = "Unofficial_Mileage_Tracker.xlsx"
    sheet_name = "Mileage Sheet 1"

    openpyxl_section.read_file()
