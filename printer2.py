n = int(input("작업 수 : "))
m = int(input("작업 번호 : "))
priority = list(map(int, input("작업 우선순위 : ").split()))
priority_list = list(range(len(priority)))
T = 0

while True:
    
    if priority[0] == max(priority):
        T = T + 1

        if priority_list[0] != m:
            priority_list.pop(0)
            priority.pop(0)

        elif priority_list[0] == m:
            print(T, "분")
            break
    else:
        priority.append(priority[0])
        priority.pop(0)
        priority_list.append(priority_list[0])
        priority_list.pop(0)
