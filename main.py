import os
import hashlib


def find_songs(directory):
    cur = os.listdir(directory)
    files = []
    for tmp in cur:
        item = os.path.join(directory, tmp)
        if os.path.isfile(item):
            files.append(item)
        else:
            files.extend(find_songs(item))
    return files


def get_file_hash(file):
    hashcode = hashlib.sha256()
    f = open(file, 'rb')
    while True:
        data = f.read()
        if not data:
            break
        hashcode.update(data)
    return hashcode


def find_dublicates(directory):
    files = find_songs(directory)
    hashes = {}
    for file in files:
        now = get_file_hash(file).hexdigest()
        if (hashes.get(now) == None):
            hashes[now] = file
        else:
            print(hashes.get(now) + " and " + file)


if __name__ == '__main__':
    directory = "C:\songs"
    find_dublicates(directory)
