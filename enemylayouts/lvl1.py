def construct():
    enemies = []
    for i in range(10):
        add_quaterRow(+-150, enemies)
        add_halfRow(+-50, enemies)
        add_fullRow(+50, enemies)
        add_halfRow(+150, enemies)
        add_quaterRow((i * -500) + 250, enemies)
        print(i)
    return enemies


# add a full row of enemies
def add_fullRow(row, enemies):
    for i in range(11):
        enemies.append([(i + 1) * 100, row])


# add a row with invaders placed 200 apart
def add_halfRow(row, enemies):
    for i in range(5):
        enemies.append([(i + 1) * 200, row])


# add a row with placed 300 apart
def add_quaterRow(row, enemies):
    for i in range(3):
        enemies.append([(i + 1) * 300, row])
