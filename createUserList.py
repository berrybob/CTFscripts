# A script used to generate certain surname & lastname patterns
import sys

wordlist = []

def __init__(self):
        pass

def mixNames(n: str, m: str):
    surname = n.lower()
    lastname = m.lower()
    print(lastname + surname[0])
    print(lastname + surname[0:3])
    print(lastname + "." + surname)
    print(surname + lastname[0])
    print(surname[0] + lastname)
    print(surname + lastname[0:3])
    print(surname + "." + lastname)



with open(sys.argv[1]) as f:
    for line in f:
        wordlist = line.split()
        mixNames(wordlist[0], wordlist[1])
