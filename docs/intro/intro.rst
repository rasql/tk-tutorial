Introduction
============

Tk is a **graphical user interface** (GUI) library. It allows to create windows, buttons and all the 
other graphical elements. 
This tutorial shows how to use **object-oriented programming** (OOP) 
for making applications with the **Tk** framework. 


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

.. literalinclude:: intro2.py

:download:`intro2.py<intro2.py>`


Classic and themed widgets
--------------------------

The elements of a graphical user interface are called **widgets**. 
In Tk there are two generations of widgets:

* the classic ``tk`` widgets
* the new **themed** ``ttk`` widgets

The new themed widgets can be found in the submodule ``tkinter.ttk``. 
We import the classic and the new themed widgets with this import statement::

    import tkinter as tk
    import tkinter.ttk as ttk

This creates a **classic label** and a new **themed label**::

    tk.Label(self.root, text='tk.Label').pack()
    ttk.Label(self.root, text='ttk.Label').pack()

This creates a **classic button** and a new **themed button**::

    tk.Button(self.root, text='tk.Button').pack()
    ttk.Button(self.root, text='ttk.Button').pack()

This is a screen capture of the result. 
The new themed widgets have a gray background and the buttons have uniform size.

.. image:: intro3.png

.. literalinclude:: intro3.py

:download:`intro3.py<intro3.py>`


Let's define our own widget class
---------------------------------

We are now going to define our own Tk widget classes.
They have the following advantages:

* the **text** option has a default (Label, Button)
* the **parent** object is automatically set (root)
* all **keyword** arguments are passed on (kwargs)
* the **themed** version is used when available (ttk)

This is the new ``Label`` class:

.. literalinclude:: intro.py
   :pyobject: Label

This is the new ``Button`` class:

.. literalinclude:: intro.py
   :pyobject: Button
   

Button
------

Buttons can be clicked and are used to execute a command associated with them.
The following demo creates 4 buttons.

.. image:: intro5.png

* The **Start** button prints *Start* to the console
* The **Stop** button prints *Stop* to the console
* The **Self** button prints the button object string to the console
* The **Destroy** button removes the button from the window

.. literalinclude:: intro5.py

:download:`intro5.py<intro5.py>`


Radiobutton
-----------

Radiobuttons are active elements which can be clicked and execute actions.
Only one button is active at any one time.

.. image:: intro6.png

.. literalinclude:: intro6.py

:download:`intro6.py<intro6.py>`


Checkbutton
-----------

Checkbuttons are active elements which can be clicked and execute actions. 
Multiple checkbuttons can be selected simultaneously.

.. image:: intro7.png

.. literalinclude:: intro7.py

:download:`intro7.py<intro7.py>`


Entry field
-----------

Entry **entry** field presents the user with a single line text field 
where he can enter a string value.

.. image:: intro8.png

.. literalinclude:: intro8.py

:download:`intro8.py<intro8.py>`


Combobox
--------

A **combobox** combines a list of choices with an entry. 
The user can select from the list, but he can also enter directly a value.

.. image:: intro9.png

.. literalinclude:: intro9.py

:download:`intro9.py<intro9.py>`