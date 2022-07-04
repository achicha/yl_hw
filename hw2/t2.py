from typing import List
import random


class Game:
    def __init__(self, board_length=10, loss_series=5, player1='X', player2='O'):
        self.length = board_length
        self.loss_series = loss_series
        self.mark_player1 = player1
        self.mark_player2 = player2
        self.padding = len(str(board_length)) + 1
        self.board = self.init_board(length=board_length)
        self.moves_history_player2 = []
        self.moves_history_player1 = []
        self.player1_loss = False
        self.player2_loss = False
        print(f"""
        Игра обратные крестики-нолики» на поле {self.length}x{self.length}
        проигрывает тот, у кого получился вертикальный, горизонтальный 
        или диагональный ряд из пяти своих фигур (крестиков/ноликов).
        """)

    @staticmethod
    def init_board(length: int):
        """init board from 1 to length*length"""
        output = []
        for i in range(length):
            output.append([j for j in range(length * i + 1, length * (i+1)+1)])
        return output

    @staticmethod
    def stop_game(lst: List, mark_to_search: str, num: int) -> bool:
        for line in lst:
            if line.count(mark_to_search) >= num:
                return True
        return False

    def next_move(self, x: int, is_player1: bool) -> bool:
        """add next move to history person/bot"""
        if x > self.length * self.length or x < 1:
            print(f'x should be between 1 and {self.length * self.length}')
            return False
        if x in self.moves_history_player1 or x in self.moves_history_player2:
            print(f'{x} already exist. please choose another cell')
            return False

        if is_player1:
            self.moves_history_player1.append(x)
        else:
            self.moves_history_player2.append(x)
        return True

    def bot_move_choice(self) -> int:
        """random algorithm to choose next move"""
        flatten = [x for xs in self.board for x in xs]
        free_cells = list(set(flatten) - set(self.moves_history_player1) - set(self.moves_history_player2))
        return random.choice(free_cells)

    def check_loss(self, moves_history: List[int], is_player1: bool):
        """check if any players already loss the game"""
        mark = self.mark_player1 if is_player1 else self.mark_player2
        rows = self.get_current_board_state()

        if len(moves_history) >= self.loss_series:
            cols = [[] for _ in range(self.length)]
            fdiag = [[] for _ in range(self.length + self.length - 1)]
            bdiag = [[] for _ in range(len(fdiag))]
            min_bdiag = -self.length + 1

            for x in range(self.length):
                for y in range(self.length):
                    cols[x].append(rows[y][x])
                    fdiag[x + y].append(rows[y][x])
                    bdiag[x - y - min_bdiag].append(rows[y][x])

            is_loss = any([
                self.stop_game(rows, mark, self.loss_series),
                self.stop_game(cols, mark, self.loss_series),
                self.stop_game(fdiag, mark, self.loss_series),
                self.stop_game(bdiag, mark, self.loss_series),
            ])

            if is_player1:
                self.player1_loss = is_loss
            else:
                self.player2_loss = is_loss

    def get_updated_line(self, line: List[int]) -> List:
        """check exist moves and fill in current line"""
        output = []
        for i in line:
            if i in self.moves_history_player1:
                output.append(self.mark_player1)
            elif i in self.moves_history_player2:
                output.append(self.mark_player2)
            else:
                output.append(i)
        return output

    def get_current_board_state(self) -> List:
        """get current board state to see all existing moves"""
        return [self.get_updated_line(line) for line in self.board]

    def draw_board(self):
        """print out current state of board"""
        for idx, line in enumerate(self.get_current_board_state()):
            line_ = '|' + '|'.join([str(x).center(self.padding) for x in line]) + '|'
            if idx == 0:
                print('-' * len(line_))
            print(line_)
            print('-' * len(line_))


if __name__ == '__main__':
    b = Game(board_length=10, loss_series=5, player1='X', player2='O')

    while True:
        b.draw_board()
        number = input(f'Type a cell number where to place your mark {b.mark_player1}?')
        try:
            number = int(number)
        except BaseException:
            print(f'try to input number from 1 to {b.length * b.length}')
            continue

        # human move
        p1 = b.next_move(number, is_player1=True)
        if not p1:
            continue

        b.check_loss(b.moves_history_player1, is_player1=True)
        if b.player1_loss:
            print('player1 loss')
            break

        # bot move
        p2 = b.next_move(b.bot_move_choice(), is_player1=False)
        if not p2:
            continue

        b.check_loss(b.moves_history_player2, is_player1=False)
        if b.player2_loss:
            print('player2 loss')
            break
