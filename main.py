import pickle
import player_builder as pb 

def main():
# File 1
    with open("Glossary.txt", "r") as infile:
        glossary = infile.read().splitlines()
    


    menu_choice = '0'
    while menu_choice != 'Q' and menu_choice != 'q':
        print('Baseketball Players')
        print(' ======================')
        print(' 1) Add')
        print(' 2) Delete')
        print(' 3) Print')
        print(' 4) Save')
        print(' Q) Quit')
        print(' ======================')
        menu_choice = input(' 1.Add 2.Delete 3.Print 4.Save Q.Quit:')
        if menu_choice == '1':

            add1 = input('Players Name: ')
            first_name = (add1.split(" "))[0]
            new_player = pb(first_name)

            add2 = int(input('Players Age: '))
            new_player.setAge(add2)

            add3 = int(input('Players Games Played: '))
            new_player.setGames(add3)

            add4 = input('Players Games They Have Started In: ')

            add5 = input('Players Minutes Played This Season: ')

            add6 = input('Players Feild Goals Made This Season: ')

            add7 = input('Players Feild Goal Attempts This Season: ')

            add8 = input('Players Feild Goal Percentage: ')

            add9 = input('Players 3-Pointers Made: ')

            add10 = input('Players 3-Pointers Attempted: ')

            add11 = input('Players 3-Pointer Percentage: ')

            add12 = input('Players 2-Pointers Made: ')

            add13 = input('Players Free Throws Made: ')

            add14 = input('Players Free Throw Attempts: ')

            add15 = input('Players Free Throw Percentage: ')

            add16 = input('Players Offesive-Rebounds This Season: ')

            add17 = input('Players Defensive-Rebounds This Season: ')

            add18 = input('Players Total-Rebounds This Season: ')

            add19 = input('Players Total Assists This Season: ')

            add20 = input('Players Total Steals This Season: ')

            add21 = input('Players Total Blocks This Season: ')

            add22 = input('Players Total Turnovers This Season: ')

            add23 = input('Players Total Personal Fouls This Season: ')

            add24 = input('Players Total Points: ')

        if menu_choice == '2':
            # Delete            
        if menu_choice == '3':
            print(infile)
        if menu_choice == '4':
            with open("team.dat", "wb") as infile:
                pickle.dump(team, infile)
        elif menu_choice == 'Q' or menu_choice == 'q':
            print(' Goodbye')
        else:
            print(' Not a valid choice, try again.')

    #TODO Load Team file Format into player objects
        # Jeff 


    #TODO Player Average Function
        # Jeff

    #TODO Team Average Function

    #TODO Print Team List

    #TODO Print Rank Team members

    return 0


def getTeamAverage(team_dict):
    # For loop through a dictionary and call the player.printStat(stat) it will  

    #TODO

    #return average
    pass

def printTeam(team_dict):
    # For loop through a dictionary and call the player.printStats()

    #TODO

    return 0 #temp statement to separate things out. This isn't returning anything

def exportTeam(team_dict):

    #TODO export team to txt file formatted

    return 0 #temp statement to separate things out. This isn't returning anything

