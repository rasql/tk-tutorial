Introduction to Tk
==================

Tk is a **graphical user interface** (GUI) library. It allows to create windows, buttons and all the 
other graphical elements. 
This tutorial shows how to use **object-oriented programming** (OOP) 
for making applications using the **Tk** framework. 


Our first program
-----------------

It is a tradition for the first program to write **Hello world** to the computer screen.
So here is this standard initiation ritual.

.. image:: intro1.png

So how do we do this ?
First we import the Python module ``tkinter`` (Tk interface) and give it the shortcut ``tk``::

    import tkinter as tk

Then we create the ``Tk()`` root widget which becomes the root for all other widgets::

    root = tk.Tk()

Then we create a ``Label()`` widget which has *root* as parent and *Hello world* as text attribute. 
To make the label appear on the window, we must call the ``grid()`` placement method::

    tk.Label(root, text='Hello world! Hello world!').grid()

Finally we call the Tk ``mainloop()`` method which keeps the window open until the **close** button is clicked::

    root.mainloop()

:download:`intro1.py<intro1.py>`

.. literalinclude:: intro1.py


The same in OOP
---------------

Now we rewrite this first program in OOP manner.
We start by defining the new ``App`` class::

    class App:

The constructor method ``__init__`` creates the root and the label::

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('App Demo')
        tk.Label(self.root, text='Hello Tkinter! ' * 3).pack()

The ``run`` method starts the main loop::

    def run(self):
        """Run the main loop."""
        self.root.mainloop()


Finally we instantiate the App and run it::

    if __name__ == '__main__':
        App().run()

This is the result:

.. image:: intro2.png

:download:`intro2.py<intro2.py>`

.. literalinclude:: intro2.py

Labels
------

Labels are used to add passive text to the window. 
We define a new ``Label()`` class which is added automatically to the current
context which is stored in the class variable ``App.stack[-1]``. 
For all placement of widgets we are going to use the ``grid()`` method:

.. literalinclude:: tklib.py
   :pyobject: Label

This is a screen capture of the result.

.. image:: intro3.png


:download:`intro3.py<intro3.py>`

.. literalinclude:: intro3.py


Buttons
-------

Buttons can be clicked and are used to execute a command associated with them.
The following demo creates 4 buttons::

    class Demo(App):
        def __init__(self):
            super(Demo, self).__init__()
            Label('Button demo',  font='Arial 24')
            Button('Start', 'print("Start")')
            Button('Stop', 'print("Stop")')
            Button('Self', 'print(self)')
            Button('Destroy', 'self.destroy()')

.. automodule:: intro5
   :members:

This is a screen capture of the above program.

.. image:: intro5.png

* The **Start** button prints *Start* to the console
* The **Stop** button prints *Stop* to the console
* The **Self** button prints the button object string to the console
* The **Destroy** button removes the button from the window


Radiobuttons
------------

Radiobuttons are active elements which can be clicked and execute actions. Only one button is active at any one time.

.. automodule:: intro6
   :members:

This is a screen capture of the above program.

.. image:: intro6.png


Checkbuttons
------------

Checkbuttons are active elements which can be clicked and execute actions. Multiple checkbuttons can be selected simultaneously.

.. automodule:: intro7
   :members:

This is a screen capture of the above program.

.. image:: intro7.png


Entry fields
------------

Entry **entry** field presents the user with a single line text field where he can enter a string value.

.. automodule:: intro8
   :members:

This is a screen capture of the above program.

.. image:: intro8.png

Combobox
--------

A **combobox** combines a list of choices with an entry. The user can select from the list, but he can also enter directly a value.

.. automodule:: intro9
   :members:

This is a screen capture of the above program.

.. image:: intro9.png


