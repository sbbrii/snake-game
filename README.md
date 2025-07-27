

# 🐍 Retro Snake Game (Python + Pygame)

A classic **Snake Game** built using **Python** and **Pygame**.
Guide the green snake to eat apples and grow longer, but avoid hitting the edges or yourself!



## 🎮 Features

✅ Retro‑style snake gameplay
✅ Score tracking
✅ Smooth movement and growth mechanics
✅ Randomized food placement (no overlap with snake body)
✅ Game over detection (walls and self‑collision)




## 🛠️ Requirements

* Python 3.x
* Pygame library

Install Pygame via pip if you haven’t already:

```bash
pip install pygame
```





## 🎯 Controls

| Key   | Action     |
| ----- | ---------- |
| **W** | Move Up    |
| **S** | Move Down  |
| **A** | Move Left  |
| **D** | Move Right |

*Press any movement key after Game Over to restart.*



## ✨ Customization

You can tweak these variables in `main.py` to change gameplay:

```python
cell_size = 30    # Size of each grid cell
no_cells = 25     # Number of cells in one row/column
OFFSET = 75       # UI offset around the board
```

You can also change `SNAKE_UPDATE` timer speed to make the snake faster/slower:

```python
pygame.time.set_timer(SNAKE_UPDATE, 200)  # 200 ms per move
```

---

## 🏗️ Future Improvements

* Add levels or increasing speed
* Add sound effects
* Implement a high‑score system
* Add a pause menu

---

**Enjoy the game!** 🎉🐍🍎
If you like this project, feel free to ⭐ it or contribute!

