import regex as re

text = "four95qvkvveight5"

fd_regex = re.compile(r".*?(one|two|three|four|five|six|seven|eight|nine|zero|\d)[a-z 0-9]*", re.IGNORECASE)
digits = fd_regex.match(text)

for group in digits.groups():
    print(group)
    group.replace(['one','two','three','four'],['1','2','3','4'])