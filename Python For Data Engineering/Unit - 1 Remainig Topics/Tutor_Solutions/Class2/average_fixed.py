marks = [60, 70, 80]
total = 0

for mark in marks:
    total += mark  # fix: accumulate

average = total / len(marks)
print("Average:", average)
