#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/timeb.h>
#include "record.h"

int main(int argc, char *atgv[]){
	
	FILE *fp_read;
	if (!(fp_read = fopen (atgv[1] , "rb" ))){
		return -1;
	}

	fseek(fp_read, 0L, SEEK_END);
	int file_size = ftell(fp_read);
	fseek(fp_read, 0L, SEEK_SET);
	printf("%d\n", file_size);
	int records_per_file = file_size/sizeof(Record);
	/* allocate buffer for 1 block */
	Record * buffer = (Record *) calloc (records_per_file, sizeof (Record)) ;
	
	
	
	/* read records into buffer */
	
	int result = fread (buffer, sizeof(Record), records_per_file, fp_read);
	struct timeb t_begin, t_end;
    long time_spent_ms;
    ftime(&t_begin);
	if (result!=records_per_file){
		return -1;
	}
	int pointer = 0;
	int current_max_id = -1;
	int current_max_followers = 0;
	int previous_max_id = -1;
	int previous_max_followers = -1;
	int id_count = 0;
	while(pointer < records_per_file){
		if(current_max_id == -1){

			current_max_id = buffer[pointer].uid1;
			current_max_followers = 1;
			id_count++;
		}else if(current_max_id == buffer[pointer].uid1){
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
		pointer++;
		
	}
	if(previous_max_followers < current_max_followers && previous_max_id != current_max_id){
		previous_max_followers = current_max_followers;
		previous_max_id = current_max_id;
	}
    ftime(&t_end);
    time_spent_ms = (long) (1000 *(t_end.time - t_begin.time)
       + (t_end.millitm - t_begin.millitm));
    printf ("Data rate: %.3f MBPS\n", ((pointer*sizeof(Record))/(float)time_spent_ms * 1000)/(1024*1024));
	printf ("total records: %d\n", (pointer));
	printf("uid %d with max followers %d, total number of uid %d, avg %.3f\n", previous_max_id, previous_max_followers, id_count, pointer/(float)id_count);
	write_result_to_file("read_ram_seq.txt", 0, ((pointer*sizeof(Record))/(float)time_spent_ms * 1000)/(1024*1024));
	fclose (fp_read);
	free (buffer);
}

