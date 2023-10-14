/*******************************************************************************
* CPU Clock Measurement Using RDTSC
*
* Description:
*     This C file provides functions to compute and measure the CPU clock using
*     the `rdtsc` instruction. The `rdtsc` instruction returns the Time Stamp
*     Counter, which can be used to measure CPU clock cycles.
*
* Author:
*     Renato Mancuso
*
* Affiliation:
*     Boston University
*
* Creation Date:
*     September 10, 2023
*
* Notes:
*     Ensure that the platform supports the `rdtsc` instruction before using
*     these functions. Depending on the CPU architecture and power-saving
*     modes, the results might vary. Always refer to the CPU's official
*     documentation for accurate interpretations.
*
*******************************************************************************/

#include <stdio.h>
#include <string.h>
#include <time.h>
#include <stdint.h>
#include <stdlib.h>
#include <unistd.h>

#include "timelib.h"

int main (int argc, char ** argv)
{
	if (argc != 4) {
        printf("Usage: %s <seconds> <nanoseconds> <s|b>\n", argv[0]);
        return 1;
    }

    long sec = atol(argv[1]);
    long nsec = atol(argv[2]);
    char method = argv[3][0];

	if (method == 's') {
		printf("WaitMethod: SLEEP\n");
		printf("WaitTime: %ld %ld \n", sec, nsec);
		uint64_t elapsed_clocks = get_elapsed_sleep(sec, nsec);
		printf("ClocksElapsed: %llu \n", elapsed_clocks);
		double elapsed_clockSpeed = (double)elapsed_clocks / (sec * NANO_IN_SEC + nsec) * (double) 1000;
		printf("ClockSpeed: %.2f", elapsed_clockSpeed);
	}
	else if (method == 'b') {
		printf("WaitMethod: BUSYWAIT\n");
		printf("WaitTime: %ld %ld \n", sec, nsec);
		uint64_t elapsed_clocks = get_elapsed_busywait(sec, nsec);
		printf("ClocksElapsed: %llu \n", elapsed_clocks);
		double elapsed_clockSpeed = (double)elapsed_clocks / (sec * NANO_IN_SEC + nsec) * (double) 1000;
		printf("ClockSpeed: %.2f", elapsed_clockSpeed);
	}
	return EXIT_SUCCESS;
}

