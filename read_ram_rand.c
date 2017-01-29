#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/timeb.h>
#include "record.h"



int main(int argc, char *atgv[]){
 	FILE *fp_read;
 	int block_size = atoi(atgv[2]);
	if (!(fp_read = fopen (atgv[1] , "rb" ))){
		return -1;
	}

	fseek(fp_read, 0L, SEEK_END);
	int file_size = ftell(fp_read);
	fclose (fp_read);
 
	if (!(fp_read = fopen (atgv[1] , "rb" ))){
		return -1;
	}
	//printf("%d\n", file_size);
    int total_records = file_size/sizeof(Record);
    int records_per_block = block_size/sizeof(Record);
    int records_need_to_read = 0;
    
    
    Record * buffer = (Record *) calloc (total_records, sizeof (Record)) ;

    struct timeb t_begin, t_end;
    long time_spent_ms;
    ftime(&t_begin);
    
	int result = fread (buffer, sizeof(Record), total_records, fp_read);
    
    if (result!=total_records){
		return -1;
	}
    
	int r = rand() % (file_size/sizeof(Record));
    
    if ((total_records - r)>=records_per_block ){
          records_need_to_read = records_per_block ;

    } else {
          records_need_to_read = total_records - r ;

    }

	printf("random postion is %d\n", r);
	int pointer = 0;
	int current_max_id = -1;
	int current_max_followers = 0;
	int previous_max_id = -1;
	int previous_max_followers = -1;
	int id_count = 0;
    printf("%d\n" , records_need_to_read);
	while(pointer < records_need_to_read){
		printf("uid1 %d\n", buffer[(pointer+r)].uid1);
		if(current_max_id == -1){

			current_max_id = buffer[(pointer+r)].uid1;
			current_max_followers = 1;
			// previous_max_followers = current_max_followers;
			// previous_max_id = current_max_id;
			id_count++;
		}else if(current_max_id == buffer[(pointer+r)].uid1){
			current_max_followers++;
		}else{
			if(previous_max_followers < current_max_followers && previous_max_id != current_max_id){
				previous_max_followers = current_max_followers;
				previous_max_id = current_max_id;
			}
			current_max_id = buffer[(pointer+r)].uid1;
			current_max_followers = 1;
			id_count++;
		}
		pointer++;
		
	}

	if(previous_max_id == -1){
		previous_max_followers = current_max_followers;
		previous_max_id = current_max_id;
	}
    ftime(&t_end);
    time_spent_ms = (long) (1000 *(t_end.time - t_begin.time)
       + (t_end.millitm - t_begin.millitm));
    printf ("Data rate: %.3f MBPS\n", ((pointer*sizeof(Record))/(float)time_spent_ms * 1000)/(1024*1024));
	printf ("total records: %d\n", (pointer));
	printf("uid with max followers %d, total number of uid %d, avg %.3f\n", previous_max_followers, id_count, pointer/(float)id_count);
	
	fclose (fp_read);
	free (buffer);
}
