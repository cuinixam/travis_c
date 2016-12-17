CC=gcc
CFLAGS=-I.
OUTDIR=./out

OBJ = src/main.o
YACT_OBJ = tools/yact/yact.o

LIGHTS_TEST_OBJ = $(YACT_OBJ) src/lights/lights.o src/lights/lights.test.o

# Remove directory options:
# -f, --force           ignore nonexistent files and arguments, never prompt
# -r, -R, --recursive   remove directories and their contents recursively
RM=rm -f -r
# Make directory options:
# -p, --parents     no error if existing, make parent directories as needed
MK=mkdir -p

%.o: %.c
	@echo "Compiling" $<
	# Mirror the source folder structure in the output folder
	@$(MK) $(OUTDIR)/$(@D)
	$(CC) -c -o $(OUTDIR)/$@ $< $(CFLAGS)

build: main.exe
test : lights.test.exe

main.exe: dirs $(OBJ)
	@echo "Linking " $@
	$(CC) -o $(OUTDIR)/$@ $(OUTDIR)/$(OBJ) $(CFLAGS)

lights.test.exe: dirs $(LIGHTS_TEST_OBJ)
	@echo "Linking " $@
	$(CC) -o $(OUTDIR)/$@ $(addprefix $(OUTDIR)/,$(LIGHTS_TEST_OBJ))  $(CFLAGS)

clean:
	$(RM) $(OUTDIR)/*

dirs:
	@echo "Create the output directory"
	$(MK) $(OUTDIR)
