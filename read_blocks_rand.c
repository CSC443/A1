#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/timeb.h>
#include "record.h"

int main(int argc, char *atgv[])
{
	printf("read blocks random");
	int block_size = atoi(atgv[2]);
	int rand_num = atoi(atgv[3]);
	int i = 0;
	int records_per_block = block_size/sizeof(Record);

	FILE *fp_read;
	/* allocate buffer for 1 block */
	//Record * buffer = (Record *) calloc (records_per_block, sizeof (Record)) ;
	
	if (!(fp_read = fopen (atgv[1] , "rb" ))){
		return -1;
	}
	fseek(fp_read, 0L, SEEK_END);
	int file_size = ftell(fp_read);
	fclose (fp_read);


    if (!(fp_read = fopen (atgv[1] , "rb" ))){
		return -1;
	}

    printf("%d\n",file_size);
    while (i < rand_num){
          int r = rand() % (file_size/block_size);
          Record * buffer = (Record *) calloc (records_per_block, sizeof (Record)) ;
          fseek(fp_read, r*block_size, SEEK_SET);   // seek to the beginning of the file
          int result = fread (buffer, sizeof(Record), records_per_block, fp_read);

		if (result!=records_per_block){
			return -1;
		}

		int pointer = 0;
		int current_max_id = -1;
		int current_max_followers = 0;
		int previous_max_id = -1;
		int previous_max_followers = -1;
		int id_count = 0;
		int record_count = 0;
		while(pointer < records_per_block){
			record_count++;
			printf("uid1 %d\n", buffer[pointer].uid1);
			if(current_max_id == -1){
				current_max_id = buffer[pointer].uid1;
				current_max_followers = 1;
				previous_max_followers = current_max_followers;
				previous_max_id = current_max_id;
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
        printf("uid with max followers %d, total number of uid %d, avg %.3f\n", previous_max_followers, id_count, record_count/(float)id_count);
        free (buffer);
        i++;

    }

	fclose (fp_read);
}