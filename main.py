from BFS import BFS
from DFS import DFS
from Game import Game
from Hill_Climbing import HillClimbing
from Stone import Stone
from A_STAR import AStar
from UCS import UCS


def main():
    magnet_n = Stone("N")
    magnet_s = Stone("S")
    iron = Stone("iron")
    #//////////////////////////////////////////////////////////////


    game1 = Game(4, 4, 1)
    game1.grid.put_stone(2, 0, magnet_n)
    game1.grid.put_stone(1, 2, iron)
    game1.grid.set_cell_type(1, 1, "gCell")
    game1.grid.set_cell_type(1, 3, "gCell")
    for col in range(game1.grid.width):
        game1.grid.set_cell_type(3, col, "bCell")

    #//////////////////////////////////////////////////////////////
    # (2,2)
    game2 = Game(5, 3, 2)
    game2.grid.put_stone(4, 0, magnet_n)
    game2.grid.put_stone(1, 2, iron)
    game2.grid.put_stone(2, 1, iron)
    game2.grid.put_stone(2, 3, iron)
    game2.grid.put_stone(3, 2, iron)
    game2.grid.set_cell_type(0, 2, "gCell")
    game2.grid.set_cell_type(2, 2, "gCell")
    game2.grid.set_cell_type(4, 2, "gCell")
    game2.grid.set_cell_type(2, 0, "gCell")
    game2.grid.set_cell_type(2, 4, "gCell")
    # //////////////////////////////////////////////////////////////
    # (2,3)
    game3 = Game(4, 4, 3)

    game3.grid.put_stone(1, 1, magnet_n)
    game3.grid.put_stone(1, 3, iron)

    game3.grid.set_cell_type(0, 3, "gCell")
    game3.grid.set_cell_type(2, 3, "gCell")
    game3.grid.set_cell_type(0, 0, "bCell")
    game3.grid.set_cell_type(0, 1, "bCell")
    game3.grid.set_cell_type(0, 2, "bCell")
    # //////////////////////////////////////////////////////////////
    #(2,1)  (0,0)
    game4 = Game(5, 2, 4)

    game4.grid.put_stone(2, 0, magnet_n)
    game4.grid.put_stone(1, 1, iron)
    game4.grid.put_stone(3, 1, iron)
    game4.grid.set_cell_type(0, 0, "gCell")
    game4.grid.set_cell_type(0, 2, "gCell")
    game4.grid.set_cell_type(4, 1, "gCell")

    game4.grid.set_cell_type(0, 3, "bCell")
    game4.grid.set_cell_type(1, 3, "bCell")
    game4.grid.set_cell_type(2, 3, "bCell")
    game4.grid.set_cell_type(3, 3, "bCell")
    game4.grid.set_cell_type(4, 3, "bCell")
    game4.grid.set_cell_type(0, 4, "bCell")
    game4.grid.set_cell_type(1, 4, "bCell")
    game4.grid.set_cell_type(2, 4, "bCell")
    game4.grid.set_cell_type(3, 4, "bCell")
    game4.grid.set_cell_type(4, 4, "bCell")
    game4.grid.set_cell_type(1, 0, "bCell")
    game4.grid.set_cell_type(3, 0, "bCell")
    # //////////////////////////////////////////////////////////////
    #(3,2) // (3,0)
    game5 = Game(4, 2, 5)

    game5.grid.put_stone(3, 1, magnet_n)
    game5.grid.put_stone(1, 0, iron)
    game5.grid.put_stone(2, 0, iron)
    game5.grid.put_stone(1, 2, iron)
    game5.grid.put_stone(2, 2, iron)

    game5.grid.set_cell_type(0, 0, "gCell")
    game5.grid.set_cell_type(0, 2, "gCell")
    game5.grid.set_cell_type(3, 0, "gCell")
    game5.grid.set_cell_type(1, 0, "gCell")
    game5.grid.set_cell_type(1, 2, "gCell")

    game5.grid.set_cell_type(0, 1, "bCell")
    game5.grid.set_cell_type(1, 1, "bCell")
    game5.grid.set_cell_type(2, 1, "bCell")
    # //////////////////////////////////////////////////////////////
    #(1,0) // (2,3)
    game6 = Game(5, 2, 5)

    game6.grid.put_stone(2, 0, magnet_n)
    game6.grid.put_stone(1, 1, iron)
    game6.grid.put_stone(1, 3, iron)

    game6.grid.set_cell_type(0, 3, "gCell")
    game6.grid.set_cell_type(1, 2, "gCell")
    game6.grid.set_cell_type(2, 3, "gCell")
    for col in range(game6.grid.width):
        game6.grid.set_cell_type(3, col, "bCell")
        game6.grid.set_cell_type(4, col, "bCell")
    # //////////////////////////////////////////////////////////////
    #(3,0)//(2,3)
    game7 = Game(5, 2, 7)

    game7.grid.put_stone(2, 1, magnet_n)
    game7.grid.put_stone(1, 0, iron)
    game7.grid.put_stone(2, 0, iron)
    game7.grid.put_stone(3, 1, iron)
    game7.grid.put_stone(3, 2, iron)

    game7.grid.set_cell_type(0, 0, "gCell")
    game7.grid.set_cell_type(2, 3, "gCell")
    game7.grid.set_cell_type(4, 3, "gCell")
    game7.grid.set_cell_type(1, 0, "gCell")
    game7.grid.set_cell_type(3, 2, "gCell")

    game7.grid.set_cell_type(4, 0, "bCell")
    game7.grid.set_cell_type(4, 1, "bCell")
    game7.grid.set_cell_type(4, 2, "bCell")
    game7.grid.set_cell_type(0, 4, "bCell")
    game7.grid.set_cell_type(1, 4, "bCell")
    game7.grid.set_cell_type(2, 4, "bCell")
    game7.grid.set_cell_type(3, 4, "bCell")
    game7.grid.set_cell_type(4, 4, "bCell")

    # //////////////////////////////////////////////////////////////
    #(2,1) // (0,2)
    game8 = Game(4, 2, 8)

    game8.grid.put_stone(2, 0, magnet_n)
    game8.grid.put_stone(1, 1, iron)
    game8.grid.put_stone(1, 2, iron)

    game8.grid.set_cell_type(0, 0, "gCell")
    game8.grid.set_cell_type(0, 2, "gCell")
    game8.grid.set_cell_type(2, 2, "gCell")
    for col in range(game8.grid.width):
        game8.grid.set_cell_type(3, col, "bCell")
    # //////////////////////////////////////////////////////////////
    #(0,4) //(0,3)
    game9 = Game(7, 2, 9)

    game9.grid.put_stone(0, 0, magnet_n)  # Place magnet
    game9.grid.put_stone(0, 3, iron)  # Place first iron
    game9.grid.put_stone(0, 5, iron)  # Place second iron

    game9.grid.set_cell_type(0, 1, "gCell")
    game9.grid.set_cell_type(0, 3, "gCell")
    game9.grid.set_cell_type(0, 6, "gCell")
    for col in range(game9.grid.width):
        game9.grid.set_cell_type(1, col, "bCell")
        game9.grid.set_cell_type(2, col, "bCell")
        game9.grid.set_cell_type(3, col, "bCell")
        game9.grid.set_cell_type(4, col, "bCell")
        game9.grid.set_cell_type(5, col, "bCell")
        game9.grid.set_cell_type(6, col, "bCell")
    # //////////////////////////////////////////////////////////////
    #(3,2)//(1,3)
    game10 = Game(4, 2, 10)

    game10.grid.put_stone(0, 0, magnet_n)  # Place magnet
    game10.grid.put_stone(2, 2, iron)  # Place first iron
    game10.grid.put_stone(2, 3, iron)  # Place second iron
    game10.grid.put_stone(3, 1, iron)  # Place third iron

    game10.grid.set_cell_type(1, 1, "gCell")
    game10.grid.set_cell_type(1, 3, "gCell")
    game10.grid.set_cell_type(3, 0, "gCell")
    game10.grid.set_cell_type(3, 3, "gCell")
    # //////////////////////////////////////////////////////////////
    #(0,1)
    game11 = Game(5, 1, 11)

    game11.grid.put_stone(1, 2, magnet_s)
    game11.grid.put_stone(0, 0, iron)
    game11.grid.put_stone(0, 4, iron)

    game11.grid.set_cell_type(0, 1, "gCell")
    game11.grid.set_cell_type(0, 2, "gCell")
    game11.grid.set_cell_type(0, 3, "gCell")

    game11.grid.set_cell_type(1, 0, "bCell")
    game11.grid.set_cell_type(1, 1, "bCell")
    game11.grid.set_cell_type(1, 3, "bCell")
    game11.grid.set_cell_type(1, 4, "bCell")
    for col in range(game11.grid.width):
        game11.grid.set_cell_type(2, col, "bCell")
        game11.grid.set_cell_type(3, col, "bCell")
        game11.grid.set_cell_type(4, col, "bCell")


    # //////////////////////////////////////////////////////////////
    #(4,0)
    game12 = Game(5, 1, 12)

    game12.grid.put_stone(3, 1, magnet_s)
    game12.grid.put_stone(0, 0, iron)
    game12.grid.put_stone(1, 0, iron)
    game12.grid.put_stone(4, 3, iron)

    game12.grid.set_cell_type(2, 0, "gCell")
    game12.grid.set_cell_type(1, 0, "gCell")
    game12.grid.set_cell_type(4, 0, "gCell")
    game12.grid.set_cell_type(4, 2, "gCell")
    game12.grid.set_cell_type(0, 2, "bCell")
    game12.grid.set_cell_type(0, 3, "bCell")
    game12.grid.set_cell_type(1, 2, "bCell")
    game12.grid.set_cell_type(1, 3, "bCell")
    for col in range(game12.grid.width):
        game12.grid.set_cell_type(col,4,"bCell")
        game12.grid.set_cell_type(col,4,"bCell")
        game12.grid.set_cell_type(col,4,"bCell")
        game12.grid.set_cell_type(col,4, "bCell")
        game12.grid.set_cell_type(col, 4,"bCell")
    # //////////////////////////////////////////////////////////////
    #(0,2)//(2,1)
    game13 = Game(6, 2, 13)

    game13.grid.put_stone(2, 3, magnet_s)
    game13.grid.put_stone(0, 0, iron)
    game13.grid.put_stone(0, 4, iron)
    game13.grid.put_stone(0, 5, iron)

    game13.grid.set_cell_type(0, 3, "gCell")
    game13.grid.set_cell_type(0, 4, "gCell")
    game13.grid.set_cell_type(2, 1, "gCell")
    game13.grid.set_cell_type(1, 1, "gCell")

    game13.grid.set_cell_type(1, 0, "bCell")
    game13.grid.set_cell_type(2, 0, "bCell")
    game13.grid.set_cell_type(1, 4, "bCell")
    game13.grid.set_cell_type(2, 4, "bCell")
    game13.grid.set_cell_type(1, 5, "bCell")
    game13.grid.set_cell_type(2, 5, "bCell")
    for col in range(game13.grid.width):
        game13.grid.set_cell_type(3, col, "bCell")
        game13.grid.set_cell_type(4, col, "bCell")
        game13.grid.set_cell_type(5, col, "bCell")

    # //////////////////////////////////////////////////////////////
    #(0,0) // (2,2)
    game14 = Game(4, 2, 14)


    game14.grid.put_stone(3, 3, magnet_s)
    game14.grid.put_stone(0, 3, iron)
    game14.grid.put_stone(2, 0, iron)
    game14.grid.put_stone(3, 0, iron)
    # Set goal cells
    game14.grid.set_cell_type(1, 0, "gCell")
    game14.grid.set_cell_type(1, 2, "gCell")
    game14.grid.set_cell_type(2, 1, "gCell")
    game14.grid.set_cell_type(2, 2, "gCell")
    # //////////////////////////////////////////////////////////////
    #n(0,2) // s(2,4)
    game15 = Game(5, 2, 15)

    game15.grid.put_stone(1, 2, magnet_n)
    game15.grid.put_stone(2, 2, magnet_s)
    game15.grid.put_stone(0, 1, iron)
    game15.grid.put_stone(0, 3, iron)

    game15.grid.set_cell_type(0, 0, "gCell")
    game15.grid.set_cell_type(0, 2, "gCell")
    game15.grid.set_cell_type(1, 4, "gCell")
    game15.grid.set_cell_type(2, 4, "gCell")

    for col in range(game15.grid.width):
        game15.grid.set_cell_type(3, col, "bCell")
    for row in range(4, game15.grid.width):
        for col in range(game15.grid.width):
            game15.grid.set_cell_type(row, col, "bCell")

    # //////////////////////////////////////////////////////////////
    #n(2,2)  s(0,4)  n(4,0)
    game16 = Game(5, 3, 16)

    game16.grid.put_stone(2, 4, magnet_n)
    game16.grid.put_stone(2, 0, magnet_s)
    game16.grid.put_stone(1, 2, iron)
    game16.grid.put_stone(3, 2, iron)


    game16.grid.set_cell_type(0, 3, "gCell")
    game16.grid.set_cell_type(0, 4, "gCell")
    game16.grid.set_cell_type(4, 0, "gCell")
    game16.grid.set_cell_type(4, 3, "gCell")
    # //////////////////////////////////////////////////////////////
    #s(2,2) n(1,1)
    game17 = Game(4, 2, 17)

    # Place magnets and irons using the new structure
    game17.grid.put_stone(3, 3, magnet_n)  # North magnet at (3, 3)
    game17.grid.put_stone(0, 0, magnet_s)  # South magnet at (0, 0)
    game17.grid.put_stone(0, 2, iron)  # Iron at (0, 2)
    game17.grid.put_stone(2, 0, iron)  # Iron at (2, 0)

    # Set goal cells
    game17.grid.set_cell_type(1, 1, "gCell")
    game17.grid.set_cell_type(1, 3, "gCell")
    game17.grid.set_cell_type(2, 2, "gCell")
    game17.grid.set_cell_type(3, 1, "gCell")
    # //////////////////////////////////////////////////////////////
    #s(2,3) n(2,5)
    game18 = Game(6, 2, 18)


    game18.grid.put_stone(4, 3, magnet_n)
    game18.grid.put_stone(4, 2, magnet_s)
    game18.grid.put_stone(2, 0, iron)
    game18.grid.put_stone(0, 3, iron)
    game18.grid.put_stone(2, 5, iron)

    game18.grid.set_cell_type(2, 1, "gCell")
    game18.grid.set_cell_type(1, 3, "gCell")
    game18.grid.set_cell_type(2, 2, "gCell")
    game18.grid.set_cell_type(2, 3, "gCell")
    game18.grid.set_cell_type(2, 5, "gCell")

    game18.grid.set_cell_type(0, 0, "bCell")
    game18.grid.set_cell_type(1, 0, "bCell")
    game18.grid.set_cell_type(0, 1, "bCell")
    game18.grid.set_cell_type(1, 1, "bCell")
    game18.grid.set_cell_type(0, 4, "bCell")
    game18.grid.set_cell_type(0, 5, "bCell")
    game18.grid.set_cell_type(1, 5, "bCell")
    game18.grid.set_cell_type(1, 4, "bCell")
    game18.grid.set_cell_type(4, 0, "bCell")
    game18.grid.set_cell_type(4, 1, "bCell")
    game18.grid.set_cell_type(4, 4, "bCell")
    game18.grid.set_cell_type(4, 5, "bCell")
    for col in range(game18.grid.width):
        game18.grid.set_cell_type(5, col, "bCell")

    # //////////////////////////////////////////////////////////////
    #s(2,3) s(2,1) //  n(1,2) n(3,2)
    game19 = Game(5, 4, 19)

    game19.grid.put_stone(0, 2, magnet_n)
    game19.grid.put_stone(2, 2, magnet_s)
    game19.grid.put_stone(0, 1, iron)
    game19.grid.put_stone(0, 3, iron)
    game19.grid.put_stone(4, 1, iron)
    game19.grid.put_stone(4, 3, iron)

    game19.grid.set_cell_type(1, 0, "gCell")
    game19.grid.set_cell_type(3, 0, "gCell")
    game19.grid.set_cell_type(2, 1, "gCell")
    game19.grid.set_cell_type(3, 2, "gCell")
    game19.grid.set_cell_type(1, 4, "gCell")
    game19.grid.set_cell_type(3, 4, "gCell")

    game19.grid.set_cell_type(0, 0, "bCell")
    game19.grid.set_cell_type(2, 0, "bCell")
    game19.grid.set_cell_type(4, 0, "bCell")
    game19.grid.set_cell_type(0, 4, "bCell")
    game19.grid.set_cell_type(2, 4, "bCell")
    game19.grid.set_cell_type(4, 4, "bCell")
    # //////////////////////////////////////////////////////////////
    #n(0,3) // s(2,0)

    game20 = Game(5, 2, 20)

    game20.grid.put_stone(4, 2, magnet_n)
    game20.grid.put_stone(4, 3, magnet_s)
    game20.grid.put_stone(0, 1, iron)
    game20.grid.put_stone(0, 2, iron)
    game20.grid.put_stone(4, 0, iron)


    game20.grid.set_cell_type(0, 1, "gCell")
    game20.grid.set_cell_type(0, 3, "gCell")
    game20.grid.set_cell_type(1, 0, "gCell")
    game20.grid.set_cell_type(2, 0, "gCell")
    game20.grid.set_cell_type(3, 0, "gCell")

    for col in range(game20.grid.width):
        game20.grid.set_cell_type(col,4,"bCell")
        game20.grid.set_cell_type(col,4,"bCell")
        game20.grid.set_cell_type(col,4,"bCell")
        game20.grid.set_cell_type(col,4, "bCell")
        game20.grid.set_cell_type(col, 4,"bCell")
    # //////////////////////////////////////////////////////////////
    #n(0,2)  s(2,0)
    game21 = Game(4, 2, 21)

    game21.grid.put_stone(2, 0, magnet_n)
    game21.grid.put_stone(2, 3, magnet_s)
    game21.grid.put_stone(0, 1, iron)
    game21.grid.put_stone(1, 1, iron)
    game21.grid.put_stone(1, 2, iron)

    game21.grid.set_cell_type(0, 2, "gCell")
    game21.grid.set_cell_type(1, 1, "gCell")
    game21.grid.set_cell_type(1, 0, "gCell")
    game21.grid.set_cell_type(2, 0, "gCell")
    game21.grid.set_cell_type(2, 1, "gCell")


    for col in range(game21.grid.width):
        game21.grid.set_cell_type(3, col, "bCell")
    # //////////////////////////////////////////////////////////////
    # s(3,3)  s(0,1) n(1,0)
    game22 = Game(5, 3, 22)

    game22.grid.put_stone(0, 0, magnet_n)
    game22.grid.put_stone(3, 2, magnet_s)
    game22.grid.put_stone(0, 3, iron)
    game22.grid.put_stone(0, 4, iron)
    game22.grid.put_stone(3, 0, iron)

    game22.grid.set_cell_type(0, 1, "gCell")
    game22.grid.set_cell_type(0, 3, "gCell")
    game22.grid.set_cell_type(1, 0, "gCell")
    game22.grid.set_cell_type(1, 4, "gCell")
    game22.grid.set_cell_type(2, 1, "gCell")
    game22.grid.set_cell_type(0, 2, "bCell")
    game22.grid.set_cell_type(1, 2,"bCell")

    for col in range(game22.grid.width):
            game22.grid.set_cell_type(4, col, "bCell")
    # //////////////////////////////////////////////////////////////
    #n(0,4) s(2,2) n(0,2)
    game23 = Game(5, 3, 23)

    game23.grid.put_stone(3, 4, magnet_n)
    game23.grid.put_stone(3, 2, magnet_s)
    game23.grid.put_stone(0, 3, iron)
    game23.grid.put_stone(1, 4, iron)
    game23.grid.put_stone(2, 0, iron)

    game23.grid.set_cell_type(0, 2, "gCell")
    game23.grid.set_cell_type(2, 2, "gCell")
    game23.grid.set_cell_type(2, 1, "gCell")
    game23.grid.set_cell_type(2, 3, "gCell")
    game23.grid.set_cell_type(2, 1, "gCell")
    # game23.grid.set_cell_type(3, 2, "bCell")
    # game22.grid.set_cell_type(1, 2,"bCell")

    for col in range(game23.grid.width):
        game23.grid.set_cell_type(4, col, "bCell")
    # //////////////////////////////////////////////////////////////
    #s(3,1) n(2,3) s(4,1)
    game24 = Game(5, 3, 24)

    game24.grid.put_stone(1, 4, magnet_n)
    game24.grid.put_stone(3, 0, magnet_s)
    game24.grid.put_stone(0, 1, iron)
    game24.grid.put_stone(1, 3, iron)
    game24.grid.put_stone(3, 4, iron)

    game24.grid.set_cell_type(0, 3, "gCell")
    game24.grid.set_cell_type(2, 3, "gCell")
    game24.grid.set_cell_type(2, 1, "gCell")
    game24.grid.set_cell_type(4, 2, "gCell")
    game24.grid.set_cell_type(4, 1, "gCell")
    game24.grid.set_cell_type(4, 0,"bCell")
    game24.grid.set_cell_type(4, 4,"bCell")
    # //////////////////////////////////////////////////////////////
    #n(2,2) s(4,0) n(0,0)
    game25 = Game(5, 3, 25)

    game25.grid.put_stone(4, 0, magnet_n)
    game25.grid.put_stone(0, 3, magnet_s)
    game25.grid.put_stone(0, 0, iron)
    game25.grid.put_stone(1, 2, iron)
    game25.grid.put_stone(3, 2, iron)
    game25.grid.put_stone(4, 3, iron)

    game25.grid.set_cell_type(0, 0, "gCell")
    game25.grid.set_cell_type(0, 3, "gCell")
    game25.grid.set_cell_type(2, 0, "gCell")
    game25.grid.set_cell_type(4, 0, "gCell")
    game25.grid.set_cell_type(4, 1, "gCell")
    game25.grid.set_cell_type(4, 2, "gCell")

    for col in range(game25.grid.width):
        game25.grid.set_cell_type(col, 4, "bCell")
    # //////////////////////////////////////////////////////////////




    game = {
        '1': game1,
        '2': game2,
        '3': game3,
        '4': game4,
        '5': game5,
        '6': game6,
        '7': game7,
        '8': game8,
        '9': game9,
        '10': game10,
        '11': game11,
        '12': game12,
        '13': game13,
        '14': game14,
        '15': game15,
        '16': game16,
        '17': game17,
        '18': game18,
        '19': game19,
        '20': game20,
        '21': game21,
        '22': game22,
        '23': game23,
        '24': game24,
        '25': game25
    }

    choice = input("Enter the number of level from 1 to 25: ")

    if choice in game:
        print(f"Start level {choice}")

        choice_1 = input("Choose the game mode:\n1. Manual Play\n2. Automatic Solve\n")

        if choice_1 == '1':
            game[choice].play()

        elif choice_1 == '2':
            choice_2 = input(
                "Enter:\n"
                "1 for BFS\n"
                "2 for DFS\n"
                "3 for UCS\n"
                "4 for Hill Climbing\n"
                "5 for A*\n"
                ": "
            )

            if choice_2 == '1':
                bfs_solver = BFS(game[choice])
                print("The answer using BFS:")
                bfs_solver.start()

            elif choice_2 == '2':
                dfs_solver = DFS(game[choice])
                print("The answer using DFS:")
                dfs_solver.start()

            elif choice_2 == '3':
                ucs_solver = UCS(game[choice])
                print("The answer using UCS:")
                ucs_solver.start()

            elif choice_2 == '4':
                hill_climbing_solver = HillClimbing(game[choice])
                print("The answer using Hill Climbing:")
                hill_climbing_solver.start()

            elif choice_2 == '5':
                a_star_solver = AStar(game[choice])
                print("The answer using A*:")
                a_star_solver.start()

            else:
                print("Invalid choice for solving method.")
    else:
        print("Invalid level choice.")







    # choice = input("enter the number of level from 1 to 25 :")
    #
    # if choice == '1':
    #     print("start level 1")
    #     choice_1 = input("Choose the game mode:\n1. Manual Play\n2. Automatic Solve\n")
    #     if choice_1 == '1':
    #         game1.play()
    #     elif choice_1 == '2':
    #         choice_2 = input("enter 1 for BFS and 2 for DFS and 3 for UCS and 4 for Hill Climbing and 5 for A_Star :")
    #         if choice_2 == '1':
    #             bfs_solver = BFS(game1)
    #             print("the answer using BFS :")
    #             bfs_solver.start()
    #         elif choice_2 == '2':
    #             dfs_solver = DFS(game1)
    #             print("the answer using DFS :")
    #             dfs_solver.start()
    #         elif choice_2 == '3':
    #             ucs_solver = UCS(game1)
    #             print("the answer using UCS :")
    #             ucs_solver.start()
    #         elif choice_2 == '4':
    #             HillClimbing_solver= HillClimbing(game1)
    #             print("the answer using Hill Climbing :")
    #             HillClimbing_solver.start()
    #         elif choice_2 == '4':
    #             A_star = AStar(game1)
    #             print("the answer using A Star :")
    #             A_star.start()

    #
    # elif choice == '2':
    #     print("start level 2")
    #     choice_1 = input("Choose the game mode:\n1. Manual Play\n2. Automatic Solve\n")
    #     if choice_1 == '1':
    #         game2.play()
    #     elif choice_1 == '2':
    #         choice_2 = input("enter 1 for BFS and 2 for DFS and 3 for ucs :")
    #         solver = Solver(game2)
    #         if choice_2 == '1':
    #             print("the answer using BFS :")
    #             solver.BFS()
    #         elif choice_2 == '2':
    #             print("the answer using DFS :")
    #             solver.DFS()
    #         elif choice_2 == '3':
    #             print("the answer using UCS :")
    #             solver.UCS()
    #
    # elif choice == '3':
    #     print("start level 3")
    #     choice_1 = input("Choose the game mode:\n1. Manual Play\n2. Automatic Solve\n")
    #     if choice_1 == '1':
    #         game3.play()
    #     elif choice_1 == '2':
    #         choice_2 = input("enter 1 for BFS and 2 for DFS and 3 for ucs :")
    #         solver = Solver(game3)
    #         if choice_2 == '1':
    #             print("the answer using BFS :")
    #             solver.BFS()
    #         elif choice_2 == '2':
    #             print("the answer using DFS :")
    #             solver.DFS()
    #         elif choice_2 == '3':
    #             print("the answer using UCS :")
    #             solver.UCS()
    #
    # elif choice == '4':
    #     print("start level 4")
    #     choice_1 = input("Choose the game mode:\n1. Manual Play\n2. Automatic Solve\n")
    #     if choice_1 == '1':
    #         game4.play()
    #     elif choice_1 == '2':
    #         choice_2 = input("enter 1 for BFS and 2 for DFS and 3 for ucs :")
    #         solver = Solver(game4)
    #         if choice_2 == '1':
    #             print("the answer using BFS :")
    #             solver.BFS()
    #         elif choice_2 == '2':
    #             print("the answer using DFS :")
    #             solver.DFS()
    #         elif choice_2 == '3':
    #             print("the answer using UCS :")
    #             solver.UCS()
    #
    # elif choice == '5':
    #     print("start level 5")
    #     choice_1 = input("Choose the game mode:\n1. Manual Play\n2. Automatic Solve\n")
    #     if choice_1 == '1':
    #         game5.play()
    #     elif choice_1 == '2':
    #         choice_2 = input("enter 1 for BFS and 2 for DFS and 3 for ucs :")
    #         solver = Solver(game5)
    #         if choice_2 == '1':
    #             print("the answer using BFS :")
    #             solver.BFS()
    #         elif choice_2 == '2':
    #             print("the answer using DFS :")
    #             solver.DFS()
    #         elif choice_2 == '3':
    #             print("the answer using UCS :")
    #             solver.UCS()
    #
    # elif choice == '6':
    #     print("start level 6")
    #     choice_1 = input("Choose the game mode:\n1. Manual Play\n2. Automatic Solve\n")
    #     if choice_1 == '1':
    #         game6.play()
    #     elif choice_1 == '2':
    #         choice_2 = input("enter 1 for BFS and 2 for DFS and 3 for ucs :")
    #         solver = Solver(game6)
    #         if choice_2 == '1':
    #             print("the answer using BFS :")
    #             solver.BFS()
    #         elif choice_2 == '2':
    #             print("the answer using DFS :")
    #             solver.DFS()
    #         elif choice_2 == '3':
    #             print("the answer using UCS :")
    #             solver.UCS()
    # elif choice == '7':
    #     print("start level 7")
    #     choice_1 = input("Choose the game mode:\n1. Manual Play\n2. Automatic Solve\n")
    #     if choice_1 == '1':
    #         game7.play()
    #     elif choice_1 == '2':
    #         choice_2 = input("enter 1 for BFS and 2 for DFS and 3 for ucs :")
    #         solver = Solver(game7)
    #         if choice_2 == '1':
    #             print("the answer using BFS :")
    #             solver.BFS()
    #         elif choice_2 == '2':
    #             print("the answer using DFS :")
    #             solver.DFS()
    #         elif choice_2 == '3':
    #             print("the answer using UCS :")
    #             solver.UCS()
    # elif choice == '8':
    #     print("start level 8")
    #     choice_1 = input("Choose the game mode:\n1. Manual Play\n2. Automatic Solve\n")
    #     if choice_1 == '1':
    #         game8.play()
    #     elif choice_1 == '2':
    #         choice_2 = input("enter 1 for BFS and 2 for DFS and 3 for ucs :")
    #         solver = Solver(game8)
    #         if choice_2 == '1':
    #             print("the answer using BFS :")
    #             solver.BFS()
    #         elif choice_2 == '2':
    #             print("the answer using DFS :")
    #             solver.DFS()
    #         elif choice_2 == '3':
    #             print("the answer using UCS :")
    #             solver.UCS()
    #
    # elif choice == '9':
    #     print("start level 9")
    #     choice_1 = input("Choose the game mode:\n1. Manual Play\n2. Automatic Solve\n")
    #     if choice_1 == '1':
    #         game9.play()
    #     elif choice_1 == '2':
    #         choice_2 = input("enter 1 for BFS and 2 for DFS and 3 for ucs :")
    #         solver = Solver(game9)
    #         if choice_2 == '1':
    #             print("the answer using BFS :")
    #             solver.BFS()
    #         elif choice_2 == '2':
    #             print("the answer using DFS :")
    #             solver.DFS()
    #         elif choice_2 == '3':
    #             print("the answer using UCS :")
    #             solver.UCS()
    #
    # elif choice == '10':
    #     print("start level 10")
    #     choice_1 = input("Choose the game mode:\n1. Manual Play\n2. Automatic Solve\n")
    #     if choice_1 == '1':
    #         game10.play()
    #     elif choice_1 == '2':
    #         choice_2 = input("enter 1 for BFS and 2 for DFS and 3 for ucs :")
    #         solver = Solver(game10)
    #         if choice_2 == '1':
    #             print("the answer using BFS :")
    #             solver.BFS()
    #         elif choice_2 == '2':
    #             print("the answer using DFS :")
    #             solver.DFS()
    #         elif choice_2 == '3':
    #             print("the answer using UCS :")
    #             solver.UCS()
    #
    # elif choice == '11':
    #     print("start level 11")
    #     choice_1 = input("Choose the game mode:\n1. Manual Play\n2. Automatic Solve\n")
    #     if choice_1 == '1':
    #         game11.play()
    #     elif choice_1 == '2':
    #         choice_2 = input("enter 1 for BFS and 2 for DFS and 3 for ucs :")
    #         solver = Solver(game11)
    #         if choice_2 == '1':
    #             print("the answer using BFS :")
    #             solver.BFS()
    #         elif choice_2 == '2':
    #             print("the answer using DFS :")
    #             solver.DFS()
    #
    # elif choice == '12':
    #     print("start level 12")
    #     choice_1 = input("Choose the game mode:\n1. Manual Play\n2. Automatic Solve\n")
    #     if choice_1 == '1':
    #         game12.play()
    #     elif choice_1 == '2':
    #         choice_2 = input("enter 1 for BFS and 2 for DFS and 3 for ucs :")
    #         solver = Solver(game12)
    #         if choice_2 == '1':
    #             print("the answer using BFS :")
    #             solver.BFS()
    #         elif choice_2 == '2':
    #             print("the answer using DFS :")
    #             solver.DFS()
    #
    # elif choice == '13':
    #     print("start level 13")
    #     choice_1 = input("Choose the game mode:\n1. Manual Play\n2. Automatic Solve\n")
    #     if choice_1 == '1':
    #         game13.play()
    #     elif choice_1 == '2':
    #         choice_2 = input("enter 1 for BFS and 2 for DFS and 3 for ucs :")
    #         solver = Solver(game13)
    #         if choice_2 == '1':
    #             print("the answer using BFS :")
    #             solver.BFS()
    #         elif choice_2 == '2':
    #             print("the answer using DFS :")
    #             solver.DFS()
    #
    # elif choice == '14':
    #     print("start level 14")
    #     choice_1 = input("Choose the game mode:\n1. Manual Play\n2. Automatic Solve\n")
    #     if choice_1 == '1':
    #         game14.play()
    #     elif choice_1 == '2':
    #         choice_2 = input("enter 1 for BFS and 2 for DFS and 3 for ucs :")
    #         solver = Solver(game14)
    #         if choice_2 == '1':
    #             print("the answer using BFS :")
    #             solver.BFS()
    #         elif choice_2 == '2':
    #             print("the answer using DFS :")
    #             solver.DFS()
    #
    # elif choice == '15':
    #     print("start level 15")
    #     choice_1 = input("Choose the game mode:\n1. Manual Play\n2. Automatic Solve\n")
    #     if choice_1 == '1':
    #         game15.play()
    #     elif choice_1 == '2':
    #         choice_2 = input("enter 1 for BFS and 2 for DFS and 3 for ucs :")
    #         solver = Solver(game15)
    #         if choice_2 == '1':
    #             print("the answer using BFS :")
    #             solver.BFS()
    #         elif choice_2 == '2':
    #             print("the answer using DFS :")
    #             solver.DFS()
    #
    # elif choice == '16':
    #     print("start level 16")
    #     choice_1 = input("Choose the game mode:\n1. Manual Play\n2. Automatic Solve\n")
    #     if choice_1 == '1':
    #         game16.play()
    #     elif choice_1 == '2':
    #         choice_2 = input("enter 1 for BFS and 2 for DFS and 3 for ucs :")
    #         solver = Solver(game16)
    #         if choice_2 == '1':
    #             print("the answer using BFS :")
    #             solver.BFS()
    #         elif choice_2 == '2':
    #             print("the answer using DFS :")
    #             solver.DFS()
    #
    # elif choice == '17':
    #     print("start level 17")
    #     choice_1 = input("Choose the game mode:\n1. Manual Play\n2. Automatic Solve\n")
    #     if choice_1 == '1':
    #         game17.play()
    #     elif choice_1 == '2':
    #         choice_2 = input("enter 1 for BFS and 2 for DFS and 3 for ucs :")
    #         solver = Solver(game17)
    #         if choice_2 == '1':
    #             print("the answer using BFS :")
    #             solver.BFS()
    #         elif choice_2 == '2':
    #             print("the answer using DFS :")
    #             solver.DFS()
    #
    # elif choice == '18':
    #     print("start level 18")
    #     choice_1 = input("Choose the game mode:\n1. Manual Play\n2. Automatic Solve\n")
    #     if choice_1 == '1':
    #         game18.play()
    #     elif choice_1 == '2':
    #         choice_2 = input("enter 1 for BFS and 2 for DFS and 3 for ucs :")
    #         solver = Solver(game18)
    #         if choice_2 == '1':
    #             print("the answer using BFS :")
    #             solver.BFS()
    #         elif choice_2 == '2':
    #             print("the answer using DFS :")
    #             solver.DFS()
    #
    # elif choice == '19':
    #     print("start level 19")
    #     choice_1 = input("Choose the game mode:\n1. Manual Play\n2. Automatic Solve\n")
    #     if choice_1 == '1':
    #         game19.play()
    #     elif choice_1 == '2':
    #         choice_2 = input("enter 1 for BFS and 2 for DFS and 3 for ucs :")
    #         solver = Solver(game19)
    #         if choice_2 == '1':
    #             print("the answer using BFS :")
    #             solver.BFS()
    #         elif choice_2 == '2':
    #             print("the answer using DFS :")
    #             solver.DFS()
    #
    # elif choice == '20':
    #     print("start level 20")
    #     choice_1 = input("Choose the game mode:\n1. Manual Play\n2. Automatic Solve\n")
    #     if choice_1 == '1':
    #         game20.play()
    #     elif choice_1 == '2':
    #         choice_2 = input("enter 1 for BFS and 2 for DFS and 3 for ucs :")
    #         solver = Solver(game20)
    #         if choice_2 == '1':
    #             print("the answer using BFS :")
    #             solver.BFS()
    #         elif choice_2 == '2':
    #             print("the answer using DFS :")
    #             solver.DFS()
    #
    # elif choice == '21':
    #     print("start level 21")
    #     choice_1 = input("Choose the game mode:\n1. Manual Play\n2. Automatic Solve\n")
    #     if choice_1 == '1':
    #         game21.play()
    #     elif choice_1 == '2':
    #         choice_2 = input("enter 1 for BFS and 2 for DFS and 3 for ucs :")
    #         solver = Solver(game21)
    #         if choice_2 == '1':
    #             print("the answer using BFS :")
    #             solver.BFS()
    #         elif choice_2 == '2':
    #             print("the answer using DFS :")
    #             solver.DFS()
    #
    # elif choice == '22':
    #     print("start level 22")
    #     choice_1 = input("Choose the game mode:\n1. Manual Play\n2. Automatic Solve\n")
    #     if choice_1 == '1':
    #         game22.play()
    #     elif choice_1 == '2':
    #         choice_2 = input("enter 1 for BFS and 2 for DFS and 3 for ucs :")
    #         solver = Solver(game22)
    #         if choice_2 == '1':
    #             print("the answer using BFS :")
    #             solver.BFS()
    #         elif choice_2 == '2':
    #             print("the answer using DFS :")
    #             solver.DFS()
    #
    # elif choice == '23':
    #     print("start level 23")
    #     choice_1 = input("Choose the game mode:\n1. Manual Play\n2. Automatic Solve\n")
    #     if choice_1 == '1':
    #         game23.play()
    #     elif choice_1 == '2':
    #         choice_2 = input("enter 1 for BFS and 2 for DFS and 3 for ucs :")
    #         solver = Solver(game23)
    #         if choice_2 == '1':
    #             print("the answer using BFS :")
    #             solver.BFS()
    #         elif choice_2 == '2':
    #             print("the answer using DFS :")
    #             solver.DFS()
    #
    # elif choice == '24':
    #     print("start level 24")
    #     choice_1 = input("Choose the game mode:\n1. Manual Play\n2. Automatic Solve\n")
    #     if choice_1 == '1':
    #         game24.play()
    #     elif choice_1 == '2':
    #         choice_2 = input("enter 1 for BFS and 2 for DFS and 3 for ucs :")
    #         solver = Solver(game24)
    #         if choice_2 == '1':
    #             print("the answer using BFS :")
    #             solver.BFS()
    #         elif choice_2 == '2':
    #             print("the answer using DFS :")
    #             solver.DFS()
    #
    # elif choice == '25':
    #     print("start level 25")
    #     choice_1 = input("Choose the game mode:\n1. Manual Play\n2. Automatic Solve\n")
    #     if choice_1 == '1':
    #         game25.play()
    #     elif choice_1 == '2':
    #         choice_2 = input("enter 1 for BFS and 2 for DFS and 3 for ucs :")
    #         solver = Solver(game25)
    #         if choice_2 == '1':
    #             print("the answer using BFS :")
    #             solver.BFS()
    #         elif choice_2 == '2':
    #             print("the answer using DFS :")
    #             solver.DFS()
    #
    # else:
    #     print("Wrong input. Please enter a number between 1 and 25.")


if __name__ == "__main__":
    main()