# Tetherspot

Script to simlify reverse USB tethering with WiFi hotspot on **non-rooted** Android

![diagram](./assets/diagram.drawio.png)

## Idea

- Use [Gnirehtet](https://github.com/Genymobile/gnirehtet) on PC to start reverse USB tethering
- Use [Every Proxy](https://play.google.com/store/apps/details?id=com.gorillasoftware.everyproxy&hl=en&gl=US) on Android to run proxy server
- Enable WiFi hotspot on Android
- Connect to created WiFi and specify proxy address

## `Tetherspot` could automate this process by

- Downloading and installing `adb` if needed
- Downloading and installing propper Gnirehtet version
- Downloading and installing EveryProxy apk
- Starting/stopping Gnirehtet, Every Proxy and WiFi hotspot in one command

## Usage

> Work in progress

---

## TODO

- [X] Run `adb` commands from Python
- [X] Enable wifi hotspot from `adb`
- [X] Disable wifi hotspot from `adb``adb`
- [X] Enable proxy server from `adb`
- [X] Disable proxy server from `adb`
- [X] Run Gnirehtet from Python
- [ ] Check that device unlocked
- [ ] Disable mobile network to ensure reverse tethering works
- [X] Cleanup Gnirehtet on android side
- [X] Working Windows prototype
- [ ] Determine OS version to get propper Gnirehtet
- [ ] Install EveryProxy if needed
- [ ] Install ADB if needed
- [ ] Write own Android proxy server (TCP, UDP, IPv6, netty, ktor)
