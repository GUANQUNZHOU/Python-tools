from pdf2docx import Converter


def convert_pdf_to_word_in_page_range(pdf_path: str, docx_path: str, start_page: int, end_page: int):
    cv = Converter(pdf_path)
    cv.convert(docx_path, start=start_page, end=end_page)
    cv.close()


def convert_pdf_to_word(pdf_path: str, docx_path: str):
    cv = Converter(pdf_path)
    cv.convert(docx_path)
    cv.close()


if __name__ == "__main__":
    is_page_set = int(input("是否选定页数范围，1.yes，2.no， 请输入数字: "))
    # path of pdf need to be converted
    input_pdf = str(input("请输入input pdf 的路径: "))
    # path of converted output
    out_word = str(input("请输入output word 的路径: "))

    if is_page_set == 1:
        start = int(input("请输入起始页数"))
        end = int(input("请输入截止页数"))
        convert_pdf_to_word_in_page_range(input_pdf, out_word, start, end)
    else:
        convert_pdf_to_word(input_pdf, out_word)
    print("Selected pages of the PDF file have been converted to Word successfully!")
