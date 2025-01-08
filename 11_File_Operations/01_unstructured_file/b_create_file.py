fh = open("b_second_file.txt", mode="w", encoding="utf-8")

print("Name of the file : ", fh.name)
print("Opening mode     : ", fh.mode)


fh.write("This is first line\n")
fh.write("This is second line\n")
fh.flush()

print("Closed or not    : ", fh.closed)
fh.close()  # garbage collector
print("Closed or not    : ", fh.closed)

try:
    fh.write("This is third line\n")
except ValueError as ve:
    print(ve)
    print("can not do operations(read/write) on closed file")


gh = open("b_second_file.txt", mode="w", encoding="utf-8")
gh.write("This is third line\n")

gh.flush()
gh.close()

mh = open("b_second_file.txt", mode="a")
mh.write("This is fourth line\n")

mh.flush()
mh.close()

f = open("b_second_file.txt", "a")
f.truncate(25)
f.close()

f = open("b_second_file.txt", "r")
print(f.read())