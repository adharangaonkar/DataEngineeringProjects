import numpy as np
# import pandas as pd
# import PyPDF2 as pypdf
# pdfobject=open('test1.pdf','rb')
# pdf=pypdf.PdfFileReader(pdfobject)
# text = pdf.getFormTextFields()
# a = pd.DataFrame.from_records(text, index=[0])
#
# def pdf_to_record():
#     pdfobject=open('test1.pdf','rb')
#     pdf=pypdf.PdfFileReader(pdfobject)
#     text = pdf.getFormTextFields()
#     a = pd.DataFrame.from_records(text, index=[0])
#     # filename = input()
#     pdfobject=open("test4.pdf" ,'rb')
#     pdf=pypdf.PdfFileReader(pdfobject)
#     text1 = pdf.getFormTextFields()
#     b = pd.DataFrame.from_records(text1, index=[1 + a.tail(1).index.item()])
#     a = a.append(b)
#     # a = pd.to_csv("data.csv")
#     return a
#
# print("Hello")