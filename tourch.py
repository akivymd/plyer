#Torch app
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
from plyer import flash
Builder.load_string('''
<FlashInterface>:
	MDRectangleFlatIconButton:
		text:"Tourch On"
		size_hint_y:.5
		size_hint_x:1
		on_release:app.turn_on()
	MDRectangleFlatIconButton:
		text:"Tourch off"
		size_hint_y:.5
		size_hint_x:1
		on_release:app.turn_off()
	
	
	
''')

class FlashInterface(MDBoxLayout):
	pass


class FlashApp(MDApp):
	def turn_on(self):
		flash.on()
	def turn_off(self):
		flash.off()
	def build(self):
		return FlashInterface()
if __name__ == "__main__":
    app = FlashApp()
    app.run()