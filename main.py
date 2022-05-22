import pandas as pd
import random
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton
from kivymd.uix.screen import Screen
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from builder import screen_helper
from kivymd.uix.picker import MDTimePicker
from kivy.clock import Clock
from datetime import datetime
import threading
import pygame
from kivymd.uix.dialog import MDDialog

path = "C:/Users/hamma/OneDrive/Bureau/sample.xlsx"
pygame.init()

Window.size = (300, 500)
sm = ScreenManager()


class WelcomeScreen(Screen):
    def on_start(self):
        Clock.schedule_once(self.change_screen, 5)  # Delay for 5 seconds

    def change_screen(self, dt):
        self.manager.current = "main"


class MainScreen(Screen):
    pass


class AlarmScreen(Screen):
    sound = pygame.mixer.Sound("alarm.mp3")
    volume = 0
    dialog = None

    def show_alert_dialog(self):
        s2 = self.manager.get_screen('second_quote')
        val = s2.get_quote()
        if not self.dialog:
            self.dialog = MDDialog(
                title="HEY !! WAKE UP and have a NICE day !!",
                text=val,
                buttons=[
                    MDFlatButton(text="Stop Alarm", on_release=self.stop),
                    MDRectangleFlatButton(text="Close Window", on_release=self.close_dialog)
                ]
            )

        self.dialog.open()

    def time_picker(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.get_time, on_save=self.schedule)
        time_dialog.open()

    def schedule(self, *args):
        Clock.schedule_once(self.alarm, 1)

    def alarm(self, *args):
        now = datetime.now()
        hours, minutes, seconds = map(int, self.ids.alarm_time.text.split(':'))
        later = datetime(datetime.today().year, datetime.today().month, datetime.today().day, hours, minutes, seconds)
        difference = later - now
        total_sec = difference.total_seconds()
        timer = threading.Timer(total_sec, self.start)
        timer.start()

    def set_volume(self, *args):
        self.volume += 0.05
        if self.volume < 1.0:
            Clock.schedule_interval(self.set_volume, 10)
            self.sound.set_volume(self.volume)
        else:
            self.sound.set_volume(1)

    def start(self, *args):
        self.sound.play(-1)
        self.set_volume()
        self.show_alert_dialog()

    def get_time(self, instance, time):
        self.ids.alarm_time.text = str(time)

    def stop(self, obj):
        self.sound.stop()
        Clock.unschedule(self.set_volume)
        self.volume = 0

    def close_dialog(self, obj):
        self.dialog.dismiss()


class QuoteScreen(Screen):
    pass


class SecondQuoteScreen(Screen):

    def spinner_clicked(self):
        value = self.ids.spinner_id.text
        print(value)

    def get_quote(self):
        val = self.ids.spinner_id.text
        df = pd.read_excel(path)
        l = len(df)
        x = []
        df['Category'] = df['Category'].str.strip()
        for i in range(0, l):
            if df.iloc[i, 2] == val:
                x.append(" ' " + df.iloc[i, 0] + " ' " + " BY " + df.iloc[i, 1])
        value = random.choice(tuple(x))
        return value




sm.add_widget(WelcomeScreen(name='welcome'))
sm.add_widget(MainScreen(name='main'))
sm.add_widget(SecondQuoteScreen(name='second_quote'))


class Motivation(MDApp):

    def close_application(self):
        App.get_running_app().stop()
        Window.close()

    def build(self):
        self.theme_cls.primary_palette = 'Teal'
        screen = Builder.load_string(screen_helper)
        return screen


if __name__ == '__main__':
    Motivation().run()
