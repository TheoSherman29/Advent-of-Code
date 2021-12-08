input = list(map(int, open('input.txt').read().split(',')))


Fish = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

for i in input:
    Fish[i] += 1

print(Fish)


def breedFish(FishList, days):
    for day in range(days):
        for i in range(0, 10):
            if i == 0:
                FishList[9] += FishList[0]
                FishList[7] += FishList[0]
                FishList[0] = 0
            else:
                FishList[i - 1] += FishList[i]
                FishList[i] = 0
        print(FishList)

    totalFish = 0
    for fish in FishList:
        totalFish += FishList[fish]

    print(totalFish)


breedFish(Fish, 256)


