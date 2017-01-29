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
	
	if (!(fp_write = fopen (atgv[1] , "r+" ))){
		return -1;
	}

    fseek(fp_write, 0L, SEEK_END);
	int file_size = ftell(fp_write);
	int records_per_file = file_size/sizeof(Record);
	Record *buffer = (Record *) calloc (records_per_file, sizeof (Record)) ;
	fseek(fp_write, 0L, SEEK_SET);
	int result = fread (buffer, sizeof(Record), records_per_file, fp_write);
	if(result != records_per_file){
		return -1;
	}
    while (i < rand_num){
        int r = rand() % (file_size/sizeof(Record));
        printf("%d\n", r);
        buffer[r].uid1 = 11;
        buffer[r].uid2 = 2;
        i++;
    }
    free (buffer);
	fclose (fp_write);
}