# CMAKE generated file: DO NOT EDIT!
# Generated by "MinGW Makefiles" Generator, CMake Version 3.19

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Disable VCS-based implicit rules.
% : %,v


# Disable VCS-based implicit rules.
% : RCS/%


# Disable VCS-based implicit rules.
% : RCS/%,v


# Disable VCS-based implicit rules.
% : SCCS/s.%


# Disable VCS-based implicit rules.
% : s.%


.SUFFIXES: .hpux_make_needs_suffix_list


# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

SHELL = cmd.exe

# The CMake executable.
CMAKE_COMMAND = "C:\Program Files\JetBrains\CLion 211.6432.9\bin\cmake\win\bin\cmake.exe"

# The command to remove a file.
RM = "C:\Program Files\JetBrains\CLion 211.6432.9\bin\cmake\win\bin\cmake.exe" -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = "C:\0's and 1's\OneDrive - CSULB\Courses\Spring 2021\CECS 328\robotDelivery"

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = "C:\0's and 1's\OneDrive - CSULB\Courses\Spring 2021\CECS 328\robotDelivery\cmake-build-debug"

# Include any dependencies generated for this target.
include CMakeFiles/robotDelivery.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/robotDelivery.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/robotDelivery.dir/flags.make

CMakeFiles/robotDelivery.dir/Main.cpp.obj: CMakeFiles/robotDelivery.dir/flags.make
CMakeFiles/robotDelivery.dir/Main.cpp.obj: ../Main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="C:\0's and 1's\OneDrive - CSULB\Courses\Spring 2021\CECS 328\robotDelivery\cmake-build-debug\CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/robotDelivery.dir/Main.cpp.obj"
	C:\PROGRA~1\MINGW-~1\X86_64~1.0-P\mingw64\bin\G__~1.EXE $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles\robotDelivery.dir\Main.cpp.obj -c "C:\0's and 1's\OneDrive - CSULB\Courses\Spring 2021\CECS 328\robotDelivery\Main.cpp"

CMakeFiles/robotDelivery.dir/Main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/robotDelivery.dir/Main.cpp.i"
	C:\PROGRA~1\MINGW-~1\X86_64~1.0-P\mingw64\bin\G__~1.EXE $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E "C:\0's and 1's\OneDrive - CSULB\Courses\Spring 2021\CECS 328\robotDelivery\Main.cpp" > CMakeFiles\robotDelivery.dir\Main.cpp.i

CMakeFiles/robotDelivery.dir/Main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/robotDelivery.dir/Main.cpp.s"
	C:\PROGRA~1\MINGW-~1\X86_64~1.0-P\mingw64\bin\G__~1.EXE $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S "C:\0's and 1's\OneDrive - CSULB\Courses\Spring 2021\CECS 328\robotDelivery\Main.cpp" -o CMakeFiles\robotDelivery.dir\Main.cpp.s

# Object files for target robotDelivery
robotDelivery_OBJECTS = \
"CMakeFiles/robotDelivery.dir/Main.cpp.obj"

# External object files for target robotDelivery
robotDelivery_EXTERNAL_OBJECTS =

robotDelivery.exe: CMakeFiles/robotDelivery.dir/Main.cpp.obj
robotDelivery.exe: CMakeFiles/robotDelivery.dir/build.make
robotDelivery.exe: CMakeFiles/robotDelivery.dir/linklibs.rsp
robotDelivery.exe: CMakeFiles/robotDelivery.dir/objects1.rsp
robotDelivery.exe: CMakeFiles/robotDelivery.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir="C:\0's and 1's\OneDrive - CSULB\Courses\Spring 2021\CECS 328\robotDelivery\cmake-build-debug\CMakeFiles" --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable robotDelivery.exe"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\robotDelivery.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/robotDelivery.dir/build: robotDelivery.exe

.PHONY : CMakeFiles/robotDelivery.dir/build

CMakeFiles/robotDelivery.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles\robotDelivery.dir\cmake_clean.cmake
.PHONY : CMakeFiles/robotDelivery.dir/clean

CMakeFiles/robotDelivery.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" "C:\0's and 1's\OneDrive - CSULB\Courses\Spring 2021\CECS 328\robotDelivery" "C:\0's and 1's\OneDrive - CSULB\Courses\Spring 2021\CECS 328\robotDelivery" "C:\0's and 1's\OneDrive - CSULB\Courses\Spring 2021\CECS 328\robotDelivery\cmake-build-debug" "C:\0's and 1's\OneDrive - CSULB\Courses\Spring 2021\CECS 328\robotDelivery\cmake-build-debug" "C:\0's and 1's\OneDrive - CSULB\Courses\Spring 2021\CECS 328\robotDelivery\cmake-build-debug\CMakeFiles\robotDelivery.dir\DependInfo.cmake" --color=$(COLOR)
.PHONY : CMakeFiles/robotDelivery.dir/depend

