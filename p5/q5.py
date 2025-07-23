isbn = input("Enter first 9 digits of an ISBN-10 as a string: ").strip()
number = int(isbn)
total = 0
counter = 9

while counter !=0:
    total += ((number % 10)* counter)
    counter -= 1
    number = number//10
checksum = total % 11

print("The ISBN-10 number is", isbn + (str(checksum) if checksum < 10 else "X"))