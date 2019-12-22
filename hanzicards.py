import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from random import randint
from hanzilib import hdict

font_path = "simsun.ttc"
font_path2 = "pinyin.TTF"


        
class Card(RelativeLayout):
    
    def __init__(self, **kwargs):
        super(Card, self).__init__(**kwargs)
        self.cols = 1
        self.r = 0
        
        self.btn = Button(text=hdict[self.r][0], size_hint_y=0.9, pos_hint={'top':1}, background_normal='', color=(0,0,0,1), font_name=font_path, font_size=40)
        self.btn.bind(on_press=self.flip)
        self.add_widget(self.btn)

        self.btn2 = Button(text=hdict[self.r][1], size_hint_y=0.9, pos_hint={'top':1}, background_normal='', color=(0,0,0,1), font_name=font_path2, font_size=40)
        self.btn2.bind(on_press=self.flip2)

        self.nextbtn = Button(text="Next", size_hint_y=0.1, pos_hint={'bottom':0})
        self.nextbtn.bind(on_press=self.next)
        self.add_widget(self.nextbtn)
    def next(self, instance):
        self.remove_widget(self.btn)
        self.remove_widget(self.btn2)
        self.r = randint(0,9932) 
        self.btn = Button(text=hdict[self.r][0], size_hint_y=0.9, pos_hint={'top':1}, background_normal='', color=(0,0,0,1), font_name=font_path, font_size=40)
        self.btn.bind(on_press=self.flip)
        self.add_widget(self.btn)
        return self.r
    def flip(self, instance):
        self.remove_widget(self.btn2)
        self.btn2 = Button(text=hdict[self.r][1], size_hint_y=0.9, pos_hint={'top':1}, background_normal='', color=(0,0,0,1), font_name=font_path2, font_size=40)
        self.btn2.bind(on_press=self.flip2)
        self.add_widget(self.btn2)
    def flip2(self, instance):
        self.remove_widget(self.btn)
        self.btn = Button(text=hdict[self.r][0], size_hint_y=0.9, pos_hint={'top':1}, background_normal='', color=(0,0,0,1), font_name=font_path, font_size=40)
        self.btn.bind(on_press=self.flip)
        self.add_widget(self.btn)
        

        
class MyApp(App):
    def build(self):
        return Card()

MyApp().run()
