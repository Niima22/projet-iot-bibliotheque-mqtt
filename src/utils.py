import random
from datetime import datetime

USERS = [f"U{100+i}" for i in range(20)]
LIVRES = [
    ("L001", "Clean Code"),
    ("L002", "Design Patterns"),
    ("L003", "Spring Boot"),
    ("L004", "Python Crash Course"),
    ("L005", "IoT Basics")
]

ZONES = ["Z1", "Z2", "Z3"]

def random_user():
    return random.choice(USERS)

def random_livre():
    return random.choice(LIVRES)

def random_zone():
    return random.choice(ZONES)

def timestamp():
    return datetime.now().isoformat(timespec="seconds")
