def construct():
    enemies = []
    # to keep track of all positions
    fullrow_start = 50
    halfRow_start = 150
    quaterRow_start = 250

    # create enemy patern by looping
    for i in range(10):
        add_fullRow(fullrow_start, enemies)
        add_halfRow(halfRow_start, enemies)
        add_quaterRow(quaterRow_start, enemies)
        fullrow_start -= 300
        halfRow_start -= 300
        quaterRow_start -= 300
        print(quaterRow_start, halfRow_start, fullrow_start)
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
