#include "inc/read_events.h"

double** read_events_from_file(const char* filename)
{
	FILE* in_file = fopen(filename,"rb");
	uint64_t n_events = 0;
	uint32_t event_size = 0;
	fread(&n_events,sizeof(uint64_t),1,in_file);
	fread(&event_size,sizeof(uint32_t),1,in_file);

	double** all_events = (double**)malloc(n_events * sizeof(double**));
	for(size_t i = 0; i < n_events; i++)
	{
		all_events[i] = (double*)malloc(event_size * sizeof(double));
		for(size_t j = 0; j < event_size; j++)
		{
			double val = 0.0;
			fread(&val,sizeof(double),1,in_file); //TODO try reading block of event_size doubles
			all_events[i][j] = val;
		}
	}

	return all_events;
}
