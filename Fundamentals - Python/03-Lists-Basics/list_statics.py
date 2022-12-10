n = int(input())
positives = []
negatives = []
count_of_positives = 0
sum_of_negatives = 0
for current_number in range(n):
     current_number = int(input())
     if current_number >= 0:
         positives.append(current_number)
         count_of_positives += 1
     else:
         negatives.append(current_number)
         sum_of_negatives += current_number
print(positives)
print(negatives)
print(f"Count of positives: {count_of_positives} \nSum of negatives: {sum_of_negatives}")
