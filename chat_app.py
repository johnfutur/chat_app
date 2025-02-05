import os
import sys
import logging

# Set environment variables to suppress Kivy logs
os.environ['KIVY_NO_CONSOLELOG'] = '1'
os.environ['KIVY_LOG_LEVEL'] = 'error'

# Redirect stdout and stderr to suppress all terminal output
sys.stdout = open(os.devnull, 'w')
sys.stderr = open(os.devnull, 'w')

# Disable all logging globally
logging.disable(logging.CRITICAL)

from kivy.config import Config
Config.set('kivy', 'log_level', 'error')


from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget
from kivy.core.window import Window
from kivy.app import App


KV = '''
MDScreen:
    md_bg_color: app.theme_cls.bg_dark
    

    MDBoxLayout:
        orientation: "vertical"
        spacing: "10dp"
        padding: "10dp"

        MDTopAppBar:
            title: "Chat Box"
            elevation: 10
            left_action_items: [["menu", lambda x: None]]
            md_bg_color: app.theme_cls.primary_dark

        MDScrollView:
            size_hint_y: 0.7
            MDList:
                id: chat_list

        MDBoxLayout:
            # This box occupies the full width of the screen.
            size_hint_x: 1
            size_hint_y: None
            height: "80dp"   # Adjust height as needed
            orientation: "horizontal"
            spacing: "10dp"
            padding: "10dp"
            md_bg_color: [0.3, 0.815, 0.882, 1]  # Slightly light cyan (approx. Cyan 300)
            radius: [20,]

            MDTextField:
                id: input_text
                hint_text: "Enter text"
                multiline: True
                size_hint_x: 0.80   # Takes up most of the horizontal space
                theme_text_color: "Custom"
                text_color_normal: 0, 0, 0, 1         # Black text for readability
                text_color_focus: 0, 0, 0, 1          # Black text for readability
                hint_text_color_normal: 0, 0, 0, 1   # Dark hint text
                hint_text_color_focus: 0, 0, 0, 1   # Dark hint text
                line_color_normal: 0, 0, 0, 1   # Black border when not focused
                line_color_focus: 0, 0, 0, 1    # Black border when focused
                mode: "rectangle"

            MDFloatingActionButton:
                icon: "arrow-up"
                md_bg_color: app.theme_cls.primary_color
                on_release: app.update_chat()
                size_hint: None, None
                size: "40dp", "40dp"  # Adjust to control button size

        MDBoxLayout:
            size_hint_y: None
            height: "25dp"
            MDLabel:
                text: "All Rights Reserved \u00A9 2025  [b]APPS Factory PH[/b]"
                markup: True
                halign: "center"
                theme_text_color: "Hint"  # Subtle but readable
                font_size: "12sp"
'''

class MyApp(MDApp):
    
    title = "Chatter Buzz"  # Set the app title
    
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Cyan"
        self.icon = 'app.png'
        Window.bind(on_request_close=self.on_request_close)
        return Builder.load_string(KV)
    def on_request_close(self, *args):
        """Handle the window close event."""
        App.get_running_app().stop()  # Stop the app properly
        Window.close()  # Ensure window closes
        return True  # Allow the window to close
    def on_start(self):
        # Ensure the window title is updated when the app starts.
        Window.title = self.title
        
        Window.size = (412, 720)
        # Get screen resolution
        screen_width, screen_height = Window.system_size

        # Center the window on the screen
        Window.left = (screen_width - 250) / 2
        Window.top = (screen_height - 630) / 2


    def update_chat(self):
        # Get the text from the text field
        text = self.root.ids.input_text.text.strip()
        if text:
            # Create a new list item with an account icon and the typed text
            item = OneLineIconListItem(text=text)
            icon = IconLeftWidget(icon="account")
            item.add_widget(icon)
            self.root.ids.chat_list.add_widget(item)
            # Clear the text field
            self.root.ids.input_text.text = ""
            

MyApp().run()
