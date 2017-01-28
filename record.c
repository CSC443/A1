#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/timeb.h>
#include "record.h"

void csv_to_record(char* filename, char* block_size){
	struct timeb t_begin, t_end;
	long time_spent_ms;
	FILE *fp, *fp_write;
	char current_line[MAX_CHARS_PER_LINE];
	char *line;
	int records_per_block = atoi(block_size) / sizeof(Record);
	Record *buffer = (Record *) calloc (records_per_block, sizeof (Record));
	int buffer_pointer = 0;
	printf("%s\n", filename);

	fp = fopen(filename, "r");
	if(fp == NULL){
		perror("Error opening file");
		return;
	}

	fp_write = fopen("data.dat", "wb");
	if(fp_write == NULL){
		perror("Error opening file");
		return;
	}

	printf("%lu\n", sizeof(Record));
	
	int file = 0;
	int i = 0;
	//Parse the lines in csv file to an array of array chars
	int total_records = 0;
    ftime(&t_begin); 
	while((line = fgets(current_line, MAX_CHARS_PER_LINE, fp)) != NULL){
		line [strcspn (line, "\r\n")] = '\0';
		printf("%s\n", line);
		char *attr = strtok(line, ",");
		int j = 0;
		while(attr){

			printf("current attr %s\n", attr);
			if(j == 0){
				buffer[i].uid1 = atoi(attr);
			}else{
				buffer[i].uid2 = atoi(attr);
			}		
			attr = strtok(NULL, ",");
			j++;
		}
		i++;
		total_records++;
		if(i == records_per_block){
			write_buffer_to_disk(buffer, records_per_block, fp_write);
			file++;
			i = 0;

		}
		

	}
	if(file == 0){
		write_buffer_to_disk(buffer, total_records, fp_write);
	}
    ftime(&t_end); 

	time_spent_ms = (long) (1000 *(t_end.time - t_begin.time)
     + (t_end.millitm - t_begin.millitm));

	printf ("Data rate: %.3f MBPS\n", ((total_records*sizeof(Record))/(float)time_spent_ms * 1000)/MB);
	printf("total records: %d\n",(total_records));	

	
	free(buffer);
	fclose (fp);
	fclose (fp_write);

}


void write_buffer_to_disk(Record* buffer, int total_records, FILE *fp){

	if(fp){
		fwrite(buffer, sizeof(Record), total_records, fp);
		fflush (fp);
	}else{
		return;
	}

}

