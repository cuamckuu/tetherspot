import re
import subprocess
import time


def run_adb(command):
    res = subprocess.run(['adb'] + command.split(), capture_output=True)
    time.sleep(0.1)
    return res


def is_package_running(package_name: str):
    output = run_adb(f'shell pidof {package_name}').stdout.decode()
    return output.strip() != ''


def start_everyproxy():
    run_adb('shell am start -S com.gorillasoftware.everyproxy/.EveryProxyActivity')
    run_adb('shell input keyevent KEYCODE_DPAD_DOWN')
    run_adb('shell input keyevent KEYCODE_ENTER')
    run_adb('shell input keyevent KEYCODE_DPAD_DOWN')
    run_adb('shell input keyevent KEYCODE_ENTER')
    run_adb('shell input keyevent KEYCODE_HOME')
    time.sleep(2)


def stop_everyproxy():
    run_adb('shell am force-stop com.gorillasoftware.everyproxy')
    time.sleep(2)


def toggle_wifi_hotspot():
    run_adb('shell am start -S com.android.settings/.TetherSettings')
    run_adb('shell input keyevent KEYCODE_DPAD_UP')
    run_adb('shell input keyevent KEYCODE_DPAD_DOWN')
    run_adb('shell input keyevent KEYCODE_ENTER')
    run_adb('shell input keyevent KEYCODE_HOME')
    time.sleep(2)


def is_wifi_hotspot_enabled():
    output = run_adb('shell dumpsys connectivity').stdout.decode()

    pattern = 'ap\d'
    if match := re.search('tetherableWifiRegexs: \[(.*)\]', output):
        pattern = match.group(1)

    match = re.search(f'{pattern} - TetheredState', output)
    return (match is not None)
