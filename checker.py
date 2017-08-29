import hashlib
from functools import partial

#Print a menu on screen 
def menu():
    print("****************************************************")
    print("*          Welcome to Hash Checker                 *")
    print("*         HASHES ARE CASE SENSITIVE                *")
    print("*     Vendor Hashes should be lower case           *")
    print("****************************************************")
    print("\n")
    print("Press 1 to change a lowercase hash to upper")
    print("Press 2 to change a uppercase hash to lower")
    print("Press 3 to Get the MD5 hash of a file and compare it")
    print("Press 4 to Get the SHA1 hash of a file and compare it")
    print("Press 5 to Get the SHA256 hash of a file and compare it")
    print("Press 6 to Exit")

#The check is case sensitive. This hashes created are in lowercase, the first 2 functions convert the case of the vendor has as required 	
def caseChangerUp():
    checkSumLow = input("Please eneter the checksum you wish to convert: ")
    checkSumUp = checkSumLow.upper()
    print("Take a copy of your hash: ", checkSumUp)
    input('Press Enter to Continue')

def caseChangerLow():
    checkSumUp = input("Please eneter the checksum you wish to convert: ")
    checkSumLow = checkSumUp.lower()
    print("Take a copy of your hash: ", checkSumLow)
    input('Press Enter to Continue')

#Function to read a file and Create an MD5 hash
def md5sum(filename):
    with open(filename, mode='rb') as f:
        d = hashlib.md5()
        for buf in iter(partial(f.read, 128), b''):
            d.update(buf)
    return d.hexdigest()
#Function to read a file and Create a SHA1 hash
def sha1sum(filename):
    with open(filename, mode='rb') as f:
        d = hashlib.sha1()
        for buf in iter(partial(f.read, 128), b''):
            d.update(buf)
    return d.hexdigest()

#Function to read a file and Create an SHA256 hash
def sha256sum(filename):
    with open(filename, mode='rb') as f:
        d = hashlib.sha256()
        for buf in iter(partial(f.read, 128), b''):
            d.update(buf)
    return d.hexdigest()

#Compare vendor hash to inputted hash
def SumChecker(hashsum):
    supplied = input('Please enter the sum supplied by the Vendor: ')
    print('Match' if (hashsum == supplied) else 'Not Matched')
    input('Press Enter to Continue')

menu()
choice = input("Make your Choice: ")
choice = int(choice)
if choice == 1:
    caseChangerUp()
if choice == 2:
    caseChangerLow()
if choice == 3:
    filename=input("name and location of file: ")
    hashsum = (md5sum(filename))
    print(md5sum(filename))
    SumChecker(hashsum)
if choice == 4:
    filename=input("name and location of file: ")
    hashsum = (sha1sum(filename))
    print(sha1sum(filename))
    SumChecker(hashsum)
if choice == 5:
    filename=input("name and location of file: ")
    hashsum =(sha256sum(filename))
    print(sha256sum(filename))
    SumChecker(hashsum)
if choice == 6:
    exit()

