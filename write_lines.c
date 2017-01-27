#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include "record.h"

//void csv_to_csv(char* filename);

void csv_to_csv(char* filename){
	FILE *fp, *output;
	char current_line[MAX_CHARS_PER_LINE];
	char *line;
	printf("%s\n", filename);
	fp = fopen(filename, "r");
	output = fopen("output.csv", "wb");
	if(fp == NULL){
		perror("Error opening file");
		return;
	}
	//Parse the lines in csv file to an array of array chars

	while((line = fgets(current_line, MAX_CHARS_PER_LINE, fp)) != NULL){
		//line [strcspn (line, "\r\n")] = '\0';
		printf("%s\n", line);
		fwrite(line, sizeof(line), 1, output);		

	}

	fclose(output);
	fclose (fp);

}

int main(int argc, char *atgv[]){
 	printf("start\n");
 	csv_to_csv(atgv[1]);
 }
