# open('file_name', 'mode')

# create file
# filename = "sample.txt"
# open(filename, 'w')
# open(filename, 'x')
# open(filename, 'a')


# file = open(filename, 'a')

# write data
# file.write("this is a example.txt file")
# file.close()
# file.write("i can not add after file closed.")
# lines = ['\nthis is a line - 6\n', 'this is a line - 7\n', 'this is a line - 8\n', 'this is a line - 9\n', 'this is a line - 10']
# file.writelines(lines)

# read data
# print(file.read())
# print(file.read(8))
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readlines())

# file.close()

import os

# os.system('type nul > test1.pdf')
# os.system('type nul > test1.xlsx')
# os.system('type nul > test1.jpg')
# os.system('type nul > test1.png')
# os.system('type nul > test1.csv')


# os.system('notepad')
# os.system('date')

# os.remove('test1.jpg')
# os.rename('test1.pdf', 'brijesh.pdf')
# os.system('mkdir test')
# os.removedirs('test')
# os.system('type nul > test/example.yml')

# import uuid
# for file_number in range(1, 11):
#     filename = f'test/example_{uuid.uuid4()}.txt'
#     os.system(f'type nul > {filename}')