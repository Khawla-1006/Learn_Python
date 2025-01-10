w = int(input("Width: "))
h = int(input("Height: "))

# i = 0 
# output = ""
# while i < w : 
#     output += "#"
#     i += 1 
# print(output)


#or simply : rectangle of hashes
j = 1
for j in range(1, h):
    print("#"* w) 
print("#" * w)