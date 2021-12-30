import os, platform, re, subprocess, tkinter, tkinter.filedialog, tkinter.messagebox, traceback
from tkinter import *
from sys import exit

# Debug stuff
versionString = "1.1b"
debugLevel = 2

filenameExt = ""
device = ""
cmd = ""

# OS detection
dfu = ""

print(f"DFUWrapper v{versionString}")

if platform.system() == "Windows":
    dfu = os.path.join(os.getcwd(), "dfu-util-static.exe")
else:
    dfu = "/usr/bin/dfu-util"

try:
    # Get list of devices
    if debugLevel > 0:
        print("Scanning for DFU devices")
    try:
        out = subprocess.run([dfu, "-l"], shell=True, capture_output=True, check=True).stdout.decode().split("\r\n")
    except Exception as e:
        tkinter.messagebox.showerror("Unhandled exception", traceback.format_exc())
        exit(-1)

    devices = []
    for line in out:
        if "Found DFU:" in line:
            devices.append(line[line.find('[')+1:line.find(']')])
            if debugLevel > 0:
                print(line)

    devices = list(set(devices))

    if len(devices) == 0:
        tkinter.messagebox.showerror("Error", "No supported devices found")
        exit(-1)
    else:
        if debugLevel >= 2:
            print("\nEnumerated device IDs:")
            for d in devices:
                print("\t- {}".format(d))
            print()

        # Init Tkinter
        root = Tk()
        root.resizable(False, False)
        root.title("DFUWrapper")

        mainGrid = Frame(root)
        mainGrid.grid()
        mainGrid.pack(padx=5, pady=5)

        ## Dropdown
        device = StringVar(root)
        device.set(devices[0])

        deviceSelectMenu = OptionMenu(mainGrid, device, *devices)
        Label(mainGrid, text="Select device to flash:").grid(row=1, column=1)
        deviceSelectMenu.grid(row=1,column=2)

        def dropdownUpdate(*args):
            print(device.get())

        device.trace('w', dropdownUpdate)

        ## File select button
        filenameExt = StringVar(root)
        filenameExt.set("")

        def selectFile():
            global cmd

            filenameExt.set(tkinter.filedialog.askopenfilename(filetypes=[("BIN files", "*.bin")], initialdir=".", title="Select file"))
            cmd = [dfu, "-d", device.get(), "-a", "0", "-s", "0x08000000:leave:mass-erase:force", "-D", filenameExt.get()]
            if debugLevel > 0:
                print("Selected file {}\n".format(filenameExt.get()))
            if debugLevel > 1:
                print("Prepared command:\n\t{}".format(' '.join(cmd)))
                
        fileSelectButton = Button(mainGrid, text="Select file", command=selectFile)
        fileSelectButton.grid(row=1, column=3)

        ## Flash button
        def startFlash():
            try:
                subprocess.run(cmd, shell=True, capture_output=True, check=True)
                tkinter.messagebox.showinfo("Success !", "Flashed successfully !")
            except subprocess.CalledProcessError as e:
                if debugLevel > 0 and debugLevel < 2:
                    tkinter.messagebox.showerror("Upload failed", "Could not flash board (dfu-util-static.exe returned {}".format(e.returncode))
                elif debugLevel >= 2:
                    tkinter.messagebox.showerror("Upload failed", "Could not flash board:\n\n{}".format(e.output.decode().split("\r\n\r\n")[2]))
            except OSError as e:
                tkinter.messagebox.showerror("Invalid command", "The command was invalid:\n\n{}".format(' '.join(cmd)))

        flashButton = Button(mainGrid, text="Flash", command=startFlash)
        flashButton.grid(row=1, column=4)

        root.mainloop()
except Exception as e:
    tkinter.messagebox.showerror("Error", traceback.format_exc())
