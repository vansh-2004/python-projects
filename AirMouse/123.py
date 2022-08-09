

from pynput.keyboard import Key, Controller
import Gesture_Controller
from threading import Thread
gc = Gesture_Controller.GestureController()
t = Thread(target = gc.start)
t.start()