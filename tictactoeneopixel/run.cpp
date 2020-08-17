#include "../Neopixel/ws2812-rpi.h"
#include "../tictactoeTD/Player.hpp"

#include <wiringPi.h>

int main (void)
{
	wiringPiSetup(); // initializes the wiringPi library
	pinMode(0, OUTPUT); // sets GPIO pin 0 to OUTPUT mode
	while (1) { // infinite loop that toggles the light in a 1000 ms period, with a 50% duty cycle
		digitalWrite(0, HIGH);
		delay(500);
		digitalWrite(0, LOW);
		delay(500);
	}
	return 0; // unreachable
}
