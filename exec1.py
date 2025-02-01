def reverseString(string):
    if len(string) == 0:
        return ""
    else: return reverseString(string[1:]) + string[0]

result = reverseString("MinhaString")
print(result)

