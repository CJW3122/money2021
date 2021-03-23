#아래 내용 전체 반복
for i in range(1, 4):
    print(i)

    print("점심시간")
    print("뭐먹지")
    print("1.한식 2.중식 3.일식")
    menu = input(str(i) + " 입력:")
    #입력값이 1 = 한식 먹어야됨 
    #입력값이 2 = 짜장면이나 먹어야됨
    #입력값이 3 = 라멘이나 먹어야됨
    if menu == '1':
        print("한식")
    if menu =='2':
        print("중식")
    if menu == '3':
        print("일식")
## 여기까지 반복##
