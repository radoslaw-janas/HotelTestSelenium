import xlrd

from page_object_pattern.utils.search_data import searchData


class ExcelReader:
    @staticmethod
    def get_data():
#Using data from excel file for tests
        wb = xlrd.open_workbook("../utils/Dane.xlsx")
        sheet = wb.sheet_by_index(0)
        data =[]
        for i in range(1,sheet.nrows):
            search_data = searchData(sheet.cell(i,0).value,sheet.cell(i,1).value)
            data.append(search_data)
        return data