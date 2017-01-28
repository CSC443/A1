#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/timeb.h>
#include "record.h"

int main(int argc, char *atgv[]){
	int block_size = atoi(atgv[2]);
	int records_per_block = block_size/sizeof(Record);
	FILE *fp_read;
	/* allocate buffer for 1 block */
	Record * buffer = (Record *) calloc (records_per_block, sizeof (Record)) ;
	
	if (!(fp_read = fopen (atgv[1] , "rb" ))){
		return -1;
	}
	
	/* read records into buffer */
	struct timeb t_begin, t_end;
    long time_spent_ms;
    ftime(&t_begin);
	int result = fread (buffer, sizeof(Record), records_per_block, fp_read);

	if (result!=records_per_block){
		return -1;
	}
	int pointer = 0;
	int current_max_id = buffer[pointer].uid1;
	int current_max_followers = 1;
	int previous_max_id = -1;
	int previous_max_followers = -1;
	int id_count = 0;
	while(pointer < records_per_block){

		pointer++;
		printf("uid1 %d\n", buffer[pointer].uid1);
		if(current_max_id == buffer[pointer].uid1){
			current_max_followers++;
		}else{
			if(previous_max_followers < current_max_followers && previous_max_id != current_max_id){
				previous_max_followers = current_max_followers;
				previous_max_id = current_max_id;
			}
			current_max_id = buffer[pointer].uid1;
			current_max_followers = 1;
			id_count++;
		}
		
		
	}
    ftime(&t_end);
    time_spent_ms = (long) (1000 *(t_end.time - t_begin.time)
       + (t_end.millitm - t_begin.millitm));
    printf ("Data rate: %.3f MBPS\n", ((pointer*sizeof(Record))/(float)time_spent_ms * 1000)/(1024*1024));
	printf ("total records: %d\n", (pointer));
	printf("%d, %d\n", previous_max_followers, id_count);
	
	fclose (fp_read);
	free (buffer);
}

