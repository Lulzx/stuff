# Main fucntion
def Run():

    # Constants
    STARTING_CHIPS = 21
    MIN_CHIPS = 1
    SCORES = 1
    NAMES = 0
    FIRST_PLAYER = 0

    # Variables
    max_chips = 3
    playersJoined = 0
    players = ([],[])
    draw = []
    roundNumber = 1
    numberOfRounds = 0
    pileOfChips = 0
    turns = 0
    whichPlayer = 0
    winnerCheck = 1
    chipsToRemove = 0
    draw = []
    name = ''
    winnerName = ''
    winnerScore = 0
    winnerName = ''
    playersInDraw = 0
    numberOfPlayers = 0

    # Start of game outputs
    print('\n====================== NEW GAME ==========================\n')
    print('Type "[ctrl]+[c]" at any time to return to home screen', end='\n\n')
    print('This is a simple game which involves two players taking chips away from a pile. Each player has one turn each, where they may take one, two or three chips away from the pile before the next player has a turn. The winner is dictated by the person who takes away the 21st chip (which will be the last chip in the pile).', end='\n\n')

    # Getting number of players
    while numberOfPlayers < 2:

        playerFail = False
        playerInput = input('Please enter the number of players: ')

        # Testing input
        try:
            numberOfPlayers = int(playerInput)
            print()

        # Not a number
        except ValueError:
            print('\nSorry, the number of players must be an integer.', end='\n\n')
            playerFail = True

        # Checking number
        if (numberOfPlayers < 2 or numberOfPlayers > 10) and not playerFail:
            print('\nSorry, the number of players must be between 2 and 10. Please try again.', end='\n\n')  
            
    # Getting users names
    while name == '' or name in players[NAMES] and playersJoined < numberOfPlayers:

        name = input('Please enter your name: ')

        # Testing name
        if name == '':
            print('\nSorry, your name cannot be blank. Please try again.', end='\n\n')

        elif name in players[NAMES]:
            print('\nSorry, you cannot have the same name as another player. Please try again', end='\n\n')

        # If valid name
        else:
            # Add player
            players[NAMES].append(name)
            players[SCORES].append(0)
            print('\nWelcome ' + name + '. Enjoy the game.', end='\n\n')
            playersJoined += 1

    # Getting number of rounds to play
    while numberOfRounds < 1:

        roundFail = False
        roundsInput = input('Please enter the number of rounds you wish to play: ')

        # Testing input
        try:
            numberOfRounds = int(roundsInput)

        # Not a number
        except ValueError:
            print('\nSorry, the number of rounds must be an integer.', end='\n\n')
            roundFail = True

        # Checking number
        if numberOfRounds < 1 and not roundFail:
            print('\nSorry, the number of rounds must be higher than 0. Please try again.', end='\n\n')

    # Starting game
    while roundNumber <= numberOfRounds:

        # Reset game values
        pileOfChips = STARTING_CHIPS
        whichPlayer = FIRST_PLAYER - 1
        turns = 0

        print('\n******************** ROUND', roundNumber, '********************')

        # Starting round 
        while pileOfChips > 0:

            # New player
            whichPlayer += 1

            # Loop back to first player
            if whichPlayer >= numberOfPlayers:
                whichPlayer = FIRST_PLAYER

            print('\n---------------- ' + players[NAMES][whichPlayer] + "'s, turn -----------------", end='\n\n')
            print('There is', pileOfChips, 'chip(s) remaining.', end='\n\n')

            # Reset chips to remove
            chipsToRemove = 0

            # Take away chips
            while chipsToRemove <= 0 or chipsToRemove > 3:

                # Set maximum to take away
                if pileOfChips <= 3:
                    max_chips = pileOfChips
                else:
                    max_chips = 3

                chipFail = False
                chipsInput = input('How many chips do you wish to remove: ')

                # Check input
                try:
                    chipsToRemove = int(chipsInput)
                    
                # When not a number
                except ValueError:
                    print('\nSorry, the chips you wish to remove must be an integer.', end='\n\n')
                    chipFail = True

                # Test input
                if chipsToRemove > max_chips or chipsToRemove < MIN_CHIPS and not chipFail:
                    print('\nSorry, you may only take a maximum of', max_chips, 'chip(s), and a minimum of', MIN_CHIPS, 'chip. Please try again.', end='\n\n')
                    chipsToRemove = 0

            # Take away the chips
            pileOfChips -= chipsToRemove

            # Switch next turn
            turns += 1

        # End of round score
        players[SCORES][whichPlayer] += 1

        print('\n****************** ROUND OVER ******************', end='\n\n')
        print('It took', turns, 'turns.', players[NAMES][whichPlayer], 'is the winner of this round.', end='\n\n')
        print('You have played', roundNumber, 'round(s).', end='\n\n')

        # Loop through players
        playersJoined -= numberOfPlayers
        while playersJoined < numberOfPlayers:
            print(players[NAMES][playersJoined] + "'s score is: ", players[SCORES][playersJoined])
            playersJoined += 1

        # Set number of player back
        playersJoined = numberOfPlayers

        # New round
        roundNumber += 1

    # Identifying the winners
    winnerScore = players[SCORES][FIRST_PLAYER]
    winnerName = players[NAMES][FIRST_PLAYER]

    draw = [FIRST_PLAYER]

    # Checking players scores
    while winnerCheck < numberOfPlayers:
        if players[SCORES][winnerCheck] > winnerScore:

            # Set new winner
            winnerScore = players[SCORES][winnerCheck]
            winnerName = players[NAMES][winnerCheck]
            draw = []

        elif players[SCORES][winnerCheck] == winnerScore:

            # Add a draw
            draw.append(winnerCheck)

        winnerCheck += 1

    # Outputting winners
    print('\n====================== GAME OVER ========================', end='\n\n')
    
    # Outputting draw
    if len(draw) > 1:
        while playersInDraw < len(draw):
            print(players[NAMES][draw[playersInDraw]], end=', ')
            if playersInDraw == len(draw) - 2:
                print('and ', end='')
            playersInDraw += 1
        print('drew this game with scores of', winnerScore, end='\n\n')

    # Outputting individual
    else:
        print(winnerName, 'won this game with a score of', winnerScore, end ='\n\n')

    # End game
    input("---Press [ctrl]+[c] to return to home screen, or [ENTER] key to close---\n")
