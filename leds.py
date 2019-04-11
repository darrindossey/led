import os

red_led="/sys/class/leds/led1"
green_led="/sys/class/leds/led0"

green_led_reset_trigger="mmc0"
red_led_reset_trigger="input"

trigger_cmd="/trigger >> /dev/null"
brightness_cmd="/brightness >> /dev/null"

def control(led_colour, state):
    if led_colour == "green":
        device = green_led

    elif led_colour = "red":
        device = red_led

    else:
        return

    if state == "on":
        os.system("echo none | tee " + device + trigger_cmd)
        os.system("echo 1 | tee " + device + brightness_cmd)
    elif state == "off":
        os.system("echo none | tee " + device + trigger_cmd)
        os.system("echo 0 | tee " + device + brightness_cmd)
    elif state == "flash":
        os.system("echo timer | tee " + device + trigger_cmd)
        os.system("echo 1 | tee " + device + brightness_cmd)
    elif state == "reset":
        if device == green_led:
            trigger=green_led_reset_trigger
        elif device == red_led:
            trigger=red_led_reset_trigger

        os.system("echo " + trigger + " | tee " + device + trigger_cmd)
        os.system("echo 1 " + device + brightness_cmd)
        else:
            return
