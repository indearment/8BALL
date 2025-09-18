def on_gesture_shake():
    global randomNumber
    basic.clear_screen()
    randomNumber = randint(0, 4)
    if randomNumber == 4:
        basic.show_string("PROBABLY")
    if randomNumber == 3:
        basic.show_string("ASK AGAIN")
    if randomNumber == 2:
        basic.show_string("YES!")
    if randomNumber == 1:
        basic.show_string("NO!")
    if randomNumber == 0:
        basic.show_string("I DON'T KNOW")
    basic.show_number(8)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

randomNumber = 0
basic.show_string("ASK A QUESTION")
basic.show_number(8)

def on_forever():
    pass
basic.forever(on_forever)
