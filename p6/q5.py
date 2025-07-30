scores = []

while True:
    number = input("Enter the number of students: ")
    
    if number.isdigit():
        number = int(number)
        if number == 0:
            print("Only number is allowed! \n")
            continue
        else:
            count = 1
            scores = []
            print("\n Enter the {:s}.".format("studemts scores" if number > 1 else "students score"))
            while count <= number:
                match(count % 10):
                    case 1:
                        suffix = "st"
                    case 2:
                        suffix = "nd"
                    case 3:
                        suffix = "rd"
                    case _:
                        suffix = "th"
                message = "{:>3s}{} student: ".format(str(count),suffix)
                
                try:
                    score = float(input(message))
                    if score < 0:
                        print("Only zero or positive value is allowed! \n")
                    else:
                        scores.append(score)
                        count += 1
                except ValueError:
                    print("Only number is allowed!")
            if count > number :
                break
    else:
        print("Only positive integer is allowed!")
        
scores.sort(reverse = True)

print("\n The Highest Scores               :{:.0f}%".format(scores[0]))
print("\n The Second Highest Scores        :{:.2f}%".format(scores[0]))
print("\n The Average Scores               :{:.2f}%".format(sum(scores)/len(scores)))