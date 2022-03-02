# f=open("pqr.txt")
# # s=f.read()
# # print(s)
# # for i in s:
# #     print(i)
# # print(f.read(21),end='')
# # print(f.readline())
# lines=f.readlines()
# for line in lines:
#     print(line,end='')
# print(len(lines))
# f.close()
with open("pqr.txt") as f:
    lines=f.readlines()
    for line in lines:
        print(line)
    print("File closed : ",f.closed)
print("File Closed[outside with] : ",f.closed)