# 🐦 Flappy Bird AI Agent (Deep Q-Network)

> 🚀 An AI agent that learns to play Flappy Bird using Deep Reinforcement Learning (DQN)

---

## 📌 Overview

This project demonstrates how an AI agent can learn to play the classic **Flappy Bird** game using a **Deep Q-Network (DQN)**.
The agent improves its performance over time by interacting with the environment and maximizing cumulative rewards.

---

## 🎯 Objectives

* Learn optimal flap timing
* Maximize survival time
* Pass as many pipes as possible

---

## 🧠 Key Concepts

* Reinforcement Learning (RL)
* Deep Q-Network (DQN)
* Markov Decision Process (MDP)
* Experience Replay
* Target Network
* ε-greedy Policy

---


---

## ⚙️ Tech Stack

* **Language:** Python
* **Frameworks:** PyTorch / TensorFlow


---

## ⚡ How It Works

1. The agent observes the current state (bird position, velocity, pipe distance)
2. Selects an action using ε-greedy policy
3. Receives reward:

   * +1 → Pass pipe
   * -1 → Collision
4. Stores experience in replay memory
5. Trains neural network using mini-batches
6. Updates target network periodically

---

## 🧪 DQN Architecture

* Input: Game state (features or pixels)
* Hidden Layers: Fully Connected / CNN
* Output: Q-values for each action


## 📊 Results

* 📈 Increasing reward over episodes
* 🎮 Agent learns stable flight
* 🧠 Improved decision-making over time



## 🔥 Future Improvements

* Double DQN
* Dueling DQN
* Prioritized Experience Replay


## 👨‍💻 Author

**Sonu Kumar**


## 🌟 Why This Project Matters

This project showcases:

* Strong understanding of Reinforcement Learning
* Practical implementation of Deep Q-Network
* Ability to build end-to-end AI systems

---

⭐ If you like this project, consider giving it a star!
