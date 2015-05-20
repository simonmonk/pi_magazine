import time
import RPi.GPIO as GPIO

PULSE_LEN = 0.03
A_PIN = 18
B_PIN = 23
# BUTTON_PIN = 24

# Configure the GPIO pins
GPIO.setmode(GPIO.BCM)
# GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(A_PIN, GPIO.OUT)
GPIO.setup(B_PIN, GPIO.OUT)

# Glogal variables
positive_polarity = True

def tick():
	# Alternate positive and negative pulses
	if positive_polarity:
		pulse(A_PIN, B_PIN)
	else:
		pulse(B_PIN, A_PIN)
	# Flip the polarity ready for the next tick
	positive_polarity = not positive_polarity
		
def pulse(pos_pin, neg_pin):
	# Turn on the pulse
	GPIO.output(pos_pin, True)
	GPIO.output(neg_pin, False)
	time.sleep(PULSE_LEN)
	# Turn the power off until the next tick
	GPIO.output(pos_pin, False)

try:
	while True:
		tick()
		time.sleep(1)
finally:
    print('Cleaning up GPIO')
    GPIO.cleanup()
