# Raspberry Pi + OLA + DMX

Self learning about OLA (Open Lightning Architecture) on Raspberry Pi

## Objective

Open DMX interface + extra capabilities:
* Inputs: Art-Net
* Outputs: USB DMX

## Inventory
* Raspberry Pi 3B+ (Running Arch Linux ARM 64 bits)
* OLA ([Open Lightning Architecture](https://www.openlighting.org/))
* USB compatible (ex: [Anyma uDMX (cheapest usb dmx)](https://www.anyma.ch/research/udmx/))
* DMX fixture ->  LED PAR 12x3W (ex: [random DMX par led](https://www.amazon.es/Lixada-Iluminaci%C3%B3n-escenario-discoteca-Christmas/dp/B07XYZ65FS))

## Install OLA
[_Arch Linux ARM_] Run: `yay -S ola` and wait several hours

## USB rule
Must add the udev rule for USB uDMX. Other devices, check [official website](https://www.openlighting.org/ola/getting-started/device-specific-configuration/)

### Anyma uDMX

```
SUBSYSTEM=="usb*", ACTION=="add", ATTRS{idVendor}=="16c0", ATTRS{idProduct}=="05dc", MODE="0666"

SUBSYSTEM=="usb*", ACTION=="add", SYSFS{idVendor}=="16c0", SYSFS{idProduct}=="05dc", MODE="0666"
```

## Run OLA

Run as: `olad -l 3` for verbose logging

Go to `http://<IP>:9090` (tip: use `http://<IP>:9090/new`)

## Example: create universe Art-Net+uDMX
_Disclaimer_: dont use webui for create/patch universe, a bug on release 0.10.8 dont let me assigned device to universe.

1. Run `ola_dev_info` to find *Device* and *Port* info for __uDMX__ (ex: Device 7, Port 0)
2. Add output device: `ola_patch -d <device> -p <port> -u <universe id>`
3. Add input device: `ola_patch -i -d <device> -p <port> -u <universe id>`
4. Rename universe: `ola_uni_name <universe name> <universe id>`

* Delete patch: `ola_patch -r -d <device> -p <port> -u`
* More commands: [Command Line Tools](https://www.openlighting.org/ola/getting-started/command-line-tools/)

## Extra: systemd service for OLA
Credits: [Github Gist: s-light/olad.service](https://gist.github.com/s-light/fba54aa65b14a1da290f10dfa4e9dcae)

Paste on `/etc/systemd/system/olad.service`

```
[Unit]
Description=OLAD Open Lighting Architecture daemon
After=network.target

[Service]
Type=simple
User=<USER>
ExecStart=/usr/bin/olad -l 3 -c /home/<USER>/.ola/
StandardOutput=null
Restart=always

[Install]
WantedBy=multi-user.target
Alias=olad.service
```

# Python scripts

See folder `scripts`