def passenger_count(N, passengers, T):
    count = 0
    for i in range(N):
        if passengers[i][0] <= T <= passengers[i][1]:
            count += 1
        elif passengers[i][0] == T == passengers[i][1]:
            count += 1
    return count

def counting():
        N = int(input())
        passengers = []
        for i in range(N):
            entry, exit = map(int, input().split())
            passengers.append((entry, exit))
        T = int(input())

        result = passenger_count(N, passengers, T)
        print(result)
counting()