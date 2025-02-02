def contarChar(string, c):
    if not string:
        return 0
    elif string[0] == c:
        return 1 + contarChar(string[1:], c)
    return contarChar(string[1:], c)

print(contarChar("banana", "a"))