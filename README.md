# Pokedex Project Documentation

## Overview
This project is a Pokedex encyclopedia application that allows users to explore Pokemon data, compare Pokemon statistics, visualize information through graphs, and simulate battles between Pokemon.

The application provides both informational and interactive features, combining data visualization, comparison tools, and a simple battle simulation system in a graphical user interface (GUI).

## What Is This?
This Pokedex acts as an encyclopedia for Pokemon where users can:
* View Pokemon appearances, types, and statistics
* Compare two Pokemon side-by-side
* Visualize data using multiple graph types
* Simulate Pokemon battles
* Generate collectible-style Pokemon cards

## Features

### Pokemon Selection and Comparison
On the left-hand side, there are two scroll boxes that allow the user to select two Pokemon (either different or the same). The center of the GUI displays:
* Pokemon images
* Stats
* Type information

### Data Visualizations
Several visualization tools are available through buttons located in the interface:

* **Radar Graph**: Displays a radar chart comparing the stats of the two selected Pokemon.
* **Totals Graph**: Shows a side-by-side comparison of the total stats (sum of all stats) for each Pokemon.
* **Top 10s**: Displays a 2x2 grid of graphs showing the top 10 Pokemon by Attack, Defense, Speed, and Total Stats.
* **Types Chart**: A pie chart showing the percentage distribution of Pokemon types in the dataset.
* **Compare Button**: Generates a bar chart comparing individual stats between the two selected Pokemon.

### Music Viewer
Located at the bottom of the GUI, this displays a synthwave-style visualization of the background music. The background music is an instrumental Pokemon theme.

### Pokemon Card Generator
Below each Pokemon image, users can click "Make Card 1" or "Make Card 2." These buttons generate a Pokemon card containing:
* Pokemon image
* Stats
* Type information

Generated cards are saved in the "produced cards" folder for later viewing.

## Auto-Battler (In Depth)
The Auto-Battler allows users to simulate a battle between the two selected Pokemon.

### How It Works
The user can choose which Pokemon starts the battle. Both Pokemon's stats and types are displayed before the battle begins.

### Battle Mechanics
* Only Attack and Health Points (HP) are used.
* No other stats or type advantages are taken into account.
* Each battle starts with full health for both Pokemon to ensure fairness.

### Battle Log
Located below the Pokemon in the Auto-Battler window, the log displays:
* Which Pokemon attacked
* Damage dealt
* Health points lost
* Death alerts and the final winner

### Health Bar System
Each Pokemon has a visual health bar:
* Green indicates remaining health.
* Red indicates damage taken.
* The bar updates in real time as damage is dealt.
* When a Pokemon dies, the health bar becomes fully red.

## Summary
This Pokedex project combines data visualization, interactive comparison tools, media integration, and a simplified battle simulation. It serves as both a learning tool and an interactive Pokemon encyclopedia, offering a rich and engaging user experience.

## Installation

Open your terminal or command prompt and run:
```bash
git clone [https://github.com/Huz4y1/Pokedex.git](https://github.com/Huz4y1/Pokedex.git)

cd Pokedex

pip install -r requirements.txt

python main.py
