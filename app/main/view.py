from flask import Blueprint, render_template
from app import mqtt, socketio
import json
main = Blueprint('main', __name__)


mqtt.subscribe("testing/#")
mqtt.subscribe("tanks/#")


@main.route('/')
def index():
    return render_template('main/index.html')


powerups = {
    0: ["all", "All powerups", ""],
    1: ["off", "none", "0x000000"],
    2: ["red", "Fire Rate", "0x000000"],
    3: ["orange", "Damage Increase", ""],
    4: ["yellow", "Damage Resistance", ""],
    5: ["green", "Repair", "0x00FF00"],
    6: ["blue", "Movement Speed", "0x0000FF"],
    7: ["cyan", "Shield", ""],
    8: ["magenta", "Turret Rotation", ""],
    9: ["white", "Remove Debuff | Neutral Flag", "0xFFFFFF"],
    10: ["rainbow", "Random", "(alternating)"],
    11: ["red/yellow", "Team Flag (Warm)", "(alternating)"],
    12: ["green/blue", "Team Flag (Cool)", "(alternating)"],

}

""" layouts mqtt layout
tanks/
└─ tank1/
   ├─ send/
   │  ├─ health
   │  └─ powerup
   └─ receive/
      ├─ hitBy
      └─ powerupUsed

"""


@main.route('/settings')
def settings():
    return render_template('settings/settings.html', powerups=powerups)


@mqtt.on_topic('tanks/<tank_num>/send')
def send(tank_num):
    pass


@mqtt.on_topic('tanks/<tank_num>/recieve')
def recieve(tank_num):
    pass


@mqtt.on_topic("testing/#")
def testing(client, userdata, message):
    payload = {
        "topic": message.topic,
        "message":  message.payload.decode()
    }
    socketio.emit("testing", payload)


@mqtt.on_topic("tanks/tank1/recieve/hitBy")
def tank1_hit(client, userdata, message):
    msg = message.payload.decode()
    results = json.loads(msg)
    print(results["id"], results["amount"], flush=True)
    socketio.emit("tanks/tank1/recieve/hitBy", results)


#
# @socketio.on('publish')
# def handle_publish(json_str):
#     data = json.loads(json_str)
#     mqtt.publish(data['topic'], data['message'])
#
#
# @socketio.on('subscribe')
# def handle_subscribe(json_str):
#     data = json.loads(json_str)
#     mqtt.subscribe(data['topic'])
#
#
# @socketio.on('unsubscribe_all')
# def handle_unsubscribe_all():
#     mqtt.unsubscribe_all()


@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    data = dict(
        topic=message.topic,
        payload=message.payload.decode()
    )
    socketio.emit('mqtt_message', data=data)


@mqtt.on_log()
def handle_logging(client, userdata, level, buf):
    print(level, buf)
