def loading(some_number):
    if some_number == 100:
        return f"{some_number}% Complete!\n[%%%%%%%%%%]"
    return f"{some_number}% [{'%' * (some_number // 10)}{'.' * (10 - (some_number // 10))}]\nStill loading..."

number = int(input())
res = loading(number)
print(res)


