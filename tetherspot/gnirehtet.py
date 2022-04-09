import os
import subprocess
import time

from tetherspot.adb import run_adb


def run_gnirehtet_pc():
    # TODO: Handle custom paths and OS
    path = os.path.normpath('./assets/gnirehtet-rust-win64')
    os.environ["PATH"] += os.pathsep + path

    try:
        subprocess.run(['gnirehtet', 'run'], env=os.environ, shell=True)
    except:
        pass

def stop_gnirehtet_android():
    run_adb('shell am force-stop com.genymobile.gnirehtet')
    time.sleep(2)
