CC = gcc
CFLAGS = -O3 -Wall 
CFLAGS += -D_LARGEFILE_SOURCE
CFLAGS += -fno-exceptions
CFLAGS += -funroll-loops
CFLAGS += -D_FILE_OFFSET_BITS=64

# Source files
WRITE_BLOCKS_SRC=record.c write_blocks_seq.c 
READ_BLOCKS_SRC= record.c read_blocks_seq.c
WRITE_LINES = write_lines.c
READ_RAM_SRC = record.c read_ram_seq.c
READ_BLOCKS_RAND=read_blocks_rand.c
READ_RAM_RAND= record.c read_ram_rand.c
WRITE_BLOCKS_RAND= record.c write_blocks_rand.c
WRITE_RAM_RAND= record.c write_ram_rand.c
# Binaries
all:write_blocks_seq read_blocks_seq write_lines read_ram_seq read_blocks_rand read_ram_rand write_blocks_rand write_ram_rand

#sequential writing in blocks
write_blocks_seq: $(WRITE_BLOCKS_SRC)
	$(CC) $(CFLAGS) $^ -o write_blocks_seq

read_blocks_seq:${READ_BLOCKS_SRC}
	$(CC) $(CFLAGS) $^ -o read_blocks_seq

write_lines:${WRITE_LINES}
	$(CC) $(CFLAGS) $^ -o write_lines

read_ram_seq:${READ_RAM_SRC}
	$(CC) $(CFLAGS) $^ -o read_ram_seq

read_blocks_rand:${READ_BLOCKS_RAND}
	$(CC) $(CFLAGS) $^ -o read_blocks_rand
read_ram_rand:${READ_RAM_RAND}
	$(CC) $(CFLAGS) $^ -o read_ram_rand

write_blocks_rand:${WRITE_BLOCKS_RAND}
	$(CC) $(CFLAGS) $^ -o write_blocks_rand
write_ram_rand:${WRITE_RAM_RAND}
	$(CC) $(CFLAGS) $^ -o write_ram_rand

clean:  
	rm write_blocks_seq read_blocks_seq write_lines read_ram_seq read_blocks_rand read_ram_rand write_blocks_rand write_ram_rand
