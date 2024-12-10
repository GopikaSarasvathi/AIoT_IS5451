let fullDistance = 0;
let halfFullDistance = 0;
radio.setGroup(7);
let timeFullInitial = 0;  
let timeHalfInitial = 0; 
let binStatus = 0;

basic.forever(function () {
    halfFullDistance = grove.measureInCentimeters(DigitalPin.P1);
    fullDistance = grove.measureInCentimeters(DigitalPin.P2);

    // full bin detection
    if (fullDistance < 20) {
        if (binStatus !== 3) {
            if (timeFullInitial === 0) {  
                timeFullInitial = input.runningTime();
            }
            // Check if 5 seconds have passed
            else if (input.runningTime() - timeFullInitial > 5000) { 
                binStatus = 3;
                radio.sendNumber(3);
                // Reset half full timer if full condition is met
                timeHalfInitial = 0;
            }
        }
    } else {
        timeFullInitial = 0;  
    }

    // Handling half full detection, ensuring it does not interfere with full detection
    if (halfFullDistance < 11 && binStatus !== 3) {  // Check if bin is not full
        if (binStatus !== 2) {
            if (timeHalfInitial === 0) {  
                timeHalfInitial = input.runningTime();
            } else if (input.runningTime() - timeHalfInitial > 5000) { // Check if 5 seconds have passed
                binStatus = 2;
                //basic.showNumber(2);
                radio.sendNumber(2);
            }
        }
    } else {
        timeHalfInitial = 0;  // Reset the timer if the half-full condition is no longer met
    }

    // If neither condition is met
    if (fullDistance >= 20 && halfFullDistance >= 11) {
        if (binStatus !== 1) {
            binStatus = 1;
            //basic.showNumber(1);
            radio.sendNumber(1);
            // Reset timers for both conditions
            timeFullInitial = 0;
            timeHalfInitial = 0;
        }
    }

    basic.pause(300); 
});
