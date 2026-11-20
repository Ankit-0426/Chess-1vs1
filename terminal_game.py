import os
import time
import chess


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def format_time(seconds):
    seconds = max(0, int(seconds))
    minutes, secs = divmod(seconds, 60)
    return f"{minutes:02d}:{secs:02d}"


def main():
    board = chess.Board()
    status_message = ""

    timers = {
        chess.WHITE: 600.0,
        chess.BLACK: 600.0,
    }

    while not board.is_game_over(claim_draw=True):
        clear_screen()
        print(board)
        print()
        print(f"White: {format_time(timers[chess.WHITE])}  |  Black: {format_time(timers[chess.BLACK])}")
        print()

        if status_message:
            print(status_message)
            print()
            status_message = ""

        turn_name = "White" if board.turn == chess.WHITE else "Black"
        opponent_name = "Black" if board.turn == chess.WHITE else "White"
        print(f"{turn_name}'s turn.")

        if board.is_check():
            print("Check!")

        turn_start = time.time()
        user_input = input(
            "Move (e.g. e2e4), 'moves', 'undo', 'draw', 'resign', or 'quit': "
        ).strip().lower()
        elapsed = time.time() - turn_start

        if user_input == "quit":
            print("Game ended early.")
            break

        timers[board.turn] -= elapsed
        if timers[board.turn] <= 0:
            clear_screen()
            print(board)
            print()
            print(f"Game Over — {opponent_name} wins! ({turn_name} ran out of time)")
            break

        if user_input == "resign":
            clear_screen()
            print(board)
            print()
            print(f"Game Over — {opponent_name} wins! ({turn_name} resigned)")
            break

        elif user_input == "draw":
            response = input(
                f"{opponent_name}, {turn_name} offers a draw. Accept? (y/n): "
            ).strip().lower()
            if response in ("y", "yes"):
                clear_screen()
                print(board)
                print()
                print("Game Over — It's a draw! (Draw by Agreement)")
                break
            else:
                status_message = f"{opponent_name} declined the draw offer."

        elif user_input == "undo":
            try:
                board.pop()
                status_message = "Last move undone."
            except IndexError:
                status_message = "No moves to undo!"

        elif user_input == "moves":
            legal = [move.uci() for move in board.legal_moves]
            status_message = "Legal moves: " + ", ".join(legal)

        else:
            try:
                board.push_uci(user_input)
            except ValueError:
                status_message = f"Illegal or invalid move: '{user_input}'. Try again."

    if board.is_game_over(claim_draw=True):
        clear_screen()
        print(board)
        print()

        outcome = board.outcome(claim_draw=True)
        if outcome.winner == chess.WHITE:
            winner = "White wins!"
        elif outcome.winner == chess.BLACK:
            winner = "Black wins!"
        else:
            winner = "It's a draw!"

        reason = outcome.termination.name.replace("_", " ").title()
        print(f"Game Over — {winner} ({reason})")


if __name__ == "__main__":
    main()