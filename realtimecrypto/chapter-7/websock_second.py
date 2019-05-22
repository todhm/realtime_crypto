import websocket 
import json 


def on_message(ws,message):
    message = json.loads(message)
    if message['type'] == "update":
        for i in message['events']:
            if 'side' in i:
                payload = {"side":i['side'],'price':i['price'],
                'remaining':i['remaining']}
                print(payload)

ws = websocket.WebSocketApp("wss://api.gemini.com/v1/marketdata/BTCUSD",
on_message=on_message)



ws.run_forever()