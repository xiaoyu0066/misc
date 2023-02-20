import os
from pdfminer.high_level import extract_text

# 定义要搜索的关键字
keywords = ["flag", "password"]

# 定义要搜索的目录
directory = r"C:\ctf\pdf\RKBtvX"

# 递归遍历目录下的所有PDF文件
def search_pdf_files(directory):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isdir(filepath):
            # 如果是子目录，则递归遍历子目录下的PDF文件
            search_pdf_files(filepath)
        elif filename.endswith(".pdf"):
            # 如果是PDF文件，则搜索文件中的关键字
            try:
                text = extract_text(filepath)
                for keyword in keywords:
                    if keyword in text:
                        print(f"文件 {filename} 中包含关键字: {keyword}")
                        break
            except:
                print(f"文件 {filename} 读取失败")

# 调用函数开始搜索
search_pdf_files(directory)
