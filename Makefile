CC = gcc
CFLAGS = -O3 -Wall 
CFLAGS += -D_LARGEFILE_SOURCE
CFLAGS += -fno-exceptions
CFLAGS += -funroll-loops
CFLAGS += -D_FILE_OFFSET_BITS=64

# Source files
WRITE_BLOCKS_SRC=record.c write_blocks_seq.c 
READ_BLOCKS_SRC= read_blocks_seq.c
WRITE_LINES = write_lines.c
READ_RAM_SRC = read_ram_seq.c

# Binaries
all:write_blocks_seq read_blocks_seq write_lines read_ram_seq
#sequential writing in blocks
write_blocks_seq: $(WRITE_BLOCKS_SRC)
	$(CC) $(CFLAGS) $^ -o write_blocks_seq

read_blocks_seq:${READ_BLOCKS_SRC}
	$(CC) $(CFLAGS) $^ -o read_blocks_seq

write_lines:${WRITE_LINES}
	$(CC) $(CFLAGS) $^ -o write_lines

read_ram_seq:${READ_RAM_SRC}
	$(CC) $(CFLAGS) $^ -o read_ram_seq

clean:  
	rm write_blocks_seq read_blocks_seq write_lines