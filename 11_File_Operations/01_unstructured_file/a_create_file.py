file_handler = open("a_first_file.txt", mode="w")
print(f"{type(file_handler) =}")  
print(f"{file_handler       =}")

print()

file_handler = open("a_first_file.txt", mode="w", encoding="utf-8")
print(f"{file_handler       =}")
print()

file_handler.write("This is the first line\n")
file_handler.write("This is the second line\n")

file_handler.close()