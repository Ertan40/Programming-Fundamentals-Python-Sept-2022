targets = input().split()
shot_targets = []
targets_as_digit = [int(item) for item in targets] # 24 50 36 70
# targets = list(map(lambda x: int(x), input().split(' ')))
command = input()
while command != "End":
    current_index = int(command)
    if len(targets) > current_index and current_index not in shot_targets:
        original_target = targets_as_digit[current_index]
        targets_as_digit[current_index] = -1
        shot_targets.append(current_index)
        for index in targets_as_digit:
            if index != -1:
                t_index = targets_as_digit.index(index)
                print(t_index)
                if index > original_target:
                    targets_as_digit[t_index] -= original_target
                else:
                    targets_as_digit[t_index] += original_target

    command = input()
format_print = " ".join([str(item) for item in targets_as_digit])
# format_print = ' '.join(list(map(lambda x: str(x), targets_as_digit)))
print(f"Shot targets: {len(shot_targets)} -> {format_print}")





# targets = list(map(lambda x: int(x), input().split(' ')))
# command = input()
# shot_targets = []
#
# while command != 'End':
#     idx = int(command)  # target to be shot
#
#     if idx < len(targets) and idx not in shot_targets:
#         original_target = targets[idx]
#         targets[idx] = -1             # shoot a target
#         shot_targets.append(idx)
#
#         for t in targets:
#             if t != -1:                   # make sure you don't update values of shot targets
#                 t_idx = targets.index(t)  # remember index to update
#                 if t > original_target:
#                     targets[t_idx] -= original_target
#                 else:
#                     targets[t_idx] += original_target
#
#     command = input()
# format_print = ' '.join(list(map(lambda x: str(x), targets)))
# print(f"Shot targets: {len(shot_targets)} -> {format_print}")