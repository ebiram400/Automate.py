from os import walk,rename

f=[]
for (dirpath, dirnames, filenames) in walk("./"):
    f.extend(filenames)

print(f)

j=1
for i in f:
    if j!=8:
        ch=str(j)+".jpg"
        rename(i , ch)
    j+=1
    