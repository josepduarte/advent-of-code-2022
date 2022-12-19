with open('input.txt', 'r') as f:
    lines = f.readlines()

############
#  PART 1  #
############
print('> Part 1')

class OpponentMove(object):
    ROCK = 'A'
    PAPER = 'B'
    SCISSORS = 'C'
    

class MyMove(object):
    ROCK = 'X'
    PAPER = 'Y'
    SCISSORS = 'Z'


class ScorePoints(object):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    WIN = 6
    DRAW = 3
    LOSE = 0

MOVES_OUTCOMES = {
    MyMove.ROCK: {
        OpponentMove.ROCK: ScorePoints.ROCK + ScorePoints.DRAW,
        OpponentMove.PAPER: ScorePoints.ROCK + ScorePoints.LOSE,
        OpponentMove.SCISSORS: ScorePoints.ROCK + ScorePoints.WIN,
    },
    MyMove.PAPER: {
        OpponentMove.ROCK: ScorePoints.PAPER + ScorePoints.WIN,
        OpponentMove.PAPER: ScorePoints.PAPER + ScorePoints.DRAW,
        OpponentMove.SCISSORS: ScorePoints.PAPER + ScorePoints.LOSE,
    },
    MyMove.SCISSORS: {
        OpponentMove.ROCK: ScorePoints.SCISSORS + ScorePoints.LOSE,
        OpponentMove.PAPER: ScorePoints.SCISSORS + ScorePoints.WIN,
        OpponentMove.SCISSORS:ScorePoints.SCISSORS +  ScorePoints.DRAW,
    },
}

# MAIN
score = 0
for opponent_move, my_move in (l.strip().split(' ') for l in lines):
    score += MOVES_OUTCOMES[my_move][opponent_move]

print(score)

############
#  PART 2  #
############
print('> Part 2')

class ExpectedOutcome(object):
    LOSE = 'X'
    DRAW = 'Y'
    WIN = 'Z'


MOVES_OUTCOMES = {
    OpponentMove.ROCK: {
        ExpectedOutcome.LOSE: ScorePoints.SCISSORS + ScorePoints.LOSE,
        ExpectedOutcome.WIN: ScorePoints.PAPER + ScorePoints.WIN,
        ExpectedOutcome.DRAW: ScorePoints.ROCK + ScorePoints.DRAW,
    },
    OpponentMove.PAPER: {
        ExpectedOutcome.LOSE: ScorePoints.ROCK + ScorePoints.LOSE,
        ExpectedOutcome.WIN: ScorePoints.SCISSORS + ScorePoints.WIN,
        ExpectedOutcome.DRAW: ScorePoints.PAPER + ScorePoints.DRAW,
    },
    OpponentMove.SCISSORS: {
        ExpectedOutcome.LOSE: ScorePoints.PAPER + ScorePoints.LOSE,
        ExpectedOutcome.WIN: ScorePoints.ROCK + ScorePoints.WIN,
        ExpectedOutcome.DRAW: ScorePoints.SCISSORS + ScorePoints.DRAW,
    },
}

# MAIN
score = 0
for opponent_move, my_move in (l.strip().split(' ') for l in lines):
    score += MOVES_OUTCOMES[opponent_move][my_move]

print(score)
