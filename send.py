import paho.mqtt.client as mqtt
import time
from gpiozero import LED
from time import sleep

led = LED(17)
Connected = False  # Global variable for the state of the connection

def control_led(state):
    if state == 'on':
        led.on()
    elif state == 'off':
        led.off()
    else:
        print("Invalid state")

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected
        Connected = True
    else:
        print("Connection failed")

def on_message(client, userdata, msg):
    message = msg.payload.decode()
    print(f"Message received: {message}")
    if message.lower() == "turn on light":
        control_led('on')
    elif message.lower() == "turn off light":
        control_led('off')
    else:
        print("Invalid command")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("127.0.0.1", 1883, 60)
client.subscribe("glblcd/sam")  # Subscribe to the topic

client.loop_start()  # Start the loop

while not Connected:
    time.sleep(1)

try:
    while True:
        pass  # Keep the program running

except KeyboardInterrupt:
    print("Disconnecting from broker...")
    client.disconnect()
    client.loop_stop()
