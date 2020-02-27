#You are given an integer, . Your task is to print an alphabet rangoli of size . (Rangoli is a form of Indian folk art based on creation of patterns.)

#Different sizes of alphabet rangoli are shown below:
#size 3

#----c----
#--c-b-c--
#c-b-a-b-c
#--c-b-c--
#----c----

#size 5

#--------e--------
#------e-d-e------
#----e-d-c-d-e----
#--e-d-c-b-c-d-e--
#e-d-c-b-a-b-c-d-e
#--e-d-c-b-c-d-e--
#----e-d-c-d-e----
#------e-d-e------
#--------e--------

#The center of the rangoli has the first alphabet letter a, and the boundary has the  alphabet letter (in alphabetical order).
#First loop, range (0,n)
#     --c--
#     -cbc-
#     cbabc
#then add '-' bewteen each element with join()
#Second loop, range (n-1,0,-1) count down to make the calculation easier
#     -cbc-
#     --c--
#then add '-' bewteen each element with join()



def print_rangoli(size):
    # your code goes here
    import string
    mid = size - 1
    for i in range(size - 1, 0, -1):
        row = ['-'] * (2 * n - 1)
        for j in range(size - i):
            row[mid - j] = row[mid + j] = string.ascii_lowercase[j + i]
        print ('-'.join(row))

    for i in range(0, size):
        row = ['-'] * (2 * size - 1)
        for j in range(0, size - i):
            row[mid - j] = row[mid + j] = string.ascii_lowercase[j + i]
        print ('-'.join(row))
    

