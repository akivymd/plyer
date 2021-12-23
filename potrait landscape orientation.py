from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
Builder.load_string('''
#:import orientation plyer.orientation
<Orien>:
	MDBoxLayout:
		size_hint_y:.5
		MDGridLayout:
			cols:2
			MDRoundFlatIconButton:
				text:"Change to landscape"
				icon:"phone-rotate-landscape"
				on_release:orientation.set_landscape()
			MDRoundFlatIconButton:
				text:"Change to Portrait"
				icon:"phone-rotate-portrait"
				on_release:orientation.set_portrait()
			MDRoundFlatIconButton:
				text:"Free sensor"
				icon:"crop"
				on_release:orientation.set_sensor(mode='any')
			MDRoundFlatIconButton:
				text:"Reverse landscape"
				icon:"phone-rotate-landscape"
				on_release:orientation.set_landscape(reverse=True)
			MDRoundFlatIconButton:
				text:"Change landscape"
				icon:"phone-rotate-landscape"
				on_release:orientation.set_sensor(mode='landscape')
			MDRoundFlatIconButton:
				text:"Change to portrait"
				icon:"phone-rotate-portrait"
				on_release:orientation.set_sensor(mode='portrait')
#Thanks for watching

''')
class Orien(MDScreen):
	pass
class Test(MDApp):
	def build(self):
		return Orien()
Test().run()
