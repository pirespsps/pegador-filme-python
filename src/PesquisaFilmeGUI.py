from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image,AsyncImage
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import Filme

class PesquisaFilmeGUI(App):

    def __init__(self):
        super(PesquisaFilmeGUI,self).__init__()
    
    def build(self):
        label = Label(text = "Digite o nome de um filme", size_hint = (.5,.5), pos_hint = {'center_x':.5,'center_y':.5})
        return label
    