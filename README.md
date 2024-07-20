# Fantasy Cricket Game

This is a Fantasy Cricket game developed using Python. The game allows users to create a virtual team of real cricket players and score points based on the players' performances in real-life matches.

## Problem Statement

Create a Fantasy Cricket game in Python with the following features:
1. Opening screen of the application showing player categories.
2. Toolbar menu options to create a new team, open an existing team, save your team, and evaluate the score of a saved team.
3. Player selection interface where players can be added to or removed from the team.
4. Evaluation of the team score based on players' performance in selected matches.

## Features

- **Player Selection**: Create a new team, select players from different categories, and manage your team.
- **Score Evaluation**: Evaluate your team's score based on the performance of selected players in real matches.
- **User Interface**: A graphical user interface (GUI) to interact with the game, developed using PyQt5.

## Folder Structure

The repository contains the following folders:

1. **ui_files**: Contains the main UI files.
    - `EvaluateDialog.ui`
    - `GameWindow.ui`
    - `GetNameDialog.ui`
    - `MessageDialog.ui`

2. **python_scripts**: Contains the Python scripts for the UI files and additional scripts.
    - `evaluate_dialog.py`
    - `game_window.py`
    - `get_name_dialog.py`
    - `message_dialog.py`
    - `scoring.py` (for calculating the score)
    - `main_game.py` (for running the main game)
    - `cricket_database` (contains data of matches, teams, and their scores)

## Database Design

The database consists of three tables: `match`, `stats`, and `teams`.

- **match**: Stores data about each match, including player scores, balls faced, fours, sixes, bowled, maiden overs, runs given, wickets, catches, stumpings, and run-outs.
- **stats**: Stores player statistics including matches played, runs, centuries, half-centuries, value, and category.
- **teams**: Stores the names of teams and their players.

## Sample Rules for Scoring

### Batting
- 1 point for 2 runs scored
- Additional 5 points for half-century
- Additional 10 points for century
- 2 points for strike rate (runs/balls faced) of 80-100
- Additional 4 points for strike rate > 100
- 1 point for hitting a boundary (four) and 2 points for over boundary (six)

### Bowling
- 10 points for each wicket
- Additional 5 points for three wickets per innings
- Additional 10 points for 5 wickets or more in an innings
- 4 points for economy rate (runs given per over) between 3.5 and 4.5
- 7 points for economy rate between 2 and 3.5
- 10 points for economy rate less than 2

### Fielding
- 10 points each for catch/stumping/run out

## Getting Started

### Prerequisites

- Python 3.x
- PyQt5
- SQLite

## Running the Game

Run the main game script:

```bash
python python_scripts/main_game.py 
```
## Contribution
Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License
