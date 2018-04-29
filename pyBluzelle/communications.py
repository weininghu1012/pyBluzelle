import websocket


class Communication:
    def __init__(self):
        self.connections = set()
        self.resolvers = {}
        self.messages = []
        self.request_id_counter = 0
        self.uuid = None
        self.address = None

    def connect(self,address, uuid):
        self.uuid = uuid
        self.address = address

    def on_message(self, event, socket):
        request_id = event['request-id']

        request = self.messages[request_id]
        resolver = self.resolvers[request_id]

        self.resolvers.pop(request_id, None)
        self.messages.pop(request_id, None)

        if request_id is None:
            raise Exception('Received non-response message.')
        if event.error == 'NOT_THE_LEADER':
            is_secure = self.address.startWith('wss://')
            prefix = 'wss://' if is_secure else 'ws://'
            address_and_port = prefix + event.data['leader-host'] + ':' + event.data['leader-port']
            self.connect(address_and_port, self.uuid)
            self.send(request_id, resolver)
        else:
            resolver(event)

    def amend_bzn_api(self, obj):
        obj.update({'bzn-api': 'crud'})
        return obj

    def amend_uuid(self, obj):
        obj.update({'db-uuid': self.uuid})

    def amend_request_id(self, obj):
        obj.update({
            'request-id': self.request_id_counter
        })
        self.request_id_counter += 1
        return obj

    def send(self, obj, resolver, rejecter):
        message = self.amend_uuid(self.amend_request_id(obj))
        request_id = message['request-id']
        self.resolvers[request_id] = resolver
        self.messages[request_id] = message

        


