#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/timeb.h>
#include "record.h"

int main(int argc, char *atgv[])
{
	printf("read blocks random\n");
	int block_size = atoi(atgv[2]);
	int rand_num = atoi(atgv[3]);
	int i = 0;
	int records_per_block = block_size/sizeof(Record);

	FILE *fp_read;
	/* allocate buffer for 1 block */
	Record * buffer = (Record *) calloc (records_per_block, sizeof (Record)) ;
	
	if (!(fp_read = fopen (atgv[1] , "rb" ))){
		return -1;
	}
	fseek(fp_read, 0L, SEEK_END);
	int file_size = ftell(fp_read);
	fseek(fp_read, 0L, SEEK_SET);

	int avg = 0;
	int uid_with_max_f = 0;
	int max_f_count = 0;
	struct timeb t_begin, t_end;
    long time_spent_ms;
    ftime(&t_begin);
    printf("%d\n",file_size);
    int record_count = 0;
    while (i < rand_num){
        int r = rand() % (file_size/sizeof(Record));
        fseek(fp_read, r*sizeof(Record), SEEK_SET);
        int result = fread (buffer, sizeof(Record), records_per_block, fp_read);
        records_per_block = block_size/sizeof(Record);
		if (result!=records_per_block){
			records_per_block = result;
		}

		int pointer = 0;
		int current_max_id = -1;
		int current_max_followers = 0;
		int previous_max_id = -1;
		int previous_max_followers = -1;
		int id_count = 0;
		
		while(pointer < records_per_block){
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
			id_count++;
		}
		
        avg+= records_per_block/(float)id_count;
        if(previous_max_followers > max_f_count){
        	max_f_count = previous_max_followers;
        	uid_with_max_f = previous_max_id;
        }
        
        i++;
        record_count+=records_per_block;

    }
    printf("%d\n", record_count);
    printf("uid with max followers %d %d, avg %.3f\n", uid_with_max_f, max_f_count, avg/(float)rand_num);
    ftime(&t_end);
    time_spent_ms = (long) (1000 *(t_end.time - t_begin.time)
       + (t_end.millitm - t_begin.millitm));
    printf ("Data rate: %.3f MBPS\n", ((record_count*sizeof(Record))/(float)time_spent_ms * 1000)/(1024*1024));
	printf ("total records: %d\n", (record_count));
	write_result_to_file("read_block_rand.txt", block_size, ((record_count*sizeof(Record))/(float)time_spent_ms * 1000)/(1024*1024));

    free (buffer);
	fclose (fp_read);
	return 0;
}
