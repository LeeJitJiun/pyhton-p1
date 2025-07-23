message = input("Enter a string: ").strip()

words = message.split()

acronym = ""

for word in words:
    acronym += word[0].upper()

print("The acronym for {} is {}".format(message.strip(),acronym))