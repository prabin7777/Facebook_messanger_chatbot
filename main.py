import pyautogui as pt
from time import sleep
import pyperclip
from data import datap

sleep(3)

position1 = pt.locateOnScreen("messanger/smile.png", confidence=.5)
x=position1[0]
y=position1[1]


# gets message
def get_message():
    global x,y

    position = pt.locateOnScreen("messanger/smile.png", confidence=.5)
    x=position[0]
    y=position[1]
    pt.moveTo(x,y, duration=.05)
    pt.moveTo(x+70, y-40 , duration=0.5)
    pt.tripleClick()
    pt.hotkey('ctrl', 'c')
    pt.click()
    message= pyperclip.paste()
    print("message recieved "+message)
    return message


# post
def post_response(message):

    global x,y
    position = pt.locateOnScreen("messanger/smile.png", confidence=.5)
    x = position[0]
    y = position[1]
    pt.moveTo(x+200,y+27)
    pt.click()
    pt.typewrite(message)
    pt.typewrite('\n')


# process
# def process_response(message):
#
#   datap(message)

# check message
def check_message():
    pt.moveTo(x+50,y-26)
    while True:
#         continuous check
          try:
              position = pt.locateOnScreen("messanger/dot.png",confidence=.7)
              if position is not None:
                  pt.moveTo(position)
                  pt.moveRel(-100,0)
                  pt.click()
                  sleep(.5)



          except(Exception):
              print("no new messages")




          processed = datap(get_message())
          post_response(processed)


          sleep(5)







processed=datap(get_message())

post_response(processed)
check_message()