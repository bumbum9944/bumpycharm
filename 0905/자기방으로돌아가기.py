T = int(input())
for tc in range(1, T+1):
    N = int(input())
    students = [list(map(int, input().split())) for _ in range(N)]
    rooms = [[0]+[num for num in range(1, 400, 2)], [0]*201, [0]+[num for num in range(2, 401, 2)]]
    for student in students:
        idx = []
        for stu in student:
            if stu % 2:
                idx.append(rooms[0].index(stu))
            else:
                idx.append(rooms[2].index(stu))
        for check in range(min(idx), max(idx)+1):
            rooms[1][check] += 1
    print('#{} {}'.format(tc, max(rooms[1])))