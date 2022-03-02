lcount=wcount=ccount=0
with open("pqr.txt") as f:
    lines=f.readlines()
    lcount=len(lines)
    for line in lines:
        ccount=ccount+len(line)
        wcount=wcount+len(line.split())
print("Line count : ",lcount)
print("word count : ",wcount)
print("char count : ",ccount)