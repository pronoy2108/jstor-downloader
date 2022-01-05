#!/usr/bin/python3
import os
import re
from glob import glob
from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter


def key_func(afilename):
    nondigits = re.compile("\D")
    return int(nondigits.sub("", afilename))


def merge_pdf(title):
    file_names = []
    for x in sorted(glob('./temp/*.pdf'), key=key_func):
        file_names.append(x)
    
    merger = PdfFileMerger()
    
    for filename in file_names:
        merger.append(fileobj=PdfFileReader(open(filename, 'rb')), pages=(1, PdfFileReader(open(filename, 'rb')).getNumPages()))
    merger.write("./books/" + title + ".pdf")
    for i in file_names:
        os.remove(i)


if __name__ == "__main__":
    merge_pdf(input("Document title: "))
