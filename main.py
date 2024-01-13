# calculator.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        self.operators = ['+', '-', '*', '/']
        self.last_was_operator = None
        self.last_button = None

        layout = BoxLayout(orientation='vertical', spacing=10)
        self.text_input = TextInput(multiline=False, readonly=True, halign='right', font_size=32)
        layout.add_widget(self.text_input)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['.', '0', '=', '+']
        ]

        for row in buttons:
            h_layout = BoxLayout(spacing=10)
            for label in row:
                button = Button(text=label, pos_hint={'center_x': 0.5, 'center_y': 0.5})
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            layout.add_widget(h_layout)

        return layout

    def on_button_press(self, instance):
        current_input = self.text_input.text
        button_text = instance.text

        if button_text == '=':
            try:
                result = str(eval(current_input))
                self.text_input.text = result
            except Exception as e:
                self.text_input.text = 'Error'
        else:
            if self.last_button in self.operators and button_text in self.operators:
                return  # Avoid consecutive operators
            new_input = current_input + button_text
            self.text_input.text = new_input

        self.last_was_operator = button_text in self.operators
        self.last_button = button_text

if __name__ == '__main__':
    CalculatorApp().run()
