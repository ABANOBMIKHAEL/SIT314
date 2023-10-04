from faker import Faker
import random
import json
from datetime import date
from pymongo import MongoClient

fake = Faker()

def generate_light(floor):
    status = random.choice(['ON', 'OFF'])
    brightness = random.randint(0, 100) if status == 'ON' else 0
    colors = ['RED', 'GREEN', 'BLUE', 'WHITE', 'YELLOW', 'PURPLE', 'ORANGE']
    color = random.choice(colors) if status == 'ON' else 'OFF'
    return {
        "light_id": fake.uuid4(),
        "status": status,
        "brightness": brightness,
        "color": color,
        "floor": floor,
        "room": fake.random_element(elements=('Conference', 'Office', 'Lobby', 'Restroom', 'Cafeteria'))
    }

def generate_switch(floor):
    control_methods = ['Physical', 'Mobile App', 'Web Interface']
    return {
        "switch_id": fake.uuid4(),
        "floor": floor,
        "room": fake.random_element(elements=('Conference', 'Office', 'Lobby', 'Restroom', 'Cafeteria')),
        "control_method": random.choice(control_methods),
        "associated_lights": [fake.uuid4() for _ in range(random.randint(1, 10))]
    }

def generate_user():
    roles = ['Admin', 'Maintenance', 'General User']
    return {
        "user_id": fake.uuid4(),
        "name": fake.name(),
        "role": random.choice(roles),
        "last_login": fake.date_time_this_year(),
        "access_logs": [{"action": fake.random_element(elements=('Login', 'Logout', 'Light Control', 'Switch Control')), "last_login": fake.date_time_this_year(),} for _ in range(random.randint(1, 10))]
    }



floors = 50
lights_per_floor = 200
switches_per_floor = 50
total_users = 5000

lights = [generate_light(floor=i+1) for i in range(floors) for _ in range(lights_per_floor)]
switches = [generate_switch(floor=i+1) for i in range(floors) for _ in range(switches_per_floor)]
users = [generate_user() for _ in range(total_users)]


#with open("mock_lights.json", "w") as file:
 #   json.dump(lights, file, default=date_handler, indent=4)

#with open("mock_switches.json", "w") as file:
 #   json.dump(switches, file, default=date_handler, indent=4)

#with open("mock_users.json", "w") as file:
 #   json.dump(users, file, default=date_handler, indent=4)

YOUR_USERNAME = "abanobmikhael7"
YOUR_PASSWORD = "&Bob01095459013&"
connection_string = f"mongodb+srv://abanobmikhael7:&Bob01095459013&@finalproject.m1flajw.mongodb.net/retryWrites=true&w=majority"

client = MongoClient(connection_string)

db = client.projectdata

lights_collection = db.lights
lights_collection.insert_many(lights)

switches_collection = db.switches
switches_collection.insert_many(switches)

users_collection = db.users
users_collection.insert_many(users)
