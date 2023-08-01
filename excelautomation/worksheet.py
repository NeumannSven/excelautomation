'''
Created on 01.08.2023

@author: neumann
'''

import openpyxl


if __name__ == '__main__':
    wb = openpyxl.Workbook()
    
    ws = wb['Sheet']
    ws["A1"] = 123

    
    wb.save('test.xlsx')
    
