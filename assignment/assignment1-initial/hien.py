import serial.tools.list_ports
import paho.mqtt.client as mqttclient
import time
import json
import random

BROKER_ADDRESS = "demo.thingsboard.io"
PORT = 1883
THINGS_BOARD_ACCESS_TOKEN = ["R1nATjBETrYupXewz5C4"]

# topic = "v1/devices/me/rpc/response/+"
autoMode = 0


def subscribed(client, userdata, mid, granted_qos):
    print("Subscribed...")


def recv_message(client, userdata, message):
    print("Data Received: ", json.loads(message.payload)["shared"])
    cmd = 0
    global autoMode
    try:
        jsonobj = json.loads(message.payload)["shared"]
        if jsonobj["method"] == "Warning" and jsonobj["params"] == "On":
            if isMicrobitConnected:
                ser.write((str("0")).encode())
        if jsonobj["method"] == "Warning" and jsonobj["params"] == "Off":
            if isMicrobitConnected:
                ser.write((str("1")).encode())
        if jsonobj["method"] == "SetFan" and jsonobj["params"] == "On":
            if isMicrobitConnected:
                ser.write((str("2")).encode())
        if jsonobj["method"] == "SetFan" and jsonobj["params"] == "Off":
            if isMicrobitConnected:
                ser.write((str("3")).encode())

    except:
        pass


def connected(client, usedata, flags, rc):
    if rc == 0:
        print("Thingsboard connected successfully!!")
        # client.subscribe("v1/devices/me/rpc/request/+")
        client.subscribe("v1/devices/me/rpc/response/1")
        # client.subscribe()
    else:
        print("Connection is failed")


clients = []
for access_token in THINGS_BOARD_ACCESS_TOKEN:
    client = mqttclient.Client("Gateway_Thingsboard")
    client.username_pw_set(access_token)
    clients.append(client)

for client in clients:
    client.on_connect = connected
    client.connect(BROKER_ADDRESS, 1883)
    client.loop_start()
    client.on_subscribe = subscribed
    client.on_message = recv_message


def getPort():
    ports = serial.tools.list_ports.comports()
    print(ports)
    N = len(ports)
    commPort = "None"
    for i in range(0, N):
        port = ports[i]
        strPort = str(port)
        print(strPort)
        if "USB-SERIAL CH340" in strPort:
            splitPort = strPort.split(" ")
            commPort = splitPort[0]
            print(commPort)
    return commPort


isMicrobitConnected = False
if getPort() != "None":
    ser = serial.Serial(port=getPort(), baudrate=115200)
    isMicrobitConnected = True

# mess = ""
entry_dict1 = {
    "temperature": "20",
    "humidity": "25",
}

entry_dict = {
    "temperature": "25",
    "humidity": "25",
}
methodSensor = {"method": "null", "params": "null"}


def processData(data):
    data = data.replace("!", "")
    data = data.replace("#", "")
    splitData = data.split(":")
    print(splitData)
    entry_dict["temperature"] = splitData[0]
    entry_dict["humidity"] = splitData[1]
    print(type(entry_dict["humidity"]))
    print(json.dumps(entry_dict))
    # Automatic in gateway
    clients[0].publish("v1/devices/me/telemetry", json.dumps(entry_dict))
    print("Auto mode is activated")
    if float(entry_dict["humidity"]) < 60:
        methodSensor["method"] = "Warning"
        methodSensor["params"] = "Off"
        for client in clients:
            client.publish("v1/devices/me/attributes", json.dumps(methodSensor))
    if float(entry_dict["humidity"]) > 70:
        methodSensor["method"] = "Warning"
        methodSensor["params"] = "On"
        for client in clients:
            client.publish("v1/devices/me/attributes", json.dumps(methodSensor))
    if float(entry_dict["temperature"]) > 30:
        methodSensor["method"] = "SetFan"
        methodSensor["params"] = "On"
        for client in clients:
            client.publish("v1/devices/me/attributes", json.dumps(methodSensor))
    if float(entry_dict["temperature"]) < 25:
        methodSensor["method"] = "SetFan"
        methodSensor["params"] = "Off"
        for client in clients:
            client.publish("v1/devices/me/attributes", json.dumps(methodSensor))


mess = ""


def readSerial():
    # print("hello")
    bytesToRead = ser.inWaiting()
    if bytesToRead > 0:
        global mess
        mess = mess + ser.read(bytesToRead).decode("UTF-8")
        while ("#" in mess) and ("!" in mess):
            start = mess.find("!")
            end = mess.find("#")
            processData(mess[start : end + 1])
            if end == len(mess):
                mess = ""
            else:
                mess = mess[end + 1 :]


while True:
    print(autoMode)
    if isMicrobitConnected:
        print("Yolobit access is accepted!")
        readSerial()
    for client in clients:
        client.publish("v1/devices/me/attributes", json.dumps(methodSensor))
        client.publish("v1/devices/me/attributes/request/1", '{"sharedKeys":"method,params"}')
        time.sleep(1)
    time.sleep(1)
