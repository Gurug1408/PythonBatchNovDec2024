"""
Purpose: Demonstration of usage of help()
on python objects
"""
# NOTE: help() usage differs only for string objects

dozen = 18 
dozen = 18.5  
dozen = 18.6  

dozen = None  
dozen = True 

print(f"{type(dozen) =}")
print(f"{id(dozen)  =}")
print(f"{dozen      =}")

print(f"{dir(dozen) =}")

help(dozen)



print("=" * 40)
mountain = "Himalayas"  
print(f"{type(mountain) =}")
print(f"{id(mountain)   =}")
print(f"{mountain       =}")

print(f"{dir(mountain) =}")

help(mountain)
help(str)
help(mountain.isalpha)
