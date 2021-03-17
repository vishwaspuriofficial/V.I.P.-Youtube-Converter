from re import search

from kivy.app import App
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.popup import Popup
import pytube
from kivy.core.window import Window
import os
from kivy.uix.image import Image

# import urllib.request

Window.size = (800, 600)

try:
    from pytube import YouTube
    from pytube import Playlist

except Exception as e:
    print("Sorry, Modules are missing {}".format(e))


class TestApp(App):
    def build(self):
        return kv


class WindowManager(ScreenManager):
    pass

class IntroWindow(Screen):
    pass


def self(args):
    pass


class SearchWindow(Screen):
    url1 = ObjectProperty(None)

    def mp4(self):
        try:
            ytd = YouTube(str(self.url1.text))
            title = ytd.title
            found = f"Found: {title}"
            print("Run the mp4 function")
            print("Downloading")          
            print(ytd.streams.get_highest_resolution().download())
            print("Downloaded")
        except:
            print("Error!: Invalid YouTube Url")

    def mp3(self):
        try:
            ytd = YouTube(str(self.url1.text))
            title = ytd.title
            found = f"Found: {title}"
            print("Run the mp3 function")
            file_path = (ytd.streams.get_highest_resolution().download())
            base = os.path.splitext(file_path)[0]
            os.rename(file_path, base + '.mp3')
            print("Downloaded")
        except:
            print("Error!: Invalid YouTube Url")

kv = Builder.load_file("test.kv")

TestApp().run()
