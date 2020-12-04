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

            add4 = int(input('Players Games They Have Started In: '))
            new_player.setStarted(add4)

            add5 = int(input('Players Minutes Played This Season: '))
            new_player.setMinutesPlayed(add5)
            
            add6 = int(input('Players Feild Goals Made This Season: '))
            new_player.setFieldGoals(add6)

            add7 = int(input('Players Feild Goal Attempts This Season: '))
            new_player.setFGA(add7)

            add8 = int(input('Players Feild Goal Percentage: '))
            new_player.setFGP(add8)

            add9 = int(input('Players 3-Pointers Made: '))
            new_player.set3P(add9)

            add10 = int(input('Players 3-Pointers Attempted: '))
            new_player.set3PA(add10)

            add11 = int(input('Players 3-Pointer Percentage: '))
            new_player.set3PP(add11)

            add12 = int(input('Players 2-Pointers Made: '))
            new_player.set2P(add12)
            
            add13 = int(input('Players 2-Pointer Percentage: '))
            new_player.setTPA(add13)

            add14 = int(input('Players Free Throws Made: '))
            new_player.setFreeThrows(add14)

            add15 = int(input('Players Free Throw Attempts: '))
            new_player.setFTA(add15)

            add16 = int(input('Players Free Throw Percentage: '))
            new_player.setFTP(add16)

            add17 = int(input('Players Offesive-Rebounds This Season: '))
            new_player.setORB(add17)

            add18 = int(input('Players Defensive-Rebounds This Season: '))
            new_player.setDRB(add18)

            add19 = int(input('Players Total-Rebounds This Season: '))
            new_player.setTRB(add19)

            add20 = int(input('Players Total Assists This Season: '))
            new_player.setAST(add20)

            add21 = int(input('Players Total Steals This Season: '))
            new_player.setSTL(add21)

            add22 = int(input('Players Total Blocks This Season: '))
            new_player.setBLK(add22)

            add23 = int(input('Players Total Turnovers This Season: '))
            new_player.setTOV(add23)

            add24 = int(input('Players Total Personal Fouls This Season: '))
            new_player.setPF(add24)

            add25 = int(input('Players Total Points: '))
            new_player.setPPG(add25)

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

