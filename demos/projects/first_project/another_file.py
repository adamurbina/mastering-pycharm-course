from sys import argv
import bs4


def my_test(string1, string2):
    print(f"hello {string1} and {string2}")


print(type(bs4))

my_test(argv[1], argv[2])

