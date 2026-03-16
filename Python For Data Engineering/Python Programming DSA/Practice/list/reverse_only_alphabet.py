text = "jz8634jjramk24jecy"
alpha_list = [ele for ele in text if ele.isalpha()][::-1]
output = []
count = 0
for ele in text:
    if ele.isalpha():
        output.append(alpha_list[count])
        count += 1
    else:
        output += ele
print("".join(output))
