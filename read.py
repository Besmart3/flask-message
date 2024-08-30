# # # import paho.mqtt.client as mqtt

# # # def on_connect(client, userdata, flags, rc):
# # #     print("Connected with result code "+str(rc))

# # #     # Here you can subscribe to whatever topics you like
# # #     # use '#' for a 'wildcard' - subscribe to any messages
# # #     client.subscribe("glblcd/sam")

# # # def on_message(client, userdata, msg):
# # #     print(msg.topic + " \n " + msg.payload.decode("utf-8") + " \n ") 

 
# # # client = mqtt.Client()
# # # client.on_connect = on_connect
# # # client.on_message = on_message
# # # client.connect("127.0.0.1", 1883, 60)

    
# # # client.loop_forever()

# # import paho.mqtt.client as mqtt
# # import time
# # from gpiozero import LED
# # from time import sleep

# # led = LED(17)
# # Connected = False  # Global variable for the state of the connection

# # def control_led(state):
# #     if state == 'on':
# #         led.on()
# #     elif state == 'off':
# #         led.off()
# #     else:
# #         print("Invalid state")

# # def on_connect(client, userdata, flags, rc):
# #     if rc == 0:
# #         print("Connected to broker")
# #         global Connected
# #         Connected = True
# #     else:
# #         print("Connection failed")

# # def on_message(client, userdata, msg):
# #     message = msg.payload.decode()
# #     print(f"Message received: {message}")
# #     if message.lower() == "turn on light":
# #         control_led('on')
# #     elif message.lower() == "turn off light":
# #         control_led('off')
# #     else:
# #         print("Invalid command")

# # def publish_message(topic, message):
# #     client.publish(topic, message)

# # client = mqtt.Client()
# # client.on_connect = on_connect
# # client.on_message = on_message

# # client.connect("127.0.0.1", 1883, 60)
# # client.subscribe("glblcd/sam")  # Subscribe to the topic

# # client.loop_start()  # Start the loop

# # while not Connected:
# #     time.sleep(1)

# # try:
# #     while True:
# #         # Publish a message
# #         message = input("Enter message to send: ")
# #         publish_message("glblcd/sam", message)
# #         sleep(1)

# # except KeyboardInterrupt:
# #     print("Disconnecting from broker...")
# #     client.disconnect()
# #     client.loop_stop()

# import paho.mqtt.client as mqtt
# import time
# from gpiozero import LED
# from time import sleep

# led = LED(17)
# Connected = False  # Global variable for the state of the connection

# def control_led(state):
#     if state == 'on':
#         led.on()
#     elif state == 'off':
#         led.off()
#     else:
#         print("Invalid state")

# def on_connect(client, userdata, flags, rc):
#     if rc == 0:
#         print("Connected to broker")
#         global Connected
#         Connected = True
#     else:
#         print("Connection failed")

# def on_message(client, userdata, msg):
#     message = msg.payload.decode()
#     print(f"Message received: {message}")
#     if message.lower() == "turn on light":
#         control_led('on')
#     elif message.lower() == "turn off light":
#         control_led('off')
#     else:
#         print("Invalid command")

# # def publish_message(topic, message):
# #     client.publish(topic, message)

# client = mqtt.Client()
# client.on_connect = on_connect
# client.on_message = on_message

# client.connect("127.0.0.1", 1883, 60)
# client.subscribe("glblcd/sam")  # Subscribe to the topic

# client.loop_start()  # Start the loop

# while not Connected:
#     time.sleep(1)

# try:
#     while True:
#         # Publish a message
#         message = input("Enter message to send: ")
#         publish_message("glblcd/sam", message)
#         sleep(1)

# except KeyboardInterrupt:
#     print("Disconnecting from broker...")
#     client.disconnect()
#     client.loop_stop()


import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Here you can subscribe to whatever topics you like
    # use '#' for a 'wildcard' - subscribe to any messages
    client.subscribe("glblcd/sam")
    

def on_message(client, userdata, msg):
    print(msg.topic + " \n " + msg.payload.decode("utf-8") + " \n ")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("127.0.0.1", 1883, 60)

client.loop_forever()