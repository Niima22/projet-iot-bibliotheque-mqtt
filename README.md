 
# 📚 Système IoT de Gestion Intelligente des Emprunts de Livres

**Python • MQTT • Node-RED**

## 📖 Description

Ce projet implémente un **système IoT complet basé sur MQTT** permettant de **simuler, surveiller et visualiser en temps réel les emprunts et retours de livres dans une bibliothèque**.

Le système permet de suivre l’activité de la bibliothèque (emprunts, retours, zones), d’historiser les données et de les visualiser via un **dashboard web interactif** développé avec **Node-RED**.

---

## 🎯 Objectifs du Projet

* Simuler des capteurs IoT liés à une bibliothèque
* Suivre les **emprunts et retours de livres** en temps réel
* Utiliser le protocole **MQTT** pour la communication
* Visualiser les données sur un **dashboard web**
* Gérer plusieurs zones de bibliothèque
* Historiser les données dans des fichiers CSV
* Produire des statistiques automatiques

---

## 🧠 Architecture du Système

```
Capteurs Python → MQTT (Mosquitto) → Node-RED → Dashboard Web
```

### 🧩 Couches de l’architecture

1. **Couche Capteurs (Python)**

   * Simulation des emprunts / retours
   * Génération d’événements utilisateurs
   * Gestion multi-zones

2. **Couche Communication**

   * Protocole MQTT
   * Broker Mosquitto (port 1883)

3. **Couche Traitement**

   * Node-RED
   * Logique métier (comptage, filtrage, statistiques)

4. **Couche Visualisation**

   * Dashboard Node-RED
   * Indicateurs, compteurs et historique

---

## ⚙️ Technologies Utilisées

| Technologie | Version | Utilisation               |
| ----------- | ------- | ------------------------- |
| Python      | 3.14+   | Simulation des capteurs   |
| Mosquitto   | 2.0+    | Broker MQTT               |
| Node-RED    | v4.x    | Traitement & Dashboard    |
| paho-mqtt   | 2.0+    | Client MQTT Python        |
| CSV         | —       | Historisation des données |

---

## ✨ Fonctionnalités

### 📘 Système Mono-Zone

* Simulation d’emprunts et de retours
* Données temps réel via MQTT
* Historisation CSV
* Compteur total des emprunts
* Affichage instantané sur Node-RED

### 🗺️ Système Multi-Zones

* Gestion de plusieurs zones de bibliothèque
* Identification de la zone d’emprunt
* Vue globale de l’activité
* Simulation simultanée (threading Python)

### 📊 Dashboard Web

* Bouton d’emprunt simulé
* Compteur total des emprunts
* Liste des derniers événements
* Historique en temps réel
* Architecture extensible (statistiques, alertes)

---

## 📁 Structure du Projet

```
projet-iot-bibliotheque-mqtt/
├── src/
│   ├── capteurs_bibliotheque.py
│   ├── capteurs_bibliotheque_avance.py
│   ├── capteurs_multi_zones.py
│   └── utils.py
├── nodered/
│   └── flows_bibliotheque.json
├── data/
│   └── historique_emprunts.csv
├── README.md
```

---

## 🚀 Installation et Exécution

### ✅ Prérequis

* Python 3.14+
* Node.js
* Node-RED
* Mosquitto MQTT Broker

---

### ▶️ Démarrage du système

#### 1️⃣ Vérifier Mosquitto

```bash
Get-Service mosquitto   # Windows
```

#### 2️⃣ Lancer Node-RED

```bash
node-red
```

➡️ Accéder au dashboard :

```
http://localhost:1880/ui
```

#### 3️⃣ Lancer la simulation (mono-zone)

```bash
cd src
python capteurs_bibliotheque_avance.py
```

#### 4️⃣ Lancer la simulation multi-zones

```bash
python capteurs_multi_zones.py
```

---

## 📈 Données Simulées

Exemple de message MQTT :

```json
{
  "user_id": "U109",
  "livre_id": "L005",
  "titre": "IoT Basics",
  "zone": "Z1",
  "timestamp": "2026-01-11T18:59:07"
}
```

---

## 🎓 Contexte Académique

**Projet réalisé dans le cadre de :**

* Module : Internet des Objets (IoT)
* Master : Ingénierie de Développement Logiciel et Décisionnel
* Université Mohammed V – Faculté des Sciences de Rabat
* Année : 2025 / 2026

---

## 👩‍💻

**Niima Bettaoui**
Master IDLD – UM5 Rabat

---

## 🔮 Perspectives d’Amélioration

* Authentification des utilisateurs
* Alertes automatiques (livre indisponible)
* Statistiques avancées
* Base de données (MongoDB / Firebase)
* Interface web dédiée (React / Angular)
* Déploiement cloud
