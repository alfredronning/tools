from os import listdir
from os.path import isfile, join
path = "/home/alfr/tools"
filenames = [f for f in listdir(path) if isfile(join(path, f))]
print("\n".join(filename[:-3] for filename in filenames))
