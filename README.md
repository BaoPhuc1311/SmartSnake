# 🐍 SmartSnake

## 📖 Introduction
SmartSnake is an AI-powered Snake game that leverages machine learning to enhance gameplay. The game integrates two core algorithms:
- **Q-learning** 🧠: A reinforcement learning technique to train the AI agent for decision-making.
- **A\*** 🌟: A heuristic search algorithm to optimize the snake's path to the food.

The project aims to create an intelligent Snake game where the AI learns to navigate, grow, and achieve higher scores autonomously.

## 🎯 Objective
- Develop a Snake game where the AI uses **Q-learning** to make decisions based on state-action values.
- Implement the **A\*** algorithm to find the shortest path to the food.
- Enable the AI to improve its performance through iterative training.
- Provide a dual-mode game for both AI-controlled and human-playable snakes.

## 📋 Requirements
- 🐍 Python 3.8+
- 🎮 Pygame (`pygame`) for game rendering
- 🔢 NumPy (`numpy`) for matrix operations

## ⚙️ Installation
1. Clone the repository and navigate to the project directory:
   ```bash
   git clone https://github.com/BaoPhuc1311/SmartSnake.git
   cd SmartSnake
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage
To play the game with the AI controlling the snake:
```bash
python src/main.py
```

To play the game manually (human mode):
```bash
python src/human_mode.py
```

**Note**: Ensure you have a compatible Python environment and dependencies installed before running the game.

## 🧠 Training the AI
To train the AI using Q-learning:
```bash
python src/train_qlearning.py
```

The training process saves the Q-table to `src/qtable.npy` for reuse. You can adjust hyperparameters in `src/train_qlearning.py` to fine-tune the AI's performance.

## 🤝 Contributing
Contributions are welcome! To contribute:
1. Fork the repository 🍴.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a clear description of your changes.

Please report issues or suggest improvements via the [Issues](https://github.com/BaoPhuc1311/SmartSnake/issues) tab.

## 📜 License
This project is licensed under the [MIT License](LICENSE).
