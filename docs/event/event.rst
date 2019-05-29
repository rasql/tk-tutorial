Events
======

Tk events can come from various sources including:

* mouse button presses
* mouse mouvement
* keyboard
* entering/leaving widgets

Each widget can bind functions and methods to events::

    widget.bind(event, handler)

If an event matching the event pattern happens, the corresponing handler is called. 

Write events to the status bar
------------------------------

Here is an exemple which prints mouse **Button** and **Motion** events to the status bar::

    class Demo(App):
        def __init__(self):
            super(Demo, self).__init__()
            Label("Button and Motion events", font="Arial 24")
            Label('Display the event in the status bar')

            App.root.bind('<Button>', self.cb)
            App.root.bind('<Motion>', self.cb)

        def cb(self, event):
            """Callback function."""
            App.status['text'] = event    

.. autoclass:: event1.Demo

This is a screen capture of the above program.

.. image:: event1.png


Write events to a Text widget
-----------------------------

The following program sends **Button** and **Mouse** events to a Text widget,
just by changing the callback function::

    def cb(self, event):
        """Callback function."""
        App.txt.insert('end', str(event) + '\n') 

.. autoclass:: event2.Demo

This is a screen capture of the above program.

.. image:: event2.png


Detecting Enter, Leave and Return events
----------------------------------------

The following program detects these events::

    App.root.bind('<Enter>', self.cb)
    App.root.bind('<Leave>', self.cb)
    App.root.bind('<Return>', self.cb)
    App.root.bind('<Configure>', self.cb)

.. autoclass:: event3.Demo

This is a screen capture of the above program.

.. image:: event3.png