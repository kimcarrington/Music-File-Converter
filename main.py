# import libraries
import defusedxml           # for security purposes
defusedxml.defuse_stdlib()  # automatically implemented by music21
import music21
import os

# handle xml file security
def is_safe_file(file_path: str, max_size_mb: int = 10) -> bool:
    # Check file size
    if os.path.getsize(file_path) > max_size_mb * 1024 * 1024:
        return False
    # Confirm file type
    if not file_path.lower().endswith(('.xml', '.musicxml')):
        return False
    return True

# analyze file for key signature

# transpose function

# convert to midi function

# main function to handle user interactions
def main():
  try:
    # Get input file from user
      input_file = input("Enter path to your MusicXML file: ")
      # Check if file exists
      if not os.path.exists(input_file):
          raise ValueError("Invalid input file path")
      # Check if file is safe
      if not is_safe_file(input_file):
          raise ValueError("Invalid or unsafe input file")
  # ask for file name
  # print analysis results
  # transpose
  # return midi file
