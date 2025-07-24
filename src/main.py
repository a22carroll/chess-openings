import chess
from openings import openings

def play_opening(opening_name, moves):
    print(f"Opening: {opening_name}")
    board = chess.Board()

    for i, move_san in enumerate(moves, 1):
        move = board.parse_san(move_san)
        board.push(move)
        print(f"\nMove {i}: {move_san}")
        print(board)
        input("Press Enter for next move...")

    print("\nOpening sequence complete!")

def main():
    print("Available openings:")
    for i, name in enumerate(openings.keys(), 1):
        print(f"{i}. {name}")

    choice = input("Enter the number of the opening you want to practice: ")
    try:
        choice_num = int(choice)
        opening_name = list(openings.keys())[choice_num - 1]
        moves = openings[opening_name]
        play_opening(opening_name, moves)
    except (ValueError, IndexError):
        print("Invalid selection. Exiting.")

if __name__ == "__main__":
    main()