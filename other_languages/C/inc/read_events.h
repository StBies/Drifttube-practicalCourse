#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

typedef struct
{
	double** all_events;
	uint64_t n_events;
	uint32_t event_size;
}Events;

Events read_events_from_file(const char* filename);
