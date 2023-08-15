# -*- coding: utf-8 -*-
import openpyxl
import unicodedata

def from_excel_to_dict(file_path='../data/76.xlsx', sheet_name=u'Лист1'):
    wb = openpyxl.load_workbook(file_path)
    sheet = wb[sheet_name]
    data_dict = {}
    total_list = []
    worker_list=['Кожурин Сергей Сергеевич', 'Емелькин Василий Анатольевич', 'Афонин Алексей Геннадьевич', 'Шляпников Гурий Александрович']

    for row in sheet.iter_rows(min_row=9, values_only=True):  # Assuming the first row contains column headers
        worker = str(row[11])
        normolize_worker=unicodedata.normalize('NFC', worker)
        if normolize_worker in worker_list:
            if normolize_worker not in data_dict:
                data_dict[normolize_worker]=[{'date':row[4], 'pp':row[3], 'sum':row[5], 'consumer':row[6], 'contract':row[7], 'comment':row[12]}]
            else:
                data_dict[normolize_worker].extend([{'date':row[4], 'pp':row[3], 'sum':row[5], 'consumer':row[6], 'contract':row[7], 'comment':row[12]}])
    return data_dict
from_excel_to_dict()
