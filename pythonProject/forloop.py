number = "9,223;372: 654,775;807"
separators = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char

print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])

# number = "9,223;372: 654"
# separators = ""
#
# for char in number:
#     if char.isnumeric():
#         separators = separators + char
#
# print(separators)