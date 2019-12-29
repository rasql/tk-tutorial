Button
======

Let's start with a simple example of creating a button
which displays some text.

A one-button program
--------------------

First we import the ``tkinter`` module and give it the shorter name ``tk``::

    import tkinter as tk

Then we create a ``Tk`` root object which represents the window
and will be the parent for all the other widgets::

    root = tk.Tk()

Then we create a button object which has root as parent,
and to which we give the text *Hello world*.
This object calls the method ``pack()``
which makes the button visible in the window.
Finally root calls the ``mainloop()`` method to start the program::

    tk.Button(root, text="Hello World").pack()
    root.mainloop()

.. image:: button1.png

.. literalinclude:: button1.py

:download:`button1.py<button1.py>`

Convert feet to meters
----------------------

Now let's create a real application.
Let's create a small program which has an input, an output
and does something when you press a button (or when you hit the return key).
It's a small program which converts feet to meters.

.. image:: button2.png

After importing the **classic Tk** module as ``tk``
we define the ``calculate`` function which gets the feet value 
and converts it to the meter value::

    def calculate(*args):
        try:
            value = float(feet.get())
            meters.set(0.3048 * value)
        except ValueError:
            pass

Then we create the ``root`` object and give a title to the window::

    root = tk.Tk()
    root.title("Feet to meters")

Two of the widgets, the entry widget and the label widget,
have special ``StringVar`` variables::

    feet = tk.StringVar()
    meters = tk.StringVar()

Now it's time to create the three widgets:

* an entry widget with the text variable ``feet``
* a button widget with the command function ``calculate``
* a label widget with the text variable ``meters```

All three widgets are placed with the ``pack()`` method::

    tk.Entry(root, width=10, textvariable=feet).pack()
    tk.Button(root, text='Convert feet to meters', command=calculate).pack()
    tk.Label(root, textvariable=meters).pack()

Finally we bind the ``calculate`` function also to the **Return** key
and start the main loop::

    root.bind('<Return>', calculate)
    root.mainloop()

:download:`button2.py<button2.py>`

.. literalinclude:: button2.py

Concepts
--------

To understand Tk you need to understand:

* widgets
* geometry management
* events

Widgets are the things you can see on the screen,
for example a label, an entry field or a button.
Later you will see checkboxes, radiobuttons, and listboxes.
Widgets are often referred to as controls.

Widgets are objects, instances of classes.
In the example above we had the following 2-level hierarchy:

* root (Tk)

  * entry (Entry class)
  * button (Button class)
  * label (Label class)

When you create a widget, you must pass its parent as the first argument.
Whether you save the object under a variable is up to you.
It depends if you need to refer to it later on.
Because it is inserted into the widget hierarchy, it won't be garbage collected.

Just creating the widget does not yet display it in the window.
You need to make a call to a geometry manager.

Event bindings
--------------

Each widget in Tk can have event bindings. 
In the following example we bind a function to these events:

* enter the widget
* leave the widget
* click the mouse button

Tk expects an event callback function which has an **event object**
as its first argument. Here we define a ``lambda`` function
with an event argument ``e``, but we do not use it here.

Event handlers can be set up for:

* the individual widget
* a class of widgets
* the toplevel window

.. image:: bind1.png

.. literalinclude:: bind1.py

:download:`bind1.py<bind1.py>`


Frame
-----

The frame widget displays just a rectangle. 
It primarily is used as a container for other widgets.
A frame has these common options:

* padding - extra space inside the frame
* borderwidth
* relief (flat, raised, sunken, solid, ridge, grove)
* width
* height

The example below shows the 6 different relief types
and uses a borderwidth of 5.

.. image:: frame1.png

.. literalinclude:: frame1.py

:download:`frame1.py<frame1.py>`


Label
-----

The label widget displays a static text, for example the text
next to an entry. User do normally not interact with a label.

Common options are:

* ``text`` - a static text
* ``textvariable`` - a dynamic text from a variable
* ``image`` - an image to be displayed
* ``compound`` - conter, top, bottom, left, right
* ``justifiy`` - left, center, right
* ``wraplength`` - linelength for long labels

The following example shows a label with a static text
and another with a dynamic text.
If both are defined, the dynamic text will have precedence.
The ``font`` keyword takes a string with the font family and font size.
The ``foreground`` keyword takes a color string.

.. image:: label1.png

.. literalinclude:: label1.py

:download:`label1.py<label1.py>`


Labels also accept the ``relief`` keyword.

.. image:: frame1.png

.. literalinclude:: label2.py

:download:`label2.py<label2.py>`

Button
------

Buttons have a ``command`` keyword which allows to specify a function.
This function is called, but without an argument.
We can use the ``lambda`` function to create a function on the fly and 
provide an argument.

Pressing the 3 buttons one after another writes this to the console::

    button 1
    button 2
    button 3

.. literalinclude:: button3.py

:download:`button3.py<button3.py>`


Checkbutton
-----------

A **checkbutton** is like a regular button,
with a label and a callback function,
but it also holds and displays a binary state.

The ``Checkbutton`` object has the following attributes:

* **parent** - the parent object
* **text** - the label to display
* **command** - the callback function
* **variable** - the variable holding the state value
* **onvalue** - the value when in the ON state
* **offvalue** - the value when in the OFF state

Here is an example of 3 checkbuttons

.. image:: check1.png

The callback function ``cb`` writes this to the console::

    --- languages ---
    English 1
    German 0
    French fluent

We notice that the default offvalue is ``0`` and the default onvalue is ``1``.
In our case:

* var0 toggles between ``0`` and ``1``
* var1 toggles between ``barely`` and ``1``
* var2 toggles between ``0`` and ``fluent``

.. literalinclude:: check1.py

:download:`check1.py<check1.py>`

Now let us rewrite this program by using lists.

.. literalinclude:: check2.py

:download:`check2.py<check2.py>`

A better Checkbutton class
--------------------------

It's time now to define a new and better ``Checkbutton`` class which can do everything in one line::

    Checkbutton('English;German;French', 'print(self.selection)')

* the items are declared as a **semicolon-separated list**
* the command is a string to be evaluated in the Checkbutton environment
* the items are available in ``self.items``
* the selected items are available in ``self.selection``
* the selection states are available in ``self.val``

This is the result written to the console for three consecutive selections::

    ['French']
    ['German', 'French']
    ['English', 'German', 'French']

.. literalinclude:: check3.py

:download:`check3.py<check3.py>`

Now let's see how this class is defined

.. literalinclude:: tklib.py
   :pyobject: Checkbutton

Entry
-----

An **entry** widget presents the user an empty field
where he can enter a text value.

.. image:: entry1.png

Each ``Entry`` object has these options:

* **parent** - the parent object
* **textvariable** - the text variable to hold the entered string
* **width** - the numbers of characters
* **show** - to indicate ``*`` for passwords

They do not have a ``text`` or ``image`` option.
You have to use a label widget instead.

.. literalinclude:: entry1.py

:download:`entry1.py<entry1.py>`


A better Entry class
--------------------

It's time now to define a new and better ``Entry`` class
which can do everything in one line::

    Entry('First name:', 'print(self.var.get())')

This new class has the attributes:

* **label** - to automatically add label in front of the entry field
* **cmd** - to execute a command string when hitting the Return key
* **val** - a default value

.. image:: entry2.png

The command function evaluates the expression entered and
displays the result in the following label widget::

    Entry('Enter expression', 'App.res["text"] = eval(self.var.get())')
    App.res = Label('Result')

.. literalinclude:: entry2.py

:download:`entry2.py<entry2.py>`

Now let's see how this class is defined

.. literalinclude:: tklib.py
   :pyobject: Entry

