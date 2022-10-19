COMPILER = g++
COMPILER_FLAGS = -c -g -std=c++17 -m32
BUILD_FLAGS = -m32 -fno-stack-protector -z execstack -no-pie

logServer: logServer.cpp
	$(COMPILER) $(COMPILER_FLAGS) logServer.cpp 
	$(COMPILER) $(BUILD_FLAGS) logServer.o -o logServer

clean:
	rm -f *.o

