message = input("Enter a string: ").strip()

words = message.split()

print("\nNo of words: ", len(words))

vowel = "aeiou"

message = message.lower()

print()

for character in vowel:
    print("No of {}:{:d}".format(character, message.count(character)))
    
total = 0

for word in words:
    total =+ len(word)
    
    print("\n Average: {:.2f}".foramt(total/len(words)))