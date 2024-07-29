"""

"""
import random,csv,time

def display_grid(grid):
    """
    Function to display the grid for the game 
    """
    for i in range(0,9,3) : 
        print(grid[i],grid[i+1],grid[i+2],sep=' | ')
        if i  == 6 :
            continue
        print('--','---','--', sep='+')
    print()
        
def computer_turn(s,comp_marker):
    """
    Function to play the computer's turn 
    """
    print("Computer's turn")
    time.sleep(1)
    i = random.choice((s)) #to randomly assign a cell to the computer
    grid[i] = comp_marker
    s.remove(i)
 
def user_history(username,win) :
    """
    Function to update the game results and return the user info to be
    displayed at the end of the game
    """
    with open('cps109_a1_output.csv','r',newline='') as f :
        user_info = list(csv.reader(f))
    with open('cps109_a1_output.csv','w',newline='') as f :
        w = csv.writer(f)
        for i in user_info :
            if username in i : #checking username for update
                if win :
                    i[1] = str(int(i[1]) + 1)
                else :
                    i[2] = str(int(i[2]) + 1)
                l = i
        w.writerows(user_info)   
        return l[0], l[1], l[2]

def new_user(username) :
    """
    Function to add new users to the csv file if the username is not present in
    the file
    """
    with open('cps109_a1_output.csv','r',newline='') as f :
        user_info = list(csv.reader(f))
    with open('cps109_a1_output.csv','w',newline='') as f :
        w = csv.writer(f)
        users = []
        for i in user_info :
           users.append(i[0])  #list of current users
        if username not in users : #checking if new user or not
            user_info.append([username,0,0])
        w.writerows(user_info)
  

def marker_assign():
    """
    Function to assign the player a marker of choice
    """
    while True :
        player_marker=  input("Choose X or O : ").upper()
        if player_marker not in 'XO' :  #checks if marker is valid
            print("Only X or O can be used as a marker")
            continue
        else :
            break
    return player_marker

def check_win(grid) :
    """
    Function to check for wins
    """
    for i in range(0,9,3) :
        if grid[i] == grid[i+1] == grid[i+2] != ' ':
            return True, grid[i]
    for i in range(0,3) :
        if grid[i] == grid[i+3] == grid[i+6] != ' ' :
            return True , grid[i]
    if grid[0] == grid[4] == grid[8] != ' ' :
        return True, grid[0]
    if grid[2] == grid[4] == grid[6] != ' ':
        return True, grid[2]
    
    return False , None


assert check_win(['X', 'O', 'X', 'O', 'O', 'O', 'X', 'X', ' ']) == (True,'O')
#Main Program 
if __name__ == '__main__' :
    #Initial setup
    grid = [' ',' ',' ',' ',' ',' ',' ',' ',' '] #empty grid
    s = [x for  x in range(0,9)]  #List to keep track of empty cells
    print("Welcome to Tic Tac Toe!") #Output to start the game 
    
    #Getting user information
    username = input("Enter your username: ") #Takes username from user
    new_user(username)
    player_marker = marker_assign() #To assign the player a marker
    
    if player_marker == 'X': #if-else to assign the computer the other marker
        turn = 1
        comp_marker = 'O' 
    else :
        comp_marker = "X"
        turn = 0
    win = False
    while not win : #playing turns start here onwards
        if turn % 2 != 0 : #Player plays when turn is odd
            cell = int(input('Enter your move (cells numbered 0-8): '))
            if cell not in range(0,9) : #to make sure correct input
                print('Only Enter numbers between 0-8')
                continue
            elif cell not in s : #to make sure the cell entered is available
                print('Cell occupied, try another')
                continue
            grid[cell] = player_marker #assigning the marker to respective cell
            s.remove(cell)
            display_grid(grid)
            turn += 1
        else : #Computer plays when turn is even
            computer_turn(s, comp_marker)
            display_grid(grid)
            turn += 1
            
        win, marker= check_win(grid) #checks if there is a win and returns winning marker
        if win == False and len(s) == 0 : #to check for a tie
            print("Its a tie.")
            break
    print("Game Over!")
    if win == True:
        if marker == player_marker :
            print('Winner is',username)
        else  :
            print("Computer Wins")
    l = user_history(username, win) #getting user info
    print(f'Wins: {l[1]} \t Losses: {l[2]}') #displaying the user stats