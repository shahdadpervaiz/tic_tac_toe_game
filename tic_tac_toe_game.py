def board(x_state, o_state):
    one = 'X' if x_state[0] else ('O' if o_state[0] else 1)
    two = 'X' if x_state[1] else ('O' if o_state[1] else 2)
    three = 'X' if x_state[2] else ('O' if o_state[2] else 3)
    four = 'X' if x_state[3] else ('O' if o_state[3] else 4)
    five = 'X' if x_state[4] else ('O' if o_state[4] else 5)
    six = 'X' if x_state[5] else ('O' if o_state[5] else 6)
    seven = 'X' if x_state[6] else ('O' if o_state[6] else 7)
    eight = 'X' if x_state[7] else ('O' if o_state[7] else 8)
    nine = 'X' if x_state[8] else ('O' if o_state[8] else 9)


    print(f"{one} | {two} | {three} ")
    print("__|___|___")
    print(f"{four} | {five} | {six} ")
    print("__|___|___")
    print(f"{seven} | {eight} | {nine} ")


if __name__ == "__main__":
    x_state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    o_state = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    turn = 1 # here 1 shown the "X" while 0 will be "O"
    print("welcome")

while(True):
    board(x_state, o_state)
    if turn == 1 :
        print("X's move")
        value = int(input(' enter the board value: '))
        x_state[value-1] = 1
    else:
        print("0's move")
        value = int(input(' enter the board value: '))
        o_state[value-1] = 1
    turn = 1 - turn
   


