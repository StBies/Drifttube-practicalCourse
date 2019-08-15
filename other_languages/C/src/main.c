#include <stdio.h>
#include "read_events.h"
#include "gnuplot_i.h"

int main(void)
{
	Events evts = read_events_from_file("event.npy");

	double x[1024];
	for(int i = 0; i < 1023; i++)
	{
		x[i] = 4 * i;
	}

	for(uint64_t i = 0; i < 1; i++)
	{
		gnuplot_ctrl *h;
		h = gnuplot_init();
		double* arr = evts.all_events[i];
		gnuplot_cmd(h,"set grid");
		gnuplot_cmd(h,"set time");
		gnuplot_setstyle(h,"lines");
		gnuplot_plot_xy(h,&x,arr,1023,"Data");
		sleep(2);
		gnuplot_close(h);
	}



	return 0;
}
