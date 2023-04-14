#!/usr/bin/env python
# -*- coding: utf-8 -*-
import PyPDF2
import docx

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
pdf_text = extract_text_from_pdf('file_pdf/hello.pdf')

# テキストをWordファイルに書き込む
doc = docx.Document()
doc.add_paragraph(pdf_text)
doc.save('file_docx/hello.docx')