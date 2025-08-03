import re
import zipfile

regex = r"Next nothing is (\d+)"
non_matching_files = []

with zipfile.ZipFile("channel.zip", 'r') as zip_ref:
    file_list = zip_ref.namelist()

    for filename in file_list:
        with zip_ref.open(filename) as file:
            content = file.read().decode('utf-8')
            if not re.search(regex, content):
                non_matching_files.append(content)
    


with zipfile.ZipFile("channel.zip", "r") as zip_ref:
    first_file = zip_ref.read("90052.txt").decode('utf-8')
    match = re.search(regex, first_file).group(1)

    while True:
        file = zip_ref.read(f"{match}.txt").decode('utf-8')
        match = re.search(regex, file)
        if match:
            match = match.group(1)
            comment = zip_ref.getinfo(f"{match}.txt").comment.decode('utf-8')
            print(comment, end="")
        else:
            break
