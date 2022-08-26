
f=open("nameslist.txt","r+")
# for line in open("nameslist.txt"):
    # print(line)

x=f.readlines()[6]
# print(x[4])
# f.read(5)
y=f.read(6)
print(y)
f.close()
darth=0
lea=0
luke=0
f=open("nameslist.txt")
while True:
    line=f.readline()
    if (line==darth):
        darth+=1
    if (line==lea):
        darth+=1
    if (line==luke):
        darth+=1
    elif (not line):
        break
print(f"luke:{luke},lea:{lea},darth:{darth}")
        
# f.read(5)
# f.close()