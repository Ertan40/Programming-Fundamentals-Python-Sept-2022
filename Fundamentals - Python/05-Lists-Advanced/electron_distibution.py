electrons = int(input())
shell_list = []
last_electron = []
n_counter = 1
while True:
    max_in_shell = 2 * (n_counter ** 2)
    if electrons <= max_in_shell:
        break
    electrons -= max_in_shell
    shell_list.append(max_in_shell)
    last_electron.append(electrons)
    n_counter += 1
final_electron = last_electron[-1]
shell_list.append(final_electron)
print(shell_list)





