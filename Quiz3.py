def leaf_status(climate, temperatures):
    threshold = 30 if climate == "Tropical" else 25 if climate == "continental" else 18
    leaf_status = ['F' if temp <= threshold else 'U' for temp in temperatures]
    for status in leaf_status:
        print(status)

climate = input().strip()
temperatures = eval(input())
leaf_status(climate, temperatures)
