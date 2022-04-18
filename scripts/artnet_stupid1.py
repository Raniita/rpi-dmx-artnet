from stupidArtnet import StupidArtnet
import time
import random

# THESE ARE MOST LIKELY THE VALUES YOU WILL BE NEEDING
target_ip = '192.168.1.3'		# typically in 2.x or 10.x range
universe = 1										# see docs
packet_size = 10								# it is not necessary to send whole universe

# CREATING A STUPID ARTNET OBJECT
# SETUP NEEDS A FEW ELEMENTS
# TARGET_IP   = DEFAULT 127.0.0.1
# UNIVERSE    = DEFAULT 0
# PACKET_SIZE = DEFAULT 512
# FRAME_RATE  = DEFAULT 30
# ISBROADCAST = DEFAULT FALSE
a = StupidArtnet(target_ip, universe, packet_size, 30, False)

# MORE ADVANCED CAN BE SET WITH SETTERS IF NEEDED
# NET         = DEFAULT 0
# SUBNET      = DEFAULT 0

# CHECK INIT
print(a)

# ALL PACKETS ARE SAVED IN THE CLASS, YOU CAN CHANGE SINGLE VALUES
a.set_single_value(1, 255)			# set channel 1 to 255
a.set_single_value(2, 255)

# ... AND SEND
a.show()							# send data

# OR USE STUPIDARTNET FUNCTIONS
#a.flash_all()						# send single packet with all channels at 255

time.sleep(5)						# wait a bit, 1 sec

a.blackout()						# send single packet with all channels at 0
#a.see_buffer()

# ... REMEMBER TO CLOSE THE THREAD ONCE YOU ARE DONE
a.stop()

# CLEANUP IN THE END
del a
