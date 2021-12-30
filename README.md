[![License: GPL v2](https://img.shields.io/badge/License-GPL_v2-blue.svg)](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html)

# dfu-utils wrapper

A hastily coded wrapper to upload firmware to Black Pill (based) boards (aka STM32F4xx family) through DFU.

## Requirements:

For Windows users:
- The latest dfu-utils binary release (http://dfu-util.sourceforge.net/)
- Zadig (more on that later) (https://zadig.akeo.ie/)
- The .exe you can grab in the Releases page (see next section)

For everybody running \*NIX (Linux, macOS, BSD...):
- dfu-utils
- The Python script

## How to use:

In all cases, plug your board in bootloader mode (hold BOOT0 on the Black Pill then plug it in) first !

### If you don't have/don't want to bother with a Python 3 installation (largely applies to most Windows users):

- Extract the dfu-utils binary package somewhere
- From there, take the file named "dfu-util-static(.exe)" and put it in the same folder as DFUWrapper.exe
- Launch DFUWrapper.exe
- Pick a device to flash
- Select a BIN image to flash onto the device
- Press the "Flash" button

### If you have a working Python 3 installation/generally don't run on Windows:

- Install dfu-utils through your package manager (I have no idea if brew has that on macOS though)
- Launch the DFUWrapper script, root might be needed for device access
- Pick a device to flash
- Select a BIN image to flash onto the device
- Press the "Flash" button

### If DFUWrapper doesn't see your board/complains about corrupted firmware (Windows only):

- Plug in your board through USB, in bootloader mode
- Fire up Zadig
- Select your device ID (it *should* be called STM32 BOOTLOADER; if it doesn't show up, tick "List all devices" under the Options tab)
- In the right spinbox, select WinUSB
- Install driver


## Some questions people might ask:

### Q: Why GPLv2 ?
A: The original plan was to licence this using WTFPL, but dfu-utils is GPL software, therefore DFUWrapper has to be GPL as well. But in spirit, it is WTFPL, so hack it as much as you want !

### Q: Why aren't you bundling dfu-utils/Zadig with your release ?
A: It's a bit of the same answer. Zadig is GPLv3 and dfu-utils is GPLv2, but DFUWrapper being (loosely licensed as) WTFPL, I think I can't legally bundle them. IANAL though, neither do I speak legalese, so consider this as just me covering my ass. I have some serious doubts anybody would come after me were I to bundle either of those softwares with DFUWrapper, but for the sake of not even trying to step on anyone's toes, I won't ! Sorry for the inconvenience.

### Q: Can I use it to flash other DFU compatible boards ?
A: I think ? I only really tried with the WeAct STM32F411CEU Black Pill v3.0, and in fact I don't think I own any other DFU compatible boards
