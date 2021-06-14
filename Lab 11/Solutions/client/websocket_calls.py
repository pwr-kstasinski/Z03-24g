import asyncio
import json
import time

import websockets
from PyQt5 import sip
from PyQt5.QtCore import QObject, pyqtSignal, QRunnable, QThreadPool
from websockets import exceptions
from websockets.exceptions import ConnectionClosedError, InvalidMessage

DEFAULT_MESSAGE = "ping"


class ProcessRunnableStatus(QObject):
    captureDataSignal = pyqtSignal(dict)


class ProcessRunnable(QRunnable):
    def __init__(self, target):
        QRunnable.__init__(self)
        self.t = target
        self.status = ProcessRunnableStatus()

    def run(self):
        # noinspection PyUnresolvedReferences
        self.t(self.status.captureDataSignal.emit)

    def start(self):
        QThreadPool.globalInstance().start(self)


def do_async(callback, fun):
    p = ProcessRunnable(fun)
    connect_callback_and_start(callback, p)


def connect_callback_and_start(callback, p: QRunnable):
    p.status.captureDataSignal.connect(callback)
    p.start()


def async_connect_websocket(callback, websocket_address, loop, log, logged_user_func):
    def connect_ws(emit):
        async def handle_websocket():
            while logged_user_func() is not None:
                log.info(f"websocket connecting with {websocket_address}")
                try:
                    async with websockets.connect(websocket_address) as websocket:
                        log.info(f"websocket connected with {websocket_address}")
                        await websocket.send(logged_user_func().id)
                        async for message in websocket:
                            if logged_user_func() is None:
                                break
                            data = json.loads(message)
                            log.info(f"websocket data received from {websocket_address}: {data} ")
                            if data != DEFAULT_MESSAGE:
                                emit(data if isinstance(data, dict) else json.loads(data))
                except ConnectionClosedError:
                    log.info(f"websocket connection with {websocket_address} lost")
                except ConnectionRefusedError:
                    log.info(f"websocket connection with {websocket_address} refused")
                except InvalidMessage:
                    log.info(f"websocket connection with {websocket_address} gotten invalid message")
                finally:
                    await asyncio.sleep(3)

        loop.run_until_complete(handle_websocket())

    do_async(callback, connect_ws)
