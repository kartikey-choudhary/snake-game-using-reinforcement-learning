A self-learning AI that plays the classic Snake game using Deep Q-Learning (DQN), built with PyTorch and Pygame.


## 🚀 Features

- Deep Q-Learning implementation from scratch (no external RL libraries)
- Training agent that learns via rewards and punishments
- Real-time or headless training modes (with or without game rendering)
- GPU and CPU compatible (CPU preferred for small models)
- Live plotting of scores and average performance over time

---

## 🧠 Tech Stack

- **Python**
- **PyTorch** – for the neural network and training
- **Pygame** – for game environment
- **Matplotlib** – for plotting training performance

---

## 📁 Project Structure

snake-ai/
├── agent.py # Core DQN agent
├── game.py # Snake game logic using Pygame
├── model.py # Neural network model and trainer
├── helper.py # Plotting utility
├── model/ # Saved model files
└── README.md # Project documentation

yaml
Copy
Edit

---

## 🧪 How It Works

1. The Snake game is run in a loop.
2. The agent observes the state (e.g. danger, direction, food).
3. Based on the state, the agent chooses an action using exploration/exploitation.
4. The game returns a reward and the next state.
5. The agent learns from this step using short- and long-term memory.
6. The model improves over time to avoid collisions and maximize score.

---

## 🎮 Controls (for Manual Mode)

- Not available. The agent plays the game itself. You just run and watch (or skip rendering for speed).

---

## 🖥️ Running the Project

### 🧰 Prerequisites
Make sure you have Python 3.7+ and pip installed.

### 🔌 Install dependencies
```bash
pip install -r requirements.txt

▶️ Start Training
bash
python agent.py




⚙️ Training Modes
With GUI (slower): Snake game window appears during training

Headless (faster): No graphics rendering, ideal for faster training
(You can toggle this via a train_mode=True flag in SnakeGameAI)

📈 Sample Training Graph
The agent's score and average score improve over time:
<img width="777" height="587" alt="Screenshot 2025-07-27 155756" src="https://github.com/user-attachments/assets/ce3d6982-c451-4ff0-b37a-66420a400e8d" />

