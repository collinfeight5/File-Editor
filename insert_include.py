import os
first_line = "#include \"stdafx.h\" \n"

file_path = "C:\KanziWorkspace_3_6_3_2514\Projects\digital-display-main\Application\src\plugin\src"


def add_new_line(root, files):

    for file in files:
        full_path = os.path.join(root, file)
        if '.cpp' in file:
            with open(full_path, "r") as src:
                oline = src.readlines()
                oline.insert(0, first_line)

            with open(full_path, "w") as src:
                src.writelines(oline)


for root, dirs, files in os.walk(file_path):
    add_new_line(root, files)








