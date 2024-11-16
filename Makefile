# Nom de l'exécutable final
TARGET = program

# Compiler et options
CC = gcc
CFLAGS = -Wall -Wextra -O2

# Fichiers sources et objets
SRCS = $(wildcard *.c)
OBJS = $(SRCS:.c=.o)

# Règle par défaut (compilation de l'exécutable)
all: $(TARGET)

# Lien des fichiers objets pour créer l'exécutable
$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJS)

# Compilation de chaque fichier source en fichier objet
%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

# Nettoyage des fichiers objets et de l'exécutable
clean:
	rm -f $(OBJS) $(TARGET)

# Commande pour recompiler tout
rebuild: clean all
