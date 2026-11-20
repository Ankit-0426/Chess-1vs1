"""
Graphical grid logic and image loading adapted from Eddie Sharick's YouTube tutorial: ["https://youtu.be/EnYui0e73Rs"]
and 
"""
import pygame
from sys import exit

board = [
    ["bR","bN","bB","bQ","bK","bB","bN","bR"],
    ["bP","bP","bP","bP","bP","bP","bP","bP"],
    ["..","..","..","..","..","..","..",".."],
    ["..","..","..","..","..","..","..",".."],
    ["..","..","..","..","..","..","..",".."],
    ["..","..","..","..","..","..","..",".."],
    ["wP","wP","wP","wP","wP","wP","wP","wP"],
    ["wR","wN","wB","wQ","wK","wB","wN","wR"]]

DIM = 8
WIDTH = 650
HEIGHT = 512
S_SIZE = HEIGHT // DIM

IMGS = {}

def load_images():
    pieces = ['wP', 'wR', 'wN', 'wB', 'wQ', 'wK', 'bP', 'bR', 'bN', 'bB', 'bQ', 'bK']
    for piece in pieces:
        IMGS[piece] = pygame.transform.scale(pygame.image.load(f"images/{piece}.png"), (S_SIZE,S_SIZE))

def main():
    
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("CS50x Chess")
    clock = pygame.time.Clock()
    load_images()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        draw_gamestate(screen)
        pygame.display.flip()
        clock.tick(60)

def draw_gamestate(screen):
    
    draw_board(screen)

    draw_pieces(screen)

def draw_board(screen):
    clrs = [pygame.Color((235, 236, 208)), pygame.Color((119, 149, 86))]
    
    for r in range(DIM):
        for c in range(DIM):
            clr = clrs[((r + c)%2)]
            pygame.draw.rect(screen, clr, pygame.Rect(c*S_SIZE, r*S_SIZE, S_SIZE, S_SIZE))

def draw_pieces(screen):
    for r in range(DIM):
        for c in range(DIM):
            piece = board[r][c]
            if piece != "..":
                screen.blit(IMGS[piece],(c*S_SIZE, r*S_SIZE))


if __name__ == "__main__":
    main()
        
