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


# transpose function
def modify_score(score: music21.stream.Score, transpose: int = 0) -> music21.stream.Score:
    # transpose score
    score = score.transpose(transpose)
    return score

# convert to midi function
def convert_to_midi(input_file, transpose) -> tuple[str, dict]:
    """Convert MusicXML to MIDI with analysis and modifications."""
    try:
        if not is_safe_file(input_file):
            raise ValueError("Invalid or unsafe input file")
        
        # Parse score
        score = music21.converter.parse(input_file)

        # Extract and strip input file name
        output_file = os.path.splitext(os.path.basename(input_file))[0]
        output_file = f"{output_file}.mid"
        
        # Apply modifications
        if transpose != 0:
            score = modify_score(score, transpose)
        
        # Write modified score to MIDI
        score.write('midi', fp=output_file)
        
        return output_file 
        
    except Exception as e:
        raise Exception(f"Conversion failed: {str(e)}")

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

       # score = music21.converter.parse(input_file)    

        # Transposition
        transpose = 0
        transpose_response = input("\nWould you like to transpose the piece? (yes/no): ").lower()
        if transpose_response == 'yes':
            transpose = int(input("Enter semitones to transpose (positive = up, negative = down): "))

        # Convert and save the file
        output_midi = convert_to_midi(
            input_file,
            transpose=transpose
        )
        
        print(f"\nSuccessfully converted to: {output_midi}")
        
    except Exception as e:
        print(f"Error: {e}")

main()
