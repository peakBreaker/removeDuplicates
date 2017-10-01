"A script to remove duplicated files using md5 hashes"

import hashlib
md5 = hashlib.md5

import os
import stat
import sys

Ignore = ('Thumbs.db',)

def getmd5(filename):
    "Get the MD5 hash of a file"
    m = md5()
    with open(filename, 'rb') as f:
        m.update(f.read(-1))
        return m.hexdigest()

def usage():
    "Prints instructions out to the console on how to use the program"
    print('Usage: remove-duplicates.py DIRECTORY')
    sys.exit(1)

def main(argv):
    "Main function for the program"
    if len(argv) < 1:
        usage()

    dir = os.path.abspath(argv[0])

    print('Reading sizes...')

    # Create a dictionary keyed by size, with each entry holding a list of
    # filenames of that size.

    data = {}
    
    for root, dirs, files in os.walk(dir):
        for name in files:
            if name in Ignore: continue
            path = os.path.join(root, name)
            size = os.path.getsize(path)
            if not size in data:
                data[size] = []

            data[size].append(path)

    # For each key, checksum each list entry and compare.

    removed = 0

    for k in data.keys():
        dk = data[k]
        if len(dk) > 1:
            #print k, len(dk)
            s = {}
            for j in dk:
                sum = getmd5(j)
                if sum in s:
                    #print(j, 'is a dupe of', s[sum])
                    try:
                        os.remove(j)
                        removed += 1
                    except:
                        pass
                else:
                    s[sum] = j

    print('Done, %d files removed.' % (removed))

if __name__ == '__main__':
    main(sys.argv[1:])
