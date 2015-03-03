from bottle import route, run, template, request
import RPi.GPIO as GPIO
import time

PASSWORD = 'letmein'
MAX_ATTEMPTS = 5
OPEN_TIME = 5
IP_ADDRESS = '192.168.1.14'

GPIO.setmode(GPIO.BCM)
LED_PIN = 18
GPIO.setup(LED_PIN, GPIO.OUT)

attempts = 0;

def unlock_door():
    GPIO.output(LED_PIN, True)
    time.sleep(OPEN_TIME)
    GPIO.output(LED_PIN, False)

@route('/')
def index(name='time'):
    return template('home.tpl')
    
@route('/unlock', method='POST')
def new_item():
    global attempts
    pwd = request.POST.get('password', '').strip()
    if attempts > MAX_ATTEMPTS:
        return template('lockout.tpl')
    if pwd == PASSWORD:
        attempts = 0
        unlock_door()
        return template('opened.tpl')
    else:
        attempts += 1
        return template('failed.tpl')
        
try: 
    run(host=IP_ADDRESS, port=80)
finally:  
    print('Cleaning up GPIO')
    GPIO.cleanup()