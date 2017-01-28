#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <sys/timeb.h>
#include "record.h"

//void csv_to_csv(char* filename);

void csv_to_csv(char* filename){
	FILE *fp, *output;
	char current_line[MAX_CHARS_PER_LINE];
	char *line;
	printf("%s\n", filename);
	fp = fopen(filename, "r");
	output = fopen("output.csv", "wb");
	struct timeb t_begin, t_end;
	long time_spent_ms;
	if(fp == NULL){
		perror("Error opening file");
		return;
	}
	//Parse the lines in csv file to an array of array chars
    ftime(&t_begin); 
    int total_size = 0;
	while((line = fgets(current_line, MAX_CHARS_PER_LINE, fp)) != NULL){
		//line [strcspn (line, "\r\n")] = '\0';
		printf("%s\n", line);
		fwrite(line, sizeof(line), 1, output);		
        total_size = total_size + sizeof(line);
	}
    ftime(&t_end);
    time_spent_ms = (long) (1000 *(t_end.time - t_begin.time)
       + (t_end.millitm - t_begin.millitm));
    printf ("Data rate: %.3f MBPS\n", (total_size/(float)time_spent_ms * 1000)/MB); 
	fclose(output);
	fclose (fp);

}

int main(int argc, char *atgv[]){
 	printf("start\n");
 	csv_to_csv(atgv[1]);
 }
