from calcthread import CalcThread
from threading import Barrier

precision = int(input("Enter the precision (number of terms): "))

terms = []
barrier = Barrier(precision)

print("Calculating the value of pi with", precision, "terms...")
for i in range(precision):
    thread = CalcThread(i, terms, barrier)
    thread.start()

sum = 0.0
for i in range(len(terms)):
    sum += terms[i]
print(sum)