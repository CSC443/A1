#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/timeb.h>
#include "record.h"

int main(int argc, char *atgv[])
{
	printf("write blocks random\n");
	int rand_num = atoi(atgv[2]);
	printf("ra. %d\n", rand_num);
	int i = 0;

	FILE *fp_write;
	struct timeb t_begin, t_end;
    long time_spent_ms;
    ftime(&t_begin);
	if (!(fp_write = fopen (atgv[1] , "rb+" ))){
		return -1;
	}

    fseek(fp_write, 0L, SEEK_END);
	int file_size = ftell(fp_write);
	Record *buffer = (Record *) calloc (1, sizeof (Record));
	fseek(fp_write, 0L, SEEK_SET);
    while (i < rand_num){
        int r = rand() % (file_size/sizeof(Record));
        //printf("%d\n", r);
        fseek(fp_write, r*sizeof(Record), SEEK_SET);
        buffer[0].uid1 = 11;
        buffer[0].uid2 = 2;
        fwrite(buffer, sizeof(Record), 1, fp_write);
        fflush (fp_write);
        i++;
    }
    ftime(&t_end);
    time_spent_ms = (long) (1000 *(t_end.time - t_begin.time)
       + (t_end.millitm - t_begin.millitm));
    printf ("Data rate: %.3f MBPS\n", ((rand_num*sizeof(Record))/(float)time_spent_ms * 1000)/(1024*1024));
	printf ("total records changed: %d\n", (rand_num));
	write_result_to_file("write_block_rand.txt", 0, ((rand_num*sizeof(Record))/(float)time_spent_ms * 1000)/(1024*1024));
    free (buffer);
	fclose (fp_write);
}