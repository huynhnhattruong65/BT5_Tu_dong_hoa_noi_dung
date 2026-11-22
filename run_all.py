"""Bấm Run Python File trong VS Code để tạo cả PDF và PPTX."""
from src.csv_to_pdf import build
from src.text_to_slides import make
if __name__=='__main__':
    build()
    make()
    print('\nHOÀN THÀNH! Mở thư mục results/ để lấy PDF, PPTX và PNG.')
