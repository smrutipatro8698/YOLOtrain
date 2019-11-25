import os

dirname = 
for i, filename in enumerate(os.listdir(dirname)):
    os.rename(dirname + "/" + filename, dirname + "/" + str(i) + ".bmp")