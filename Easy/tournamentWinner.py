def tournamentWinner(competitions, results):
    # Write your code here.
    tournament_results = {}  # dict
    highest_score = -1
    highest_scoring_team = ""

    for idx in range(len(competitions)):
        new_score = -1
        match = competitions[idx]
        match_result = results[idx]
        winner = None
        looser = None
        if match_result == 1:
            # Home team (i = 0) won
            winner = match[0]
            looser = match[1]
        else:
            # Away team (i = 1) won
            winner = match[1]
            looser = match[0]

        if winner in tournament_results:
            score = tournament_results.get(winner)
            new_score = score + 3
        else:
            new_score = 3
        if new_score > highest_score:
            highest_score = new_score
            highest_scoring_team = winner
        tournament_results[winner] = new_score

        if looser not in tournament_results:
            tournament_results[looser] = 0

    return highest_scoring_team


