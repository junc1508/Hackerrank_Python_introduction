#Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
if __name__ == '__main__':
    s = input()
    for method in [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]:
        print(any(method(c) for c in s))
