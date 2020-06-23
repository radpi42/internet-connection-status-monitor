import connection
import time


counter_mes = '''times run: %d'''
count = 0

def connect():
    try:
        connection.check()
        return True
    except:
        return False


while True:
        
    while connection.check() == True:   
        print(connection.check())
        print("Connected")
        count +=1

        print(counter_mes %count)
        time.sleep(1)
    else:
        print('no connection')
        count +=1
        print(counter_mes %count)
        time.sleep(1)
