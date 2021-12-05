# This is a working to find a string in an excel workbook and write the row into a new file
from xlrd import open_workbook
import xlsxwriter

# book_name = 'Azure_Unattached_Disk_Drives_October.xlsx'
# book_name = 'Azure_Rightsizing_November.xlsx'
# book_name = 'Azure_Rightsizing_November_V2.xlsx'
# book_name = 'SSR_Test.xlsx'
book_name = 'AWS_Unused_or_Underutilized_Resource_Cleanup.xlsx'
book = open_workbook(book_name)
data_found_in_excel = []

with open('String_to_search.txt') as f:
# with open('SSR_test.txt') as f:
# with open('Test_file.txt') as f:
    file_contents_list = [line.rstrip('\n') for line in f]
print('Searching strings')
print(file_contents_list)
        
def Checking_for_string(string_in_excelsheet,string_in_text_file,sheet_name,book_name):
    if string_in_text_file in string_in_excelsheet:
        # value = sheet.cell(rowidx, colidx)
        # print(value)
        # print(string_in_text_file+' is present in the sheet: '+sheet.name +' at row: '+str(rowidx)+' and column: '+str(col) +' in book: '+book_name)
        data_found_in_excel.append(sheet.row_values(rowidx)) 
        # print(sheet.row_values(rowidx))
    return data_found_in_excel
 
    
for sheet in book.sheets():
    for rowidx in range(sheet.nrows):
        row = sheet.row(rowidx)
        sheet_name = sheet.name
        # print(sheet_name)
        # print(rowidx)
        for colidx, cell in enumerate(row):
            # print(colidx)
            col = colidx
            cell_value = str([cell.value])+'ss'
            #print(str(cell_value)+'SS')
            string_in_excelsheet = cell.value
            # print('String in excel: '+str(string_in_excelsheet))
            for string_in_text_file in file_contents_list:
                # print('String in text file: '+str(string_in_text_file))
                if len(cell_value) < 1:
                    print('Empty cell') 
                else:
                    # print('Str val') 
                    string_in_text_file_upper = str(string_in_text_file).upper()
                    string_in_excelsheet_upper = str(string_in_excelsheet).upper()
                    # print('String in text file: '+str(string_in_text_file_upper))
                    # print('String in excel: '+str(string_in_excelsheet_upper))
                    data_found_in_excel_to_newfile = Checking_for_string(string_in_excelsheet_upper,string_in_text_file_upper,sheet_name,book_name)

print('Strings found are: ')
print(data_found_in_excel_to_newfile)

new_book_name = 'Rentals_in_'+book_name
with xlsxwriter.Workbook(new_book_name) as workbook:
    worksheet = workbook.add_worksheet()
    for row_num, data in enumerate(data_found_in_excel_to_newfile):
        worksheet.write_row(row_num, 0, data)