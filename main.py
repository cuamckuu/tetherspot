import time

from tetherspot.adb import (disable_mobile_data, enable_mobile_data,
                            is_package_running, is_screen_on, is_unlocked,
                            is_wifi_hotspot_enabled, press_power_button,
                            start_everyproxy, stop_everyproxy,
                            toggle_wifi_hotspot)

from tetherspot.gnirehtet import run_gnirehtet_pc, stop_gnirehtet_android


def main():
    while not is_unlocked():
        print('Unlock screen\n')

        if not is_screen_on():
            press_power_button()

        time.sleep(3)

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
    print('Disabling mobile data to ensure VPN sharing')
    disable_mobile_data()

    print()
    print('Starting Gniregtet')
    if True: # TODO: If gnirehtet installed
        press_power_button()
    run_gnirehtet_pc()

    while not is_unlocked():
        print('\nUnlock screen')

        if not is_screen_on():
            press_power_button()

        time.sleep(3)

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

    print()
    print('Enabling mobile data')
    enable_mobile_data()


if __name__ == '__main__':
    main()
