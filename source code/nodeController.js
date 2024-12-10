radio.onReceivedNumber(function (receivedNumber) {
    serial.writeNumber(receivedNumber)
})
input.onButtonPressed(Button.A, function () {
    basic.showNumber(0)
    pins.servoWritePin(AnalogPin.P1, 180)
    basic.pause(2000)
})
input.onButtonPressed(Button.AB, function () {
    basic.showIcon(IconNames.Happy)
    serial.writeString("" + ("takephoto\n"))
    basic.pause(100)
})
input.onButtonPressed(Button.B, function () {
    basic.showNumber(1)
    pins.servoWritePin(AnalogPin.P1, 0)
    basic.pause(2000)
})
serial.onDataReceived(serial.delimiters(Delimiters.NewLine), function () {
    basic.showIcon(IconNames.Sad)
    basic.clearScreen()
    value = serial.readUntil(serial.delimiters(Delimiters.NewLine))
    if (value == "organic") {
        basic.showNumber(1)
        pins.servoWritePin(AnalogPin.P1, 0)
        basic.pause(2000)
    } else if (value == "recyclable") {
        basic.showNumber(0)
        pins.servoWritePin(AnalogPin.P1, 180)
        basic.pause(2000)
    }
})
let value = ""
radio.setGroup(7)
basic.forever(function () {
    basic.showIcon(IconNames.Asleep)
    pins.servoWritePin(AnalogPin.P1, 90)
})
