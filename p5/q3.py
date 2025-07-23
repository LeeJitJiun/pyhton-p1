a_i = 0.05
m_i = a_i / 12

base = 100
total = 0
repetition = 10
month = ""

print("{:10s}{:10s}".format("Month","Total"))

for count in range(repetition):
    total = (base + total) + (1 + m_i)
    
    match (count + 1) % 10: 
        case 1:
            month = str(count + 1) + "st"
        case 2:
            month = str(count + 1) + "nd"
        case 3:
            month = str(count + 1) + "rd"
        case _:
            month = str(count + 1) + "th" 
    print("{:10s} RM {:<10.2f}".format(month,total))