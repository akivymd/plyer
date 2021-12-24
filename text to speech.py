from kivy.lang import Builder
from kivymd.app import MDApp
from plyer import tts
from kivymd.uix.screen import MDScreen
Builder.load_string(
"""
<Text_to_speech>:
	MDFloatLayout:
		md_bg_color:1,0,0,1
		MDLabel:
			text:"Text to speech converter"
			pos_hint:{"center_x":.6,"center_y":.86}
			font_size:dp(40)
		MDFloatLayout:
			size_hint:1,.15
			pos_hint:{"center_x":.5,"center_y":.6}
			canvas:
				Color:
					rgb:1,1,1,1
				RoundedRectangle:
					size:self.size
					pos:self.pos
			MDTextField:
				id:spe
				hint_text:"Hello Write Here"
				pos_hint:{"center_x":.5,"center_y":.6}
		MDRectangleFlatIconButton:
			text:"speak"
			icon:"speaker"
			pos_hint:{"center_x":.5,"center_y":.56}
			on_release:app.speak()
				
				

				
				
	
	
""")

class Text_to_speech(MDScreen):
	pass

#Thanks for watching
class Test(MDApp):
	def speak(self):
		tts.speak(self.root.ids.spe.text)
	def build(self):
		return Text_to_speech()
Test().run()