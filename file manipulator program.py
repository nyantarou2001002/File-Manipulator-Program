l = input("Please input your command referencing README.md: ").split()
ordername = l[0]
inputpath = l[1]

def contents(pathname):
    with open(pathname) as f:
        contents = f.read()
    return contents

if ordername == "reverse" and len(l) == 3:
    result1 = contents(inputpath)[::-1]
    with open(l[2], 'w') as f:
        f.write(result1)

elif ordername == "copy" and len(l) == 3:
    result2 = contents(inputpath)
    with open(l[2], "w") as f:
        f.write(result2)

elif ordername == "deplicate-contents" and len(l) == 3:
    result3 = contents(inputpath)
    with open(inputpath, "a") as f:
        for i in range(int(l[2])):
            f.write(result3)

elif ordername == "replace-string" and len(l) == 4:
    result4 = contents(inputpath)
    with open(inputpath, "w") as f:
        f.write(result4.replace("needle", "newstring"))

else:
    print("Error!! Please input your command in the right way referencing README.md")
 




