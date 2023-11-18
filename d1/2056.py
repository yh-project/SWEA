T = int(input())

for i in range(T):
    print(f"#{i+1}", end=" ")
    calender = input()
    year = calender[:4]
    month = calender[4:6]
    day = calender[6:]

    if int(month) not in range(1, 13) or int(day) > [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][int(month)-1]:
        print(-1)
    else: print(f"{year}/{month}/{day}")