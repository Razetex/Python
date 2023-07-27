print(" Приветствую в игре крестики-нолики! \n -----------------------------------")
field = [["-"] * 3 for i in range(3)]
def show_game():
    print()
    print("  | 0 | 1 | 2 |")
    print("---------------")
    for i, j in enumerate(field):
        row_info = f"{i} | {' | '.join(j)} |"
        print(row_info)
        print("---------------")
    print()

def input_player():
    while True:
     res = input("Ваш ход(принимает две координаты): ").split()

     if len(res) != 2:
      print("Введите две координаты!")
      continue

     x,y = res

     if not (x.isdigit()) or not (y.isdigit()):
         print("Введите числа!")
         continue

     x,y = int(x), int(y)

     if x < 0 or 2 < x or y < 0 or 2 < y:
      print("Координаты вне диапазона!")
      continue

     if field[x][y] != "-":
         print("Клетка уже занята!")
         continue

     return x,y

def chek_win():
    win = (((0,0), (0,1), (0,2)), ((1,0), (1,1), (1,2)), ((2,0), (2,1), (2,2)),
           ((0,0), (1,1), (2,2), (2,0),(1,1),(0,2)),
           ((0,0),(1,0),(2,0)), ((0,1),(1,1),(2,1)), ((0,2),(1,2),(2,2)))
    for cord in win:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X","X","X"]:
            print("Победа за X")
            return True
        if symbols == ["O","O","O"]:
            print("Победа за O")
            return True
    return False
count = 0

while True:
    count += 1
    show_game()
    if count % 2 == 1:
        print("Ходит первый игрок('X')")
    else:
        print("Ходит второй игрок('O')")

    x, y = input_player()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "O"

    if chek_win():
        break

    if count == 9:
        print("Ничья!")
        break





