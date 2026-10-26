text="HELLO WORLD"
shift=1
result=[]
for char in text:
    word=chr(ord(char)+shift)
    result+=word
print(result)