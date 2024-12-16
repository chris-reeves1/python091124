import matplotlib.pyplot as plt
import numpy as np

# Define the chessboard
def draw_chessboard():
    fig, ax = plt.subplots(figsize=(8, 8))
    for x in range(8):
        for y in range(8):
            color = 'white' if (x + y) % 2 == 0 else 'gray'
            rect = plt.Rectangle((x, y), 1, 1, facecolor=color, edgecolor='black')
            ax.add_patch(rect)
    ax.set_xlim(0, 8)
    ax.set_ylim(0, 8)
    ax.set_xticks(np.arange(0.5, 8.5, 1))
    ax.set_yticks(np.arange(0.5, 8.5, 1))
    ax.set_xticklabels(range(1, 9))
    ax.set_yticklabels('ABCDEFGH')
    ax.grid(False)
    return ax

# Knight's movement visualization using circles
def draw_knight_moves(ax, position):
    x, y = position
    moves = [(x+2, y+1), (x+2, y-1), (x-2, y+1), (x-2, y-1),
             (x+1, y+2), (x+1, y-2), (x-1, y+2), (x-1, y-2)]
    for mx, my in moves:
        if 0 <= mx < 8 and 0 <= my < 8:  # Ensure moves are within the board
            circle = plt.Circle((mx + 0.5, my + 0.5), 0.4, color='blue', alpha=0.5)
            ax.add_patch(circle)

# Queen and Bishop's movement visualization using triangles
def draw_bishop_moves(ax, position):
    x, y = position
    for dx, dy in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
        for step in range(1, 8):
            mx, my = x + step * dx, y + step * dy
            if 0 <= mx < 8 and 0 <= my < 8:
                triangle = plt.Polygon([(mx + 0.5, my + 0.5), 
                                        (mx + 1, my), 
                                        (mx, my + 1)], color='green', alpha=0.5)
                ax.add_patch(triangle)

# Rook's movement visualization using squares
def draw_rook_moves(ax, position):
    x, y = position
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        for step in range(1, 8):
            mx, my = x + step * dx, y + step * dy
            if 0 <= mx < 8 and 0 <= my < 8:
                square = plt.Rectangle((mx, my), 1, 1, color='red', alpha=0.3)
                ax.add_patch(square)

# Example usage
def visualize_chess():
    ax = draw_chessboard()

    # Add pieces and visualize their moves
    knight_position = (3, 3)
    draw_knight_moves(ax, knight_position)

    bishop_position = (2, 2)
    draw_bishop_moves(ax, bishop_position)

    rook_position = (5, 5)
    draw_rook_moves(ax, rook_position)

    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

visualize_chess()
