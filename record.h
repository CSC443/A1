#define MAX_CHARS_PER_LINE 1024
#define MB 1024 * 1024
typedef struct record {
	int uid1;
	int uid2;
} Record;

void csv_to_record(char* filename, char* block_size);

//void write_record_to_buffer(char *buffer, Record* record, int buffer_pointer);

void write_buffer_to_disk(Record* buffer, int total_records, int filennum, char* orginal_filename);