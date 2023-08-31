import random

list_of_games = {}
display_list_of_games = []
NumberGamesAdded = {

}

UsersVoted = {

}

max_votes = -1
most_voted_game = None

def get_response(message: str, user: str) -> str:
    p_message = message.lower()
    



    if p_message == '!help':
        return '```Usable Commands \n 1. !addgame  \n 2. !list  \n 3. !clear  \n 4. !vote  \n 5. !finish ``` '
    
    if message == 'roll':
        return str(random.randint(1, 6))
    
    if p_message[:8] == "!addgame":
        print ("etst")
        NumberGamesAdded[user] = NumberGamesAdded.get(user, 0) + 1
        print (NumberGamesAdded[user])

        if NumberGamesAdded[user] > 3:
            return "You have added to many games"


    
        Game = p_message[9:]

        if Game in list_of_games:
            NumberGamesAdded[user] = NumberGamesAdded.get(user, 0) - 1


            return "game already in list"

        list_of_games[Game] = list_of_games.get(Game, 0)
        display_list_of_games.append(Game)


        print (Game)
        return "game toegevoegd"

    if p_message == "!list":
        return list_of_games


    if p_message == "!clear":
        list_of_games.clear()
        display_list_of_games.clear()
        NumberGamesAdded.clear()
        UsersVoted.clear()
        return "list cleared"

    if p_message[:5] == "!vote":
        UsersVoted[user] = UsersVoted.get(user, 0) + 1
        if UsersVoted[user] > 1:
            return "You have voted to many times"
        Games = p_message[6:]
        NewGames = Games.split(", ")
        votePoints = 3
        
        for i in NewGames:
            if i in list_of_games:
                list_of_games[i] = list_of_games.get(i, 0) + votePoints
                votePoints = votePoints - 1
        return NewGames

    if p_message == "!finish":
        max_votes = 0
        for game, votes in list_of_games.items():
            if votes > max_votes:
                max_votes = votes
                most_voted_game = game
        return "the game with the most votes is: " + most_voted_game
        


    