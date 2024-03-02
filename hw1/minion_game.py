def minion_game(string): 
    kevin_score = 0 
    stuart_score = 0 
    for i in range(len(string)): 
        if string[i] in "AEIOU": 
            kevin_score += len(string) - i 
        else: 
            stuart_score += len(string) - i 
            if kevin_score > stuart_score: 
                winner = "Kevin" 
            elif stuart_score > kevin_score: 
                winner = "Stuart" 
            else: 
                winner = "Draw" 
                return winner, kevin_score if winner == "Kevin" else stuart_score 
            string = input() 
            winner, score = minion_game(string) 
            print(winner, score)