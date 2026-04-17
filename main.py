from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class AppUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.label = Label(text="🚀 AI TikTok PRO MAX")

        btn = Button(text="تشغيل AI")
        btn.bind(on_press=self.run_ai)

        self.add_widget(self.label)
        self.add_widget(btn)

    def run_ai(self, instance):
        self.label.text = "🤖 AI يعمل... جاهز للنشر"

class MyApp(App):
    def build(self):
        return AppUI()

MyApp().run()
