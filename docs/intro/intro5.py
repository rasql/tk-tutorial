from tklib import *
app = App('Buttons')

Button('Start', 'print("Start")')
Button('Stop', 'print("Stop")')
Button('Self', 'print(self)')
Button('Destroy', 'self.destroy()')
    
app.run()