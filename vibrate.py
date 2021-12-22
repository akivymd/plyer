from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
Builder.load_string('''
#: import vibrator plyer.vibrator
<VibrationInterface>:
	orientation:"vertical"
	spacing:dp(10)
	padding:dp(10)
	MDRoundFlatIconButton:
		text:"Vibrate for 5 second"
		icon:"vibrate"
		on_release:vibrator.vibrate(5)
	MDRoundFlatIconButton:
		text:"Cancel Vibration"
		icon:"vibrate-off"
		on_release:vibrator.cancel()
	MDTextField:
		id:t
		hint_text:"Enter Pattern to vibrate"
		text:'0.5,0.5'
	MDRoundFlatIconButton:
		text:"Vibrate in pattern"
		icon:"vibrate"
		on_release:
			vibrator.pattern([float(n) for n in t.text.split(',')])
	
		
	
	
		
	
	
	

''')
class VibrationInterface(MDBoxLayout):
    pass


class VibrationApp(MDApp):
	def build(self):
   	 return VibrationInterface()

if __name__ == "__main__":
    VibrationApp().run()