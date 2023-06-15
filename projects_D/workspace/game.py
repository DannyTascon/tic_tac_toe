import pygame
import random

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((300, 300))
        pygame.display.set_caption("Tic-Tac-Toe")
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.turn = "X"

    def draw_board(self):
        for i in range(3):
            for j in range(3):
                pygame.draw.rect(self.screen, (255, 255, 255), (i * 100, j * 100, 100, 100), 1)

    def handle_input(self, pos):
        i, j = pos[0] // 100, pos[1] // 100
        if self.board[i][j] is None:
            self.board[i][j] = self.turn
            self.turn = "O" if self.turn == "X" else "X"

    def check_win(self):
        for row in self.board:
            if row[0] == row[1] == row[2] and row[0] is not None:
                return True
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] is not None:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] is not None:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] is not None:
            return True
        return False

    def computer_move(self):
        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] is None]
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.board[i][j] = self.turn
            self.turn = "X"

    def update_display(self):
        self.screen.fill((0, 0, 0))
        self.draw_board()
        for i in range(3):
            for j in range(3):
                if self.board[i][j] is not None:
                    font = pygame.font.Font(None, 100)
                    text = font.render(self.board[i][j], True, (255, 255, 255))
                    self.screen.blit(text, (i * 100 + 30, j * 100 + 20))
        pygame.display.flip()

    def restart_game(self):
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.turn = "X"

    def game_loop(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.turn == "X":
                        self.handle_input(pygame.mouse.get_pos())
                        if self.check_win():
                            print("Player X wins!")
                            self.restart_game()
                        else:
                            self.computer_move()
                            if self.check_win():
                                print("Computer wins!")
                                self.restart_game()
            self.update_display()
            pygame.time.delay(100)
