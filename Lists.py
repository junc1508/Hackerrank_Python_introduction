#Consider a list (list = []). You can perform the following commands:
#insert i e: Insert integer  at position .
#print: Print the list.
#remove e: Delete the first occurrence of integer .
#append e: Insert integer  at the end of the list.
#sort: Sort the list.
#pop: Pop the last element from the list.
#reverse: Reverse the list.
#Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.



if __name__ == '__main__':
    n = int(input())
    l = []
    for _ in range(n):
        s = input().split()
        cmd = s[0]
        if cmd == 'insert':
            l.insert(int(s[1]),int(s[2]))
        elif cmd == 'remove':
            l.remove(int(s[1]))
        elif cmd == 'append':
            l.append(int(s[1]))
        elif cmd == 'sort':
            l.sort()
        elif cmd == 'pop':
            l.pop()
        elif cmd == 'reverse':
            l.reverse()
        elif cmd == 'print':
            print(l)
        
        
or
n = input()
l = []
for _ in range(n):
    s = input().split()
    cmd = s[0]
    args = s[1:]
    if cmd !="print":
        cmd += "("+ ",".join(args) +")"   #cmd(args[1],(args[2]))
        eval("l."+cmd)
    else:
        print l
