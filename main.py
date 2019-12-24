import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from random import randint
from hanzilib import hdict
import os

tools_path = os.path.dirname(__file__)


font_path = os.path.join(tools_path, "simsun.ttc")
font_path2 = os.path.join(tools_path,"lsansuni.ttf")


        
class Card(RelativeLayout):
    
    def __init__(self, **kwargs):
        super(Card, self).__init__(**kwargs)
        self.cols = 1
        self.r = 0
        self.df = 9932
        
        self.btn = Button(text=hdict[self.r][0], size_hint_y=0.9, pos_hint={'top':1}, background_normal='', color=(0,0,0,1), font_name=font_path, font_size=40)
        self.btn.bind(on_press=self.flip)
        self.add_widget(self.btn)

        self.btn2 = Button(text=hdict[self.r][1], size_hint_y=0.9, pos_hint={'top':1}, background_normal='', color=(0,0,0,1), font_name=font_path2, font_size=40)
        self.btn2.bind(on_press=self.flip2)

        self.nextbtn = Button(text="Next", size_hint_y=0.1, size_hint_x=0.8, pos_hint={'bottom':0})
        self.nextbtn.bind(on_press=self.next)
        self.add_widget(self.nextbtn)
        
        self.hardbtn = Button(text="Hard", size_hint_y=0.1, size_hint_x=0.2, pos_hint={'bottom':0, 'right':1}, background_color=(1,0,0,1))
        self.hardbtn.bind(on_press=self.easy)
        self.add_widget(self.hardbtn)

        self.easybtn = Button(text="Easy", size_hint_y=0.1, size_hint_x=0.2, pos_hint={'bottom':0, 'right':1}, background_color=(0,1,0,1))
        self.easybtn.bind(on_press=self.medium)

        self.mediumbtn = Button(text="Medium", size_hint_y=0.1, size_hint_x=0.2, pos_hint={'bottom':0, 'right':1}, background_color=(0,0,1,1))
        self.mediumbtn.bind(on_press=self.hard)
        
        #self.aboutbtn = Button(text="About", size_hint_y=0.1, size_hint_x=0.1, pos_hint={'bottom':0, 'right':1})
        #self.aboutbtn.bind(on_press=self.about)
        #self.add_widget(self.aboutbtn)
    def easy(self, instance):
        self.remove_widget(self.hardbtn)
        self.df = 999
        self.easybtn = Button(text="Easy", size_hint_y=0.1, size_hint_x=0.2, pos_hint={'bottom':0, 'right':1}, background_color=(0,1,0,1))
        self.easybtn.bind(on_press=self.medium)
        self.add_widget(self.easybtn)
        return self.df
    def medium(self, instance):
        self.remove_widget(self.easybtn)
        self.df = 2999
        self.mediumbtn = Button(text="Medium", size_hint_y=0.1, size_hint_x=0.2, pos_hint={'bottom':0, 'right':1}, background_color=(0,0,1,1))
        self.mediumbtn.bind(on_press=self.hard)
        self.add_widget(self.mediumbtn)
        return self.df
    def hard(self, instance):
        self.remove_widget(self.mediumbtn)
        self.df = 9932
        self.hardbtn = Button(text="Hard", size_hint_y=0.1, size_hint_x=0.2, pos_hint={'bottom':0, 'right':1}, background_color=(1,0,0,1))
        self.hardbtn.bind(on_press=self.easy)
        self.add_widget(self.hardbtn)
        return self.df
    def next(self, instance):
        self.remove_widget(self.btn)
        self.remove_widget(self.btn2)
        self.r = randint(0,self.df) 
        self.btn = Button(text=hdict[self.r][0], size_hint_y=0.9, pos_hint={'top':1}, background_normal='', color=(0,0,0,1), font_name=font_path, font_size=40)
        self.btn.bind(on_press=self.flip)
        self.add_widget(self.btn)
        return self.r
    def about(self, instance):
        self.clear_widgets()
        self.add_widget(Label(text='Hanzi Cards Flash-Card App is based on the Chinese Character List by Frequency from hanzidb.org.\n\n Created by KJ(2019).', font_name=font_path2))
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
