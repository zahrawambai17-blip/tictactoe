import random

_AIname = "larry the robot"

AI_WIN_MESSAGES = [
    "{ai} wins this round. Do better next time, {name}!",
    "{ai} is better than you, {name}. womp womp!!!",
]
PLAYER_WIN_MESSAGES = [
    "you are the GOAT, {name}! You beat {ai}!",
    "{name} is The winner {ai} better training needed.",
]
TIE_MESSAGES = [
    "A draw! {name} and {ai} are evenly matched.",
    "Draws are for the mediocre. Rematch?",
]

_winlines = [ (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6),
]
def _welcome():
    print("=" * 40)
    print("      Welcome to tic tac toe")
    print("=" * 40)
    print("this are how the sqaures are numbered:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    
def _newboard():
    return [" "] * 9
def _printboard(board):
    print()
    for row in range(3):
        x, y, z = board[row * 3 : row * 3 + 3]
        print(f" {x} | {y} | {z} ")
        if row < 2:
            print("---+---+---")
    print()

def _checkwinner(board):
    for x, y, z in _winlines:
        if board[x] != " " and board[x] == board[y] == board[z]:
            return board[x]
    return None

def a_tie(board):
    return " " not in board and _checkwinner(board) is None

def _humanmove(board):
    while True:
        word = input("your turn (1-9): ").strip()
        if word.isdigit() and 1 <= int(word) <= 9 and board[int(word) - 1] ==" ":
            return int(word) - 1
        print("wrong move. choose an empty square (1-9)")
        
def _twoplayers():
    board = _newboard()
    player = "X"
    while True:
        _printboard(board)
        print(f"player {player}")
        board[_humanmove(board)] = player
        if _checkwinner(board):
            _printboard(board)
            print(f"{player} wins")
            return
        if a_tie(board):
            _printboard(board)
            print("it is a draw")
            return
        player = "O" if player == "X" else "X"
        

class QAgent:
    def __init__(self, alpha=0.3, gamma=0.9, epsilon=0.2):
        self.q = {}
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon

    def get_q(self, state, action):
        return self.q.get((state, action), 0.0)

    def _chooseaction(self, board, explore=True):
        moves = [i for i, c in enumerate(board) if c == " "]
        if explore and random.random() < self.epsilon:
            return random.choice(moves)
        state = "".join(board)
        best = max(self.get_q(state, m) for m in moves)
        return random.choice([m for m in moves if self.get_q(state, m) == best])

    def update(self, state, action, reward, next_state, next_moves):
        future = 0.0
        if next_state is not None and next_moves:
            future = max(self.get_q(next_state, m) for m in next_moves)
        old = self.get_q(state, action)
        self.q[(state, action)] = old + self.alpha * (reward + self.gamma * future - old)


def train(agent, episodes=50000):
    for _ in range(episodes):
        board = _newboard()
        while True:
            state = "".join(board)
            action = agent._chooseaction(board, explore=True)
            board[action] = "X"

            if _checkwinner(board) == "X":
                agent.update(state, action, 1.0, None, [])
                break
            if a_tie(board):
                agent.update(state, action, 0.5, None, [])
                break

            empty = [i for i, c in enumerate(board) if c == " "]
            board[random.choice(empty)] = "O"

            if _checkwinner(board) == "O":
                agent.update(state, action, -1.0, None, [])
                break
            if a_tie(board):
                agent.update(state, action, 0.5, None, [])
                break

            new_moves = [i for i, c in enumerate(board) if c == " "]
            agent.update(state, action, 0.0, "".join(board), new_moves)


def _playgame(agent, name):
    board = _newboard()
    while True:
        board[agent._chooseaction(board, explore=False)] = "X"
        print(f"{_AIname} moved:")
        _printboard(board)
        if _checkwinner(board) == "X":
            print(random.choice(AI_WIN_MESSAGES).format(ai=_AIname, name=name))
            return
        if a_tie(board):
            print(random.choice(TIE_MESSAGES).format(ai=_AIname, name=name))
            return

        board[_humanmove(board)] = "O"
        _printboard(board)
        if _checkwinner(board) == "O":
            print(random.choice(PLAYER_WIN_MESSAGES).format(ai=_AIname, name=name))
            return
        if a_tie(board):
            print(random.choice(TIE_MESSAGES).format(ai=_AIname, name=name))
            return

def main():
    _welcome()
    name = input("enter name:").strip()
    if name == "":
        name = "Player"
    agent = QAgent()
    print(f"\nWelcome!!, {name}! {_AIname} is training, please wait...")
    train(agent)
    print(f"Training complete. You are O, {_AIname} is X.")
    while True:
        _playgame(agent, name)
        again = input("Play again? (yes/no): ").lower().strip()
        if again != "yes":
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()
        


        
