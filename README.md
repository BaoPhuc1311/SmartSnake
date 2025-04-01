# SmartSnake

## Introduction:
SmartSnake is an AI-powered Snake game that utilizes machine learning algorithms to improve gameplay. The game implements two core algorithms:
- **Q-learning**: Reinforcement learning to train the AI agent to play the game.
- **A\***: A heuristic search algorithm used to optimize the pathfinding of the snake.

The goal of this project is to build a Snake game where the AI can autonomously play and learn how to grow the snake to achieve higher scores.

## Objective:
- Create a Snake game where the AI uses **Q-learning** to make decisions based on state-action values.
- Implement **A\*** search algorithm to find the shortest path to the food.
- Allow the AI to learn and improve through training.
- Provide a playable version of the game for both humans and AI-controlled snakes.

## Requirements:
- Python 3.x
- Pygame (for game rendering)
- NumPy (for matrix manipulation)

## Installation
Clone this repository and navigate to the project directory:

```
git clone https://github.com/BaoPhuc1311/SmartSnake.git
cd SmartSnake
```

Install the necessary dependencies:

```
pip install -r requirements.txt
```

## Usage
To start the game and let the AI play:

```
python src/main.py
```

To manually control the snake, run the game in human mode:

```
python src/human_mode.py
```

## Training the AI
To train the AI using Q-learning, run:

```
python src/train_qlearning.py
```

## Contributing
Feel free to fork the repository, submit issues, or send pull requests. Contributions are welcome!

## License
This project is licensed under the MIT License
