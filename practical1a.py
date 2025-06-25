import random
import time

Number_of_elements = 10000

list_1 = list(range(Number_of_elements))
random.shuffle(list_1)

set_1 = set(list_1)

start_time = time.time()
for i in range(Number_of_elements):
    i in set_1

end_time = time.time()
run_time = int((end_time - start_time) * 1000)
print("To test if", Number_of_elements, "elements are in the set")
print("--> The runtime is", run_time, "milliseconds")

#-----------------------------------------------------------------------------------

start_time = time.time()
for i in range(Number_of_elements):
    i in list_1

end_time = time.time()
run_time = int((end_time - start_time) * 1000)
print("\nTo test if", Number_of_elements, "elements are in the list")
print("--> The runtime is", run_time, "milliseconds")

#-----------------------------------------------------------------------------------

start_time = time.time()
for i in range(Number_of_elements):
    set_1.remove(i)

end_time = time.time()
run_time = int((end_time - start_time) * 1000)
print("\nTo remove", Number_of_elements, "elements are in the set")
print("--> The runtime is", run_time, "milliseconds")

#-----------------------------------------------------------------------------------

start_time = time.time()
for i in range(Number_of_elements):
    list_1.remove(i)

end_time = time.time()
run_time = int((end_time - start_time) * 1000)
print("\nTo remove", Number_of_elements, "elements are in the set")
print("--> The runtime is", run_time, "milliseconds")
