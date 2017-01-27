CC = gcc
CFLAGS = -O3 -Wall 
CFLAGS += -D_LARGEFILE_SOURCE
CFLAGS += -fno-exceptions
CFLAGS += -funroll-loops
CFLAGS += -D_FILE_OFFSET_BITS=64

# Source files
WRITE_BLOCKS_SRC=record.c write_blocks_seq.c write_lines.c 
READ_BLOCKS_SRC= read_blocks_seq.c
# Binaries
all:write_blocks_seq read_blocks_seq
#sequential writing in blocks
write_blocks_seq: $(WRITE_BLOCKS_SRC)
	$(CC) $(CFLAGS) $^ -o write_blocks_seq

read_blocks_seq:${READ_BLOCKS_SRC}
	$(CC) $(CFLAGS) $^ -o read_blocks_seq
	
clean:  
	rm write_blocks_seq read_blocks_seq