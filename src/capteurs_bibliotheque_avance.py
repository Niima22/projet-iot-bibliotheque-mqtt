import json
import time
import random
import paho.mqtt.client as mqtt
from utils import random_user, random_livre, random_zone, timestamp

BROKER = "localhost"
TOPIC = "bibliotheque/emprunt"

client = mqtt.Client()
client.connect(BROKER, 1883, 60)

print("✅ Simulation Bibliothèque (avancée) démarrée... Ctrl+C pour arrêter")

while True:
    livre_id, titre = random_livre()
    action = random.choices(
        ["emprunt", "retour"],
        weights=[0.7, 0.3]
    )[0]

    data = {
        "user_id": random_user(),
        "livre_id": livre_id,
        "titre": titre,
        "zone": random_zone(),
        "action": action,
        "timestamp": timestamp()
    }

    client.publish(TOPIC, json.dumps(data))

    emoji = "📘" if action == "emprunt" else "📗"
    print(f"{emoji} {action.capitalize()} :", data)

    time.sleep(3)
