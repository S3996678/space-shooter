def construct(value):
    enemies = []
    # to keep track of all positions
    high_start = 50
    medium_start = 150
    low_start = 350

    if value == "high":
        add_fullRow(high_start, enemies)
    elif value == "medium":
        for i in range(2):
            add_fullRow(medium_start, enemies)
            medium_start += 100
    elif value == "low":
        for i in range(2):
            add_fullRow(low_start, enemies)
            low_start += 100

    return enemies


# add a full row of enemies
def add_fullRow(row, enemies):
    for i in range(11):
        enemies.append([(i + 1) * 100, row])
