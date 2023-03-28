import os
import tornado.ioloop
from tornado.web import Application
from app.config import Config
from app.handlers import MainHandler
from app.logging_config import setup_logging
from threading import Lock
import asyncio

config = Config(os.path.join(os.path.dirname(__file__), "openai_gpt_key.yaml"))
key_lock = asyncio.Lock()
key_state = {'index': 0}

def make_app():
    return Application([
        (r"/", MainHandler, dict(config=config, key_lock=key_lock, key_state=key_state)),
    ])

if __name__ == "__main__":
    setup_logging()  # Sets up logging configuration
    app = make_app()
    app.listen(8080, address="0.0.0.0")
    tornado.ioloop.IOLoop.current().start()
