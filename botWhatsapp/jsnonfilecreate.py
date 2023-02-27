import json
import os

# Replace with the path to your input directory
input_dir = "C:/Users/ferna/Desktop/botWhatsapp/arquivoswhatsappB"

# Replace with the path to your output JSONL file
output_file = "whatsapp_chat.jsonl"

# Define the JSONL format for each message
def format_message(name, text):
    message = {"text": text, "meta": {"name": name}}
    return json.dumps(message)

# Open the output file for writing
with open(output_file, "w", encoding="utf-8") as f_out:
    # Loop through each file in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith(".txt"):
            # Open the input file and loop through each line
            with open(os.path.join(input_dir, filename), "r", encoding="utf-8") as f_in:
                for line in f_in:
                    # Split the line into name and text
                    parts = line.strip().split(": ", maxsplit=1)
                    if len(parts) == 2:
                        name, text = parts
                        # Format the message and write it to the output file
                        message = format_message(name, text)
                        f_out.write(message + "\n")
