# ⚙️ TicTacToe Backend (Django + Channels)

## 📌 Description

This is the backend service for the TicTacToe Realtime Game.
It handles game logic, player connections, and real-time communication for online multiplayer using WebSockets.

## 🚀 Features

* 🌐 Real-time multiplayer with WebSockets
* 🔌 Player connection & matchmaking system
* 🎮 Game state synchronization between players
* ⚡ Fast asynchronous handling using Django Channels

## 🛠️ Tech Stack

* **Framework:** Django
* **Realtime Engine:** Django Channels
* **Protocol:** WebSockets
* **ASGI Server:** (e.g., Daphne / Uvicorn)
* **Other Tools:** (e.g., Redis if you used it)

## 📂 Project Structure

```
backend/
│── game/               # Game logic and consumers
│── tictactoe/          # Main Django project settings
│── manage.py
│── requirements.txt
```

## 📦 Installation

### 1. Clone the repository

```bash id="a1x9bz"
git clone https://github.com/mike0001-prog/backend-tic-tac-toe
cd backend-tic-tac-toe
```

### 2. Create virtual environment

```bash id="4lq2sp"
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash id="y7rk2n"
pip install -r requirements.txt
```

### 4. Set up cache for django (to handle game state between devices)
```CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": BASE_DIR / "django_cache",
    }
}
```

```

## ▶️ Running the Server

### Development server

```bash id="1r1rq5"
python manage.py runserver
```

### ASGI (for Channels)

```bash id="yuzn3m"
daphne tictactoe.asgi:application
```

## 🔌 WebSocket Endpoints

Example:

```
ws://localhost:8000/ws/game/
```

> Handles:

* Player connections
* Game moves
* Real-time updates

## 🧠 How It Works

* Django handles standard backend logic and routing
* Django Channels enables asynchronous communication
* WebSocket consumers manage real-time gameplay
* Each game session syncs moves between connected players instantly
* Django cachhing is used to store the game data between opponents



## 🔐 Environment Variables

*Create a `.env` file if needed*

Example:

```
DEBUG=True
SECRET_KEY=your-secret-key
```

## 🤝 Contributing

Contributions are welcome! Feel free to fork and submit pull requests.

## 📄 License

This project is licensed under the MIT License.

## 👤 Author

* Your Name – https://github.com/mike0001-prog
