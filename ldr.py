from pyfirmata import Arduino, util

import time

board = Arduino('/dev/ttyUSB0')
while(1==1):
    board.digital[8].write(1)
    time.sleep(0.4)
    board.digital[8].write(0)
    time.sleep(0.3)

  
    it = util.Iterator(board)
    it.start()
 
    board.analog[0].enable_reporting() 

    luz = (board.analog[0].read())
    padraoclaro = 0.0280

    print('luz',luz)
    if luz < padraoclaro:
        board.digital[13].write(1)
    else:
        board.digital[13].write(0)
