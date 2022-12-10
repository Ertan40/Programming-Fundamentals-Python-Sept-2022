numbers = list(map(lambda x: int(x), input().split(", ")))
found_indices_or__no = map(lambda x: x if numbers[x] % 2 == 0 else "no", range(len(numbers)))
even_indices = list(filter(lambda a: a != "no", found_indices_or__no))
print(even_indices)

# numbers = input().split(", ")   # ['3', '2', '1', '5', '8']
# indexes_of_event_nums = []
#
# for idx in numbers:
#     if int(idx) % 2 == 0:
#         finds_idx = numbers.index(idx)
#         indexes_of_event_nums.append(finds_idx)
# print(indexes_of_event_nums)