#!/usr/bin/env python
# -*- coding: utf-8 -*-
import docx
import re

# Word文書のパスを受け取り、テキストを読み込んで返す
def read_word_text(filepath):
    doc = docx.Document(filepath)
    text = ''
    for para in doc.paragraphs:
        text += para.text
    return text

# 改行自動削除、ハイフンで区切られた英単語を連結する関数
def remove_newlines_and_join_hyphenated_words(text):
    # 改行を削除する
    text = text.replace('\n', ' ')
    # ハイフンで区切られた英単語を連結する
    text = re.sub(r'([a-zA-Z]+)-\s?([a-zA-Z]+)', r'\1\2', text)
    return text

# 与えられた文字列を最大5000文字の長さで改行する
def break_lines(text):
    max_length = 5000
    lines = []
    line = ''
    words = text.split()

    for word in words:
        if len(line) + len(word) > max_length and line[-1] == '.':
            lines.append(line)
            line = ''
        line += word + ' '
    lines.append(line)

    return '\n'.join(lines)

word_text = read_word_text('file_docx/hello.docx')
word_text = remove_newlines_and_join_hyphenated_words(word_text)
word_text = break_lines(word_text)

# テキストをWordファイルに書き込む
doc = docx.Document()
doc.add_paragraph(word_text)
doc.save('file_docx/hello.docx')