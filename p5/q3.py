a_i = 0.05
m_i = a_i / 12

base = float(input("Enter the monthly saving amount: "))

total = base * (1 + m_i)
total = (base + total) * (1 + m_i)
total = (base + total) * (1 + m_i)
total = (base + total) * (1 + m_i)
total = (base + total) * (1 + m_i)
total = (base + total) * (1 + m_i)

print("After the sixth month, the account value is" , total)
print("After the sixth month, the account value is" , (round(total,2)))  

