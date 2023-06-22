player_1 = "x"
player_2 = "o"

step_board = list(range(1,10)) #Порядковые номера клеток
def board(): #Вывод доски на экран консоли
    print("_____________")
    for n in range(3):
        print("|", step_board[0 + n * 3], "|", step_board[1 + n * 3], "|", step_board[2 + n * 3], "|")
        print("_____________")
def who_win(step_board): #Кто победил
    win_combination = [[0, 1, 2], [0, 3, 6], [0, 4, 8], [1, 4, 7], [2, 5, 8],[2, 4, 6], [3, 4, 5], [6, 7, 8]]
    for w in win_combination:
        if step_board[w[0]] == step_board[w[1]] == step_board[w[2]]:
            return step_board[w[0]]
    return False
def step():
    count = 0
    while True:
        print("Ход x")
        step_board[int(input("Введите номер постановки х: ")) - 1] = "x"
        print("Ход o")
        step_board[int(input("Введите номер постановки o: ")) - 1] = "o"
        board()
        count += 1
        if count == 3:
            if who_win(step_board) in "x, o":
                print("Победил " + who_win(step_board))
                break

        print(who_win(step_board))


step()








