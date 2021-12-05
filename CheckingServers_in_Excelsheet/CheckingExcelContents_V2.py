# This is a working to find a string in an excel workbook and print its row and columns nos
from xlrd import open_workbook

book_name = 'Azure_Unattached_Disk_Drives_October.xlsx'
# book_name = 'Azure_Rightsizing_November_V2.xlsx'
# book_name = 'Azure_Rightsizing_November.xlsx'
book = open_workbook(book_name)
print(book)

# with open('Servers_list.txt') as f:
with open('Strings.txt') as f:
    file_contents_list = [line.rstrip('\n') for line in f]
print(file_contents_list)
        
def Checking_for_string(string_in_excelsheet,string_in_text_file,sheet_name,book_name):
    # if string_in_excelsheet == string_in_text_file:
    if string_in_excelsheet in string_in_text_file:
        # print(string_in_text_file)
        # value = sheet.cell(rowidx, colidx)
        # print(value)
        # print('True')
        print(string_in_excelsheet+' is present in the sheet: '+sheet.name +' at row: '+str(rowidx)+' and column: '+str(col) +' in book: '+book_name)
 
    
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
            #print('String in excel: '+str(string_in_excelsheet))
            for string_in_text_file in file_contents_list:
                # print(type(string_in_excelsheet))
                # print('String in text file: '+str(string_in_text_file))
                if len(cell_value) < 1:
                    print('Empty cell') 
                elif cell.value is None:
                    print('None')
                else:
                    # print('Str val') 
                    string_in_text_file_upper = str(string_in_text_file).upper()
                    string_in_excelsheet_upper = str(string_in_excelsheet).upper()
                    # print('String in text file: '+str(string_in_text_file_upper))
                    # print('String in excel: '+str(string_in_excelsheet_upper))
                    Checking_for_string(string_in_excelsheet_upper,string_in_text_file_upper,sheet_name,book_name)
