N, M = map(int, input().split())

dogam = {}

for i in range(1, N + 1):
    pokemon = input()
    dogam[str(i)] = pokemon
    dogam[pokemon] = str(i)

for _ in range(M):
    pokemon = input()
    print(dogam[pokemon])
