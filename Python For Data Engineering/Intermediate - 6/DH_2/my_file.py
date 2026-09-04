# Open Function Arguments - Buffering in File Handling
f = open("Hello.txt", "r", buffering = 10, encoding = "utf-8")
if f:
    print("Opend file ", f.name)

print(f)