import regex as re

text = "four95qvkvveight5"

fd_regex = re.compile(r".*?(one|two|three|four|five|six|seven|eight|nine|zero|\d)[a-z 0-9]*", re.IGNORECASE)
digits = fd_regex.match(text)

for group in digits.groups():
    print(group)

text = "Hello World! How are you?"
nongreedy = re.compile(r"(.*?)")
matches = nongreedy.match(text)

for group in matches.groups():
    print(group)