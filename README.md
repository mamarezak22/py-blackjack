# Blackjack CLI Game 🃏

A simple **Blackjack-style card game** in Python where you play against an AI.  
This game runs in the terminal and uses **pretty card symbols** for suits.

---

## Features

- Play multiple rounds against a computer AI.
- Tracks **round points** and **total rounds won**.
- Beautiful card display using suit symbols:
  - ♥, ♦, ♣, ♠
- Clear scoreboard after each round.
- Easy-to-read terminal interface with emojis.

---

## How to Play

1. Run the game:
   ```bash
   python main.py
   ```
2. During each round:
   - You draw cards one by one.
   - Type `y` to draw another card, `n` to stop.
   - Try to get as close to 21 points as possible without going over.
3. After each round:
   - Your points and AI points are displayed.
   - Round winner is shown.
   - Overall scoreboard updated.
4. Decide if you want to play another round by typing `y` or `n`.

---

## Rules

- Number cards are worth their number.
- Jack = 11, Queen = 12, King = 13.
- AI draws cards until it reaches at least 17 points.
- Winner of the round is whoever is closest to 21 without exceeding it.

---

## Example Gameplay

```
🃏 Card 1: ♥ 7  → Total: 7
🃏 Card 2: ♠ King → Total: 20

==============================
🃏 ROUND RESULT
🧑 Your points : 20
🤖 AI points   : 18
==============================

------------------------------
🏁 SCOREBOARD
🧑 You : 2 rounds
🤖 AI  : 1 rounds
------------------------------
```

---

## Project Structure

```
.
├── main.py          # Entry point, handles multiple rounds
├── functions.py     # Game logic: drawing cards, calculating points, determining winner
├── cards.py         # Card class and deck creation
└── README.md        # This file
```

---

## Requirements

- Python 3.8+
- No external libraries needed (uses standard library only)

---

Have fun and try to beat the AI! 🎉
