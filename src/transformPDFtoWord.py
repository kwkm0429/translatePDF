#!/usr/bin/env python
# -*- coding: utf-8 -*-
import PyPDF2
import docx
import sys

args = sys.argv

# PDFファイルからテキストを抽出する関数
def extract_text_from_pdf(pdf_path):
    pdf_file = open(pdf_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ''
    for page in range(len(pdf_reader.pages)):
        page_obj = pdf_reader.pages[page]
        text += page_obj.extract_text()
    pdf_file.close()
    return text

# PDFファイルからテキストを抽出する
pdf_text = extract_text_from_pdf('file_pdf/'+args[1]+'.pdf')

# テキストをWordファイルに書き込む
doc = docx.Document()
doc.add_paragraph(pdf_text)
doc.save('file_docx/'+args[1]+'.docx')