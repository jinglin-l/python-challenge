import re
import zipfile

regex = r"Next nothing is \d+"
non_matching_files = []

with zipfile.ZipFile("channel.zip", 'r') as zip_ref:
    file_list = zip_ref.namelist()

    for filename in file_list:
        with zip_ref.open(filename) as file:
            content = file.read().decode('utf-8')
            if not re.search(regex, content):
                non_matching_files.append(content)
    

print(non_matching_files)


with zipfile.ZipFile("channel.zip", "r") as zip_ref:
    for file_info in zip_ref.infolist():
        file_comment = file_info.comment.decode('utf-8')
        if file_comment and file_comment[0].isalpha():
            print(file_comment)