from tetherspot.adb import (is_package_running, is_wifi_hotspot_enabled,
                            start_everyproxy, stop_everyproxy,
                            toggle_wifi_hotspot)







def main():
    #run_adb('shell input keyevent KEYCODE_APP_SWITCH')

    # EveryProxy test
    print('EveryProxy status:', is_package_running('com.gorillasoftware.everyproxy'))
    start_everyproxy()
    print('EveryProxy status:', is_package_running('com.gorillasoftware.everyproxy'))
    stop_everyproxy()
    print('EveryProxy status:', is_package_running('com.gorillasoftware.everyproxy'))

    # WiFi test
    print('WiFi hotspot status:', is_wifi_hotspot_enabled())
    toggle_wifi_hotspot()
    print('WiFi hotspot status:', is_wifi_hotspot_enabled())


if __name__ == '__main__':
    main()