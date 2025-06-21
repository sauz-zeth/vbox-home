TARGET = main
SRC = main.cpp vec.hpp storage.hpp number.hpp point.hpp

CC = g++
CXXFLAGS = -std=c++17 -g3
LDLIBS =

STARS = ***********************
$(info )
$(info [32;1m$(STARS) Make $(STARS)[0m)
$(info )

.PHONY: run

run: $(TARGET) 
	./$<

debug: $(TARGET)
	gdb -q $<

$(TARGET): $(SRC) Makefile
	$(CC) $(CXXFLAGS) $@.cpp $(LDLIBS) -o $@
