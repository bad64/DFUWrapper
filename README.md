[![License: GPL v2](https://img.shields.io/badge/License-GPL_v2-blue.svg)](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html)

# dfu-utils wrapper

A hastily coded wrapper to upload firmware to Black Pill (based) boards (aka STM32F4xx family) through DFU.

## Requirements:

- The latest dfu-utils binary release (http://dfu-util.sourceforge.net/)
- Zadig (more on that later) (https://zadig.akeo.ie/)
- The .exe you can grab in the Releases page

## How to

### ONE-TIME ONLY: Use Zadig to install libusb

- Plug in your board through USB, in bootloader mode (hold BOOT0 on the Black Pill then plug it in)
- Fire up Zadig
- Select your device ID (it *should* be called STM32 BOOTLOADER; if it doesn't show up, tick "List all devices" under the Options tab)
- In the right spinbox, select libusb0
- Install driver

### Actual flashing

- Extract the dfu-utils binary package somewhere
- From there, take the file named "dfu-util-static(.exe)" and put it in the same folder as DFUWrapper.exe
- Launch DFUWrapper.exe
- Pick a device to flash
- Select a BIN image to flash onto the device
- Press the "Flash" button

## Troubleshooting

### DFUWrapper fails to detect dfu-util-static.exe
It most likely isn't in the same folder. You really do need to extract both

### The flashing fails with an error message about a corrupted device
TODO
