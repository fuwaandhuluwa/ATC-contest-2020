# encoding=utf-8
# read file list from special path

import os
import re


# return the full qualify name of files in the special path
def getFileList(path: str = 'C:/Users/jiafu.li/PyCharmProjects/AStar_Algorithm/testcase', extension: str = ""):
    # sub directory
    dir_list = []

    # all files
    file_list = []

    files = os.listdir(path)
    for f in files:
        file_qualify_name = path + '/' + f
        if os.path.isdir(file_qualify_name):
            # 排除隐藏文件夹
            if f[0] == '.':
                pass
            else:
                # 添加文件夹
                dir_list.append(f)

        pattern = re.compile(extension)
        if os.path.isfile(file_qualify_name) and pattern.search(file_qualify_name):
            file_list.append(file_qualify_name)

    return file_list


def readFileContent(file: str):
    print("File Name: {}".format(file))
    content_list = []
    with open(file, 'r') as f:
        for line in f.readlines():
            line = line.split('\n')  # remove 换行符
            content_list.append(line[0])
    return content_list


# file_list = getFileList(extension='.in')
#
# for content in readFileContent(file_list[0]):
#     print(content)
