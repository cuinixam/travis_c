CC=gcc
CFLAGS=-I.
OUTDIR=./out

OBJ = main.o

# Remove directory options:
#  -f, --force           ignore nonexistent files and arguments, never prompt
RM=rm -f
# Make directory options:
# -p, --parents     no error if existing, make parent directories as needed
MK=mkdir -p

%.o: %.c
	@echo "Compiling" $<
	$(CC) -c -o $(OUTDIR)/$@ $< $(CFLAGS)

main.exe: dirs $(OBJ)
	@echo "Linking " $@
	$(CC) -o $(OUTDIR)/$@ $(OUTDIR)/$(OBJ) $(CFLAGS)

clean:
	$(RM) $(OUTDIR)/*

dirs:
	@echo "Create the output directory"
	$(MK) $(OUTDIR)
