def count(string, search_char):
    char_count = 0
    for letter in string:
        if letter == search_char:
            char_count = char_count + 1
    return (char_count)

print(count('fredrick', 'f'))
print(count('freedrick', 'e'))