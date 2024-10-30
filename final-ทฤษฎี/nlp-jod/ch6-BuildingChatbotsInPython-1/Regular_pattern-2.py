import re
pattern = "if (.*)"
message = "what would happen if bots took over the world"
match = re.search(pattern, message)

match.group(0)

match.group(1)