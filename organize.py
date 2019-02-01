import os

def OrganizeFiles():
    for file in os.listdir():
        filename = os.fsdecode(file)
        print(filename)
OrganizeFiles()