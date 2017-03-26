import os

def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def write_file(path,data):
    f = open(path,'a')
    f.write(data)
    f.close()

def reindent(string,char):
    string = '\n'.join([char + e for e in string.split('\n')])
    return string