input.onGesture(Gesture.Shake, function () {
    basic.clearScreen()
    randomNumber = randint(0, 4)
    if (randomNumber == 4) {
        basic.showString("PROBABLY")
    }
    if (randomNumber == 3) {
        basic.showString("ASK AGAIN")
    }
    if (randomNumber == 2) {
        basic.showString("YES!")
    }
    if (randomNumber == 1) {
        basic.showString("NO!")
    }
    if (randomNumber == 0) {
        basic.showString("I DON'T KNOW")
    }
    basic.showNumber(8)
})
let randomNumber = 0
basic.showString("ASK A QUESTION")
basic.showNumber(8)
basic.forever(function () {
	
})
