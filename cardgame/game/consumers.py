import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer
from django.core import serializers
import datetime


def handle_message(text_data_json):
    message = text_data_json['message']
    username = text_data_json['username']
    time = datetime.datetime.now()

    return {
        'type': 'chat_message',
        'message': message,
        "username": username,
        "time": time.strftime("%m/%d/%Y, %H:%M:%S"),
    }


def handle_card(text_data_json):
    card_id = text_data_json['card_id']
    card_hp = text_data_json['card_hp']
    card_attack = text_data_json['card_atk']
    card_name = text_data_json['card_name']
    username = text_data_json['username']

    return {
        'type': 'card',
        'card_id': card_id,
        'card_hp': card_hp,
        'card_atk': card_attack,
        'card_name': card_name,
        'username': username,
    }


class ChatConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.room_group_name = None
        self.room_name = None

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name, self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):

        data = {}
        text_data_json = json.loads(text_data)
        if text_data_json['type'] == 'message':
            data = handle_message(text_data_json)
        elif text_data_json['type'] == 'card':
            data = handle_card(text_data_json)

        # Send message to room group
        await self.channel_layer.group_send(self.room_group_name, data)

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        time = event['time']

        # Send message to WebSocket
        await self.send(
            text_data=json.dumps(
                {
                    'type': 'message',
                    'message': message,
                    "username": username,
                    "time": time,
                },
                default=str,
            )
        )

    async def card(self, event):
        card_id = event['card_id']
        card_hp = event['card_hp']
        card_attack = event['card_atk']
        card_name = event['card_name']
        username = event['username']

        await self.send(
            text_data=json.dumps(
                {
                    'type': 'card',
                    'card_id': card_id,
                    'card_hp': card_hp,
                    'card_atk': card_attack,
                    'card_name': card_name,
                    'username': username,
                },
                default=str,
            )
        )
