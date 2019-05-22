from kafka import KafkaProducer, KafkaConsumer
import websocket
import json
import datetime



class gemini_websocket(object):
    """
    An object for interacting with the Gemini Websocket. Full Gemini API documentation is
    available at https://docs.gemini.com
    """
    
    def __init__(self, kafka_bootstrap_servers):
        """
        Initializes gemini object.
        
        Args:
            gemini_api_key: your API key for the exchange
            gemini_api_secret: secret associated with your API key
        """
        self.kafka_bootstrap_servers = kafka_bootstrap_servers
        self.producer = self.create_producer(self.kafka_bootstrap_servers)
    
    def create_producer(self, bootstrap_servers): 
        return KafkaProducer(bootstrap_servers=bootstrap_servers)
    
    def on_message(self, ws, message):
        message = json.loads(message)
        if message['type'] == 'update':
            for i in message['events']:
                print(i)
                if 'side' in i:
                    payload = {'side': i['side'], 'price': i['price'], 'remaining': i['remaining']}
                    sent = self.producer.send('gemini-feed', bytes(json.dumps(payload), 'utf-8'))

    def on_error(self, ws, error):
        print('Error {0}, {1}'.format(error, datetime.datetime.now()))

    def on_close(self, ws):
        print('Closed, {}'.format(datetime.datetime.now()))

    def on_open(self, ws):
        print('Opened, {}'.format(datetime.datetime.now()))

    def run_websocket(self):
        ws = websocket.WebSocketApp("wss://api.gemini.com/v1/marketdata/BTCUSD",
                                    on_message=self.on_message,
                                    on_open=self.on_open,
                                    on_close=self.on_close,
                                    on_error=self.on_error
                                    )

        ws.run_forever(ping_interval=5)  

gem = gemini_websocket(['kafka-node:9092'])
gem.run_websocket()