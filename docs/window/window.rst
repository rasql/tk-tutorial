Windows
=======

In this section we present how to create new windows and 
how to open dialog windows.

In order open a new window we instantiate the ``Toplevel`` class. 
To create new windows, we create a new ``Window`` class::

    class Window():
        """Create a new window."""
        def __init__(self, title='Window'):
            top = tk.Toplevel(App.root)
            top.title(title)
            frame = ttk.Frame(top, width=300, height=200, padding=(5, 10))
            frame.grid()
            App.stack.append(frame)

First we create a toplevel window and add a title to it::

    top = tk.Toplevel(App.root)
    top.title(title)

Then we add a themed frame widget in order to get the theme's background color, 
add the geometry manager (grid) and place the frame on the widget stack,
so new widgets are added to the new window::

    frame = ttk.Frame(top, width=300, height=200, padding=(5, 10))
    frame.pack()
    App.stack.append(frame)

.. autoclass:: tklib.Window
   :members:

Create new windows
------------------

The following example adds two more windows besides the root window. 
Each one can be closed individually, but only if the root window is 
closed, the application ends::

    Window('Text')
    Text(height=10, width=40)

    Window('Canvas')
    Canvas()


.. automodule:: window1
   :members:

This is a screen capture of the above program.

.. image:: window1.png

The buttons have the following functions:

* **New Window** creates a new window
* **Print window geometry** prints the window placement (191x175+47+51)
* **Print window title** prints the window title (Window and dialogs)

* **Resize H** allows for only horizontal resizing
* **Resize V** allows for only vertical resizing
* **Iconify** iconifies the window

Standard dialogs
----------------

Tk provides multiple standard dialogs for 

* asking the open file name
* asking the save file name
* asking a directory name
* finding a color

.. automodule:: window2
   :members:

This is a screen capture of the above program.

.. image:: window2.png

Alert and confirmation dialogs
------------------------------

Tk provides multiple standard dialogs for showing

* info
* error
* question
* warning

.. automodule:: window3
   :members:

This is a screen capture of the above program.

.. image:: window3.png


Add widgets and separators
---------------------------

The following demo program shows how to insert buttons, labels and separators.

.. automodule:: window4
   :members:

This is a screen capture of the above program.

.. image:: window4.png


The Labelframe widget
---------------------

The **Labelframe** widget is a frame used for grouping widgets, 
but has a label attached to it

.. automodule:: window5
   :members:

This is a screen capture of the above program.

.. image:: window5.png

Paned windows
---------------------

The **Panedwindow** widget creates a slider and allows to change 
the width or hight between two or more widgets.

.. automodule:: window6
   :members:

This is a screen capture of the above program.

.. image:: window6.png

Tabbed notebooks
----------------

The **Notebook** widget creates a section with tabbed frames.

.. automodule:: window7
   :members:

This is a screen capture of the above program.

.. image:: window7.png


Add more tabs
-------------

In the following example we add more tabs by clicking on a button.

.. automodule:: window8
   :members:

This is a screen capture of the above program.

.. image:: window8.png