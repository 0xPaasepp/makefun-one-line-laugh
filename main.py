# The One-Line Laugh entry: one funny line, written to /output/entry.txt.
# Standard library only, no network. The bytes are identical on every run.
# The line: a claim of being a functioning adult, undercut in the same
# breath by phoning mum to ask how long chicken lasts in the fridge --
# a real surprise at the end that still makes sense, an everyday truth
# everyone recognises, and nothing there to explain the joke.
import os

LINE = "I told my mum I'm a functioning adult, then rang her to ask how long chicken lasts in the fridge."

OUTPUT_PATH = "/output/entry.txt"

assert 1 <= len(LINE) <= 200, "entry must be 1 to 200 characters"
assert LINE.count(".") == 1 and LINE.endswith("."), "entry must be a single sentence"

os.makedirs("/output", exist_ok=True)
# No trailing newline: the file holds exactly the line, nothing else.
with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
    handle.write(LINE)
