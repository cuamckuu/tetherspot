from tetherspot.adb import (is_package_running, is_wifi_hotspot_enabled,
                            start_everyproxy, stop_everyproxy,
                            toggle_wifi_hotspot)

from tetherspot.gnirehtet import run_gnirehtet_pc, stop_gnirehtet_android


def main():
    print('(Re)starting EveryProxy')
    stop_everyproxy()
    start_everyproxy()
    print('EveryProxy status:', is_package_running('com.gorillasoftware.everyproxy'))

    print()
    print('Starting WiFi hotspot if needed')
    is_hotspot_enabled = is_wifi_hotspot_enabled()
    print('WiFi hotspot status:', is_hotspot_enabled)

    if not is_hotspot_enabled:
        print('Enabling WiFi hotspot')
        toggle_wifi_hotspot()

    print()
    print('Starting Gniregtet')
    run_gnirehtet_pc()

    print()
    print('Stopping Gniregtet')
    stop_gnirehtet_android()

    print()
    print('Stopping EveryProxy')
    stop_everyproxy()
    print('EveryProxy status:', is_package_running('com.gorillasoftware.everyproxy'))

    print()
    print('Stopping WiFi hotspot if needed')
    is_hotspot_enabled = is_wifi_hotspot_enabled()
    print('WiFi hotspot status:', is_hotspot_enabled)

    if is_hotspot_enabled:
        print('Disabling WiFi hotspot')
        toggle_wifi_hotspot()


if __name__ == '__main__':
    main()