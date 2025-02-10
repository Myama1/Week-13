import numpy as np
import matplotlib.pyplot as plt
import glob
import natsort
from matplotlib.animation import FuncAnimation

def read_config(filename, skip=2):
    """Reading an vicsek configuration from a file handle"""
    with open(filename) as file_handle:
        # skip the first two lines
        for i in range(skip): 
            next(file_handle)

        data = np.loadtxt(file_handle)
        conf = {}

        conf["id"] = data[:,0]
        conf["x"] = data[:,1]
        conf["y"] = data[:,2]
        conf["theta"] = data[:,3]
        conf["vx"] = np.cos(conf["theta"])
        conf["vy"] = np.sin(conf["theta"])  
        return conf

def plot(conf,ax):
    qv = ax.quiver(conf["x"], conf["y"], conf["vx"], conf["vy"], conf["theta"], scale=1, scale_units='xy', cmap='hsv')
    ax.set_aspect('equal')
    return qv

#if __name__ == "__main__":
    filename = "init.conf"
    conf = read_config(filename)

    fig,ax = plt.subplots(figsize=(5,5))
    plot(conf,ax)

    plt.savefig("vicsekarrow.png")
    print("plot saved as 'vicsekarrow.png'")


# files are stored in a folder
files = natsort.natsorted(glob.glob("frames/*"))

# first plot
fig, ax= plt.subplots() #

qv = plot(read_config(files[0]),ax)
plt.axis('equal')
plt.axis('off')

# function called to plot all files
def animate(i):
    print(i)
    conf = read_config(files[i])
    pos = np.array(list(zip(conf["x"], conf["y"])))
    print(pos)
    qv.set_offsets(pos)
    qv.set_UVC(conf["vx"], conf["vy"], conf["theta"])
    
# Create the animation
anim = FuncAnimation(fig,animate, frames = len(files), interval = 100)

anim.save("vicsekanim.mp4",writer = "ffmpeg",fps=30)
# Show the animation
plt.show()