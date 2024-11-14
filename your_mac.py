import os
import sys
import time
import re
import spacy
import difflib
import glob

class TheOracle:
    # ... (other functions)

    def process_natural_language(self, command):
        """Processes natural language commands using spaCy."""
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(command)

        # You can uncomment the following lines to see the tokens and their POS tags
        # for token in doc:
        #    print(token.text, token.pos_)

        # Basic command matching:
        if re.search(r"list files in (.*)", command):
            directory = re.search(r"list files in (.*)", command).group(1).strip()
            return self.list_files(directory)
        elif re.search(r"give me a list of my files in (.*)", command):
            directory = re.search(r"give me a list of my files in (.*)", command).group(1).strip()
            return self.list_files(directory)
        elif re.search(r"show me (.*) in (.*)", command):  # New command
            filename = re.search(r"show me (.*) in (.*)", command).group(1).strip()
            directory = re.search(r"show me (.*) in (.*)", command).group(2).strip()
            try:
                with open(os.path.join(directory, filename), "r") as file:
                    content = file.read()
                    return content
            except FileNotFoundError:
                return "File not found."
        elif re.search(r"rename (.*) to (.*)", command):  # New command
            old_name = re.search(r"rename (.*) to (.*)", command).group(1).strip()
            new_name = re.search(r"rename (.*) to (.*)", command).group(2).strip()
            if os.path.exists(old_name):
                try:
                    os.rename(old_name, new_name)
                    return f"Renamed {old_name} to {new_name}"
                except OSError:
                    return "Rename failed."
            else:
                return "File not found."
        elif re.search(r"list files$", command):
            directory = os.getcwd()  # Get current working directory
            return self.list_files(directory)
        elif re.search(r"open (.*)$", command):  # New condition
            filename = re.search(r"open (.*)$", command).group(1).strip()
            possible_files = difflib.get_close_matches(filename, os.listdir(os.getcwd()), cutoff=0.4,
                                                      n=1)  # Get only the best match
            if possible_files:
                return self.open_file(possible_files[0])
            else:
                return "File not found."
        elif re.search(r"(open|list) recent files", command):  # New condition
            recent_files = glob.glob(os.path.join(os.getcwd(), '*'))
            recent_files = sorted(recent_files, key=os.path.getmtime, reverse=True)
            recent_files = recent_files[:5]  # Show only the top 5 recent files
            if command.startswith("open"):
                if len(recent_files) == 1:
                    return self.open_file(recent_files[0])
                else:
                    return f"Did you mean: {', '.join(recent_files)}?"
            else:
                return ', '.join(recent_files)
        else:
            return "I don't understand."

if __name__ == '__main__':
    pass