from tkinter import *
from stupidArtnet import StupidArtnet

# Declare globals
stupid = None
window = None

def updateValueR(slider_value):
    global stupid
    stupid.set_single_value(2, int(slider_value))

def updateValueG(slider_value):
    global stupid
    stupid.set_single_value(3, int(slider_value))

def updateValueB(slider_value):
    global stupid
    stupid.set_single_value(4, int(slider_value))


def cleanup():
    """Cleanup function for when window is closed.
    Closes socket and destroys object.
    """
    print('cleanup')

    global stupid
    #stupid.set_single_value(1, 0)
    #stupid.set_single_value(2, 0)
    stupid.stop()
    del stupid

    global window
    window.destroy()


# ARTNET CODE
# -------------

# Create artnet object
target_ip = '192.168.1.3'		
universe = 1										
packet_size = 10								
stupid = StupidArtnet(target_ip, universe, packet_size, 30, False)

# Start persistent thread
stupid.start()

stupid.set_single_value(1, 255)


# TKINTER CODE
# --------------

# Create window object
window = Tk()

slider_valR = IntVar()
scale1 = Scale(window, variable=slider_valR,
              command=updateValueR, from_=255, to=0)
scale1.pack(anchor=W)


slider_valG = IntVar()
scale2 = Scale(window, variable=slider_valG,
              command=updateValueG, from_=255, to=0)
scale2.pack(anchor=CENTER)

slider_valB = IntVar()
scale3 = Scale(window, variable=slider_valB,
              command=updateValueB, from_=255, to=0)
scale3.pack(anchor=E)

# Create label with value
label = Label(window)
label.pack()

# Cleanup on exit
window.protocol("WM_DELETE_WINDOW", cleanup)

# Start
window.mainloop()
