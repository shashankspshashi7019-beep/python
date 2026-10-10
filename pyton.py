table = str.maketrans("abc", "123")
text = "apple banana cat"
result = text.translate(table)
print(result)
