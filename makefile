.PHONY: all clean

# Define the source and test directories
SRC_DIR = src
TEST_DIR = tests

# List of Python files in the source directory
SRC_FILES = $(wildcard $(SRC_DIR)/*.py)

# List of test files in the test directory
TEST_FILES = $(wildcard $(TEST_DIR)/*.py)

# Define the output directory
OUT_DIR = build

# Define the target files by replacing the source directory prefix with the output directory
TARGET_FILES = $(patsubst $(SRC_DIR)/%.py,$(OUT_DIR)/%.py,$(SRC_FILES)) \
			  $(patsubst $(TEST_DIR)/%.py,$(OUT_DIR)/%.py,$(TEST_FILES))

# Default target
all: $(TARGET_FILES)

# Rule to create output directory if it doesn't exist
$(OUT_DIR):
	mkdir -p $(OUT_DIR)

# Rule to copy source files to the output directory
$(OUT_DIR)/$(SRC_DIR)/%.py: $(SRC_DIR)/%.py | $(OUT_DIR)
	cp $< $@

# Rule to copy test files to the output directory
$(OUT_DIR)/$(TEST_DIR)/%.py: $(TEST_DIR)/%.py | $(OUT_DIR)
	cp $< $@

# Clean the output directory
clean:
	rm -rf $(OUT_DIR)

