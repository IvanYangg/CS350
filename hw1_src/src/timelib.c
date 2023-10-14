/*******************************************************************************
* Time Functions Library (implementation)
*
* Description:
*     A library to handle various time-related functions and operations.
*
* Author:
*     Renato Mancuso <rmancuso@bu.edu>
*
* Affiliation:
*     Boston University
*
* Creation Date:
*     September 10, 2023
*
* Notes:
*     Ensure to link against the necessary dependencies when compiling and
*     using this library. Modifications or improvements are welcome. Please
*     refer to the accompanying documentation for detailed usage instructions.
*
*******************************************************************************/

#include "timelib.h"

/* Return the number of clock cycles elapsed when waiting for
 * wait_time seconds using sleeping functions */
long get_elapsed_sleep(long sec, long nsec)
{
	uint64_t startTSC, endTSC;
    get_clocks(startTSC);

    struct timespec req, rem;
    req.tv_sec = sec;
    req.tv_nsec = nsec;
    
    int response = nanosleep(&req, &rem);
  
    if (response != 0) {
        printf("Nap was Interrupted.\n");
    }

    get_clocks(endTSC);
	unsigned long long difference = endTSC - startTSC;
    return difference;
}

/* Return the number of clock cycles elapsed when waiting for
 * wait_time seconds using busy-waiting functions */
long get_elapsed_busywait(long sec, long nsec)
{
	struct timespec begin_timestamp, current_timestamp;
	uint64_t startTSC, endTSC;
	clock_gettime(CLOCK_MONOTONIC, &begin_timestamp);
	get_clocks(startTSC);
	while (1) {
        clock_gettime(CLOCK_MONOTONIC, &current_timestamp);

        // Calculate the elapsed time in nanoseconds
        uint64_t elapsed_ns = (current_timestamp.tv_sec - begin_timestamp.tv_sec) * NANO_IN_SEC +
                              (current_timestamp.tv_nsec - begin_timestamp.tv_nsec);

        if (elapsed_ns >= sec * NANO_IN_SEC + nsec) {
            break;
        }
    }
	get_clocks(endTSC);
	return (unsigned long long)(endTSC - startTSC);
}

/* Utility function to add two timespec structures together. The input
 * parameter a is updated with the result of the sum. */
void timespec_add (struct timespec * a, struct timespec * b)
{
	/* Try to add up the nsec and see if we spill over into the
	 * seconds */
	time_t addl_seconds = b->tv_sec;
	a->tv_nsec += b->tv_nsec;
	if (a->tv_nsec > NANO_IN_SEC) {
		addl_seconds += a->tv_nsec / NANO_IN_SEC;
		a->tv_nsec = a->tv_nsec % NANO_IN_SEC;
	}
	a->tv_sec += addl_seconds;
}

/* Utility function to compare two timespec structures. It returns 1
 * if a is in the future compared to b; -1 if b is in the future
 * compared to a; 0 if they are identical. */
int timespec_cmp(struct timespec *a, struct timespec *b)
{
	if(a->tv_sec == b->tv_sec && a->tv_nsec == b->tv_nsec) {
		return 0;
	} else if((a->tv_sec > b->tv_sec) ||
		  (a->tv_sec == b->tv_sec && a->tv_nsec > b->tv_nsec)) {
		return 1;
	} else {
		return -1;
	}
}

/* Busywait for the amount of time described via the delay
 * parameter */
uint64_t busywait_timespec(struct timespec delay)
{
	/* IMPLEMENT ME! (Optional but useful) */
}
