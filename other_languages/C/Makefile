CC = gcc
CFLAGS = -std=c99 -fopenmp
LDFLAGS = -fopenmp
INCDIR = -Iinc
SRC			=	$(wildcard src/*.c)
OBJ			=	$(addprefix obj/,$(notdir $(SRC:.c=.o)))
OBJDIR		=	obj
MKDIR		=	mkdir -p

.PHONY :	directories

all: directories prog

prog: $(OBJ)
	$(CC) -o Drifttube $^ $(LDFLAGS)

obj/%.o : src/%.c
	$(CC) $(CFLAGS) $(INCDIR) -c -o $@ $<
	
directories: ${OBJDIR}
	
${OBJDIR}:
	$(MKDIR) ${OBJDIR}
	
clean: directories
	rm -r ${OBJDIR}
	rm *.out