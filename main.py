# imports
import FantasyTeam as ft
import NFLPlayer as nflplayer
import requests
import numpy
import pandas as pd

"""
Fantasy table dataframe as a global so all the functions have access to the data frame
"""

fantasy_football_rankings_url = 'http://games.espn.com/ffl/leaders?&seasonTotals=true&seasonId=2018'

source = requests.get(fantasy_football_rankings_url).text

fantasy_table = pd.read_html(source)[0]

ranking_table = fantasy_table[fantasy_table.columns[0:8]]

# organize the dataframe
player_col = ranking_table[ranking_table.columns[0]]
player_passing_attempts = ranking_table[ranking_table.columns[2]]
player_passing_yards = ranking_table[ranking_table.columns[3]]
player_rushing_TD = ranking_table[ranking_table.columns[4]]
player_int = ranking_table[ranking_table.columns[5]]
player_rush_attempts = ranking_table[ranking_table.columns[7]]

# have a global dict that will hold all the team objects
# we will add team objects that contain player objects
global_teams = {}


def main():
    """"""

    print(ranking_table)

    print("--------------------------------------------")
    print("Welcome to Fantasy Manager")
    print("where you can select the players you want")
    print("to draft for next year on your fantasy team")
    print("--------------------------------------------")

    # entering the team management aspect of the program
    teamSettings()

# team settings
# provide user with GUI to edit their team

def teamSettings():
    """
    Function GUI for user to select and edit a particualr team
    """

    while True:
        try:

            print("--------------------------------------------")
            print("Press [A] to create a new team ->")
            print("Press [D] to delete a exisiting team ->")
            print("Press [P] to display all your teams ->")
            print("Press [E] to select and edit a team ->")
            print("Press [X] to exit from the program ->")
            print("--------------------------------------------")

            # check the user input
            print("--------------------------------------------")
            user_team_choice = input("Type in your option: ").lower()
            print("--------------------------------------------")

            if user_team_choice == 'a' or user_team_choice == 'A':
                # create a new team
                created_team = createTeam()

                # add the created team to the dictionary with the team name as the key and the actual team object as the value
                global_teams.update({created_team.name: created_team.fantasy_team})

                print(global_teams)

            elif user_team_choice == 'd' or user_team_choice == 'D':
                # delete the team within the array or dict
                deleteTeam()

            elif user_team_choice == 'p' or user_team_choice == 'P':
                # print the list/dict of all teams
                print(global_teams)

            elif user_team_choice == 'e' or user_team_choice == 'E':
                # go into edit that team -- make this a seperate function
                editTeam()

            elif user_team_choice == 'x' or user_team_choice == 'X':
                # exit out of the loop
                pass

            else:
                print("I did not understand that input, please enter a valid entry.")

        except ValueError as e:
            print(e)
            print("Enter a letter command")


def selectPlayer():
    """
    Function that traverses through a list and will select a player in the dataframe
    """
    pass


def createTeam():
    """
    Function to create a team from the team class
    """
    # define a new instance of the team object

    # ask the user to give his team a name
    user_team_name = input("Enter a team name for your fantasy team: ")

    new_team = ft.Team(user_team_name)

    return new_team


def deleteTeam():
    """
    Function that will take an a selected team name (string) that the user wants to delete and will delete that object from the dict
    """

    while True:
        try:
            user_delete_team = input("Enter the name of the team that you want to delete: ").lower()

            # loop through the global dict
            # if the user deleted selected team matches with the a team in the global dict
            # take it out/update the dict

            for team in global_teams:
                if user_delete_team not in global_teams:

                    print("Please enter a team that is already exsist")

                else:

                    del global_teams[user_delete_team]

                    print(global_teams)

                    return global_teams

        except ValueError or KeyError as e:
            print(e)
            print("Enter a valid input")
            print("That team does not exisit, enter a valud input")


def editTeam():
    """
    function that will get a specifc team from the global teams dict
    the user will be able to edit that specifc team
    """

    # ask the user for the team that they want to make edits to

    while True:
        try:

            user_selected_team = input("Enter the team name that you want to make edits too: ").lower()

            # loop through global teams
            # if the team is in the dict
            # create a GUI that will prompt the user
            # to add a player
            # delete player
            # and get the specifed stats

            for team in global_teams:
                if user_selected_team not in global_teams:
                    print("Enter a team that is already exsists")

                elif user_selected_team == team:
                    print(team)
                    # this should return the object that is based on the user string
                    return playerSettings(global_teams.get(user_selected_team))

                else:
                    print("Don't know how you got here")

        except ValueError as e:
            print(e)
            print("enter a valid input")


def playerSettings(current_team):
    """
    function that provides users with a GUI to add players to that spcific team
    """

    while True:
        try:
            print("---------------------------------------------------------")
            print("Press [A] to add a player to your team ->")
            print("Press [D] to delete a player from your team -> ")
            print("Press [P] to display the player's info -> ")
            print("Press [X] to quit making modifications to this team -> ")
            print("---------------------------------------------------------")

            user_selected_choice = input("Enter a player option from the menu: ").lower()

            if user_selected_choice == 'a' or user_selected_choice == 'A':
                new_nfl_player = createPlayer()

                # append this player to the current team
                updated_team = current_team.update({
                    'Player': new_nfl_player.getName()
                })

                print(global_teams)

                return updated_team

            elif user_selected_choice == 'd' or user_selected_choice == 'D':
                pass

            elif user_selected_choice == 'p' or user_selected_choice == 'p':
                print(f"Name: f{new_nfl_player.getName()}")
                print(f"Passing Attempts: f{new_nfl_player.getPassingAttempt()}")

            elif user_selected_choice == 'x' or user_selected_choice == 'X':

                break

            else:
                print("Please enter a valid option")

        except ValueError as e:
            print(e)
            print("Enter a valid input")


def createPlayer():
    """
    function that takes in the team the user is currently editing
    """

    # ask the user to enter the index number from the table
    # select player and add those contents to the table
    # create a NFL player instance

    while True:
        try:
            print("--------------------------------------------------------------------")
            print("Enter a index number on the NFL Ranking table to select that player")
            print("--------------------------------------------------------------------")

            user_selected_player_index = int(input("Enter index number: "))

            # player_col = ranking_table[ranking_table.columns[0]]
            # player_passing_attempts = ranking_table[ranking_table.columns[2]]
            # player_passing_yards = ranking_table[ranking_table.columns[3]]
            # player_rushing_TD = ranking_table[ranking_table.columns[4]]
            # player_int = ranking_table[ranking_table.columns[5]]
            # player_rush_attempts = ranking_table[ranking_table.columns[7]]

            user_player_name = player_col.iloc[user_selected_player_index]
            user_passing_attempt = player_passing_attempts.iloc[user_selected_player_index]
            user_passing_yards = player_passing_yards.iloc[user_selected_player_index]
            user_rushing_TD = player_rushing_TD.iloc[user_selected_player_index]
            user_int = player_int.iloc[user_selected_player_index]
            user_rush_attempts = player_rush_attempts.iloc[user_selected_player_index]

            # create a new player object and pass in these items when you define them
            user_created_player = nflplayer.Player(user_player_name, user_passing_attempt, user_passing_yards, user_rushing_TD, user_int, user_rush_attempts)

            # return the create player
            return user_created_player


        except ValueError as e:
            print(e)
            print("Enter a valid input.")


if __name__ == '__main__':
    main()