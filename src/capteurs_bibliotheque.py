import json
import time
import random
import paho.mqtt.client as mqtt
from utils import random_user, random_livre, timestamp

BROKER = "localhost"
TOPIC = "bibliotheque/emprunt"

client = mqtt.Client()
client.connect(BROKER, 1883, 60)

print("📚 Simulation Bibliothèque (simple) démarrée... Ctrl+C pour arrêter")

while True:
    livre_id, titre = random_livre()
    data = {
        "user_id": random_user(),
        "livre_id": livre_id,
        "titre": titre,
        "zone": "Z1",
        "action": random.choice(["emprunt", "retour"]),
        "timestamp": timestamp()
    }

    client.publish(TOPIC, json.dumps(data))
    print("📘 Message envoyé :", data)

    time.sleep(3)
