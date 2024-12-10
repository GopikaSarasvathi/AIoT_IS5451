let fullDistance = 0;
let halfFullDistance = 0;
radio.setGroup(7);
let timeFullInitial = 0;  
let timeHalfInitial = 0;  
let binStatus = 0;

basic.forever(function () {
    halfFullDistance = grove.measureInCentimeters(DigitalPin.P1);
    fullDistance = grove.measureInCentimeters(DigitalPin.P2);

    // full bin detection, using 4,5,6 to avoid interference in reciever with organic bin
    if (fullDistance < 20) {
        if (binStatus !== 6) {
            if (timeFullInitial === 0) { 
                timeFullInitial = input.runningTime();
            } 
			// Check if 5 seconds have passed 
			else if (input.runningTime() - timeFullInitial > 5000) {
                binStatus = 6;
                //basic.showNumber(6);
                radio.sendNumber(6);
                // Reset half full timer if full condition is met
                timeHalfInitial = 0;
            }
        }
    } else {
        timeFullInitial = 0;  
    }

    // Handling half full detection, ensuring it does not interfere with full detection
    if (halfFullDistance < 11 && binStatus !== 6) {  // Check if bin is not full
        if (binStatus !== 5) {
            if (timeHalfInitial === 0) {  
                timeHalfInitial = input.runningTime();
            } else if (input.runningTime() - timeHalfInitial > 5000) { // Check if 5 seconds have passed
                binStatus = 5;
               // basic.showNumber(5);
                radio.sendNumber(5);
            }
        }
    } else {
        timeHalfInitial = 0;  // Reset the timer if the half-full condition is no longer met
    }

    // If neither condition is met, assume bin is empty
    if (fullDistance >= 20 && halfFullDistance >= 11) {
        if (binStatus !== 4) {
            binStatus = 4;
          //  basic.showNumber(4);
            radio.sendNumber(4);
            // Reset timers for both conditions
            timeFullInitial = 0;
            timeHalfInitial = 0;
        }
    }

    basic.pause(300); 
});
