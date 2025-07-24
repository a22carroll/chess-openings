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
    keep_playing = True
    while(keep_playing):
        print("Available openings:")
        for i, name in enumerate(openings.keys(), 1):
            print(f"{i}. {name}")
        
        choice = input("Enter the number of the opening you want to practice: ")
        try:
            choice_num = int(choice)
            opening_name = list(openings.keys())[choice_num - 1]
            moves = openings[opening_name]
            play_opening(opening_name, moves)
            end_game = input("Do you want to quit? y/n ")
            if(end_game == "y"):
                keep_playing = False

        except (ValueError, IndexError):
            print("Invalid selection.")

if __name__ == "__main__":
    main()