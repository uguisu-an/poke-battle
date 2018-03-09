class EventEmitter:
    def __init__(self):
        self.event = {}

    def on(self, topic, action):
        self.event.setdefault(topic, []).append(action)

    def emit(self, topic, *args, **keywords):
        for action in self.event.setdefault(topic, []):
            action(*args, **keywords)
