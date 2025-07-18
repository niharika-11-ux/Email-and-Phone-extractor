import re

with open("input.txt", "r", encoding="utf-8") as file:
    text = file.read()

phone_regex = re.compile(r'''(
    (?:\+91[\s-]*|91[\s-]*|0)?    
    [6-9]\d{4}[\s-]?\d{5}          
)''', re.VERBOSE)

email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+            
    @
    [a-zA-Z0-9.-]+                
    \.[a-zA-Z]{2,}                
)''', re.VERBOSE)

matches = []
for match in phone_regex.findall(text):
    digits_only = re.sub(r'\D', '', match)
    if (
        len(digits_only) == 10 and digits_only[0] in '6789'
    ) or (
        len(digits_only) == 11 and digits_only.startswith('0') and digits_only[1] in '6789'
    ) or (
        len(digits_only) == 12 and digits_only.startswith('91') and digits_only[2] in '6789'
    ):
        matches.append(match.strip())

for match in email_regex.findall(text):
    matches.append(match.strip())
matches = sorted(set(matches))

if matches:
    print("Found emails and phone numbers:")
    for item in matches:
        print(item)
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write('\n'.join(matches))
    print("\nSaved to output.txt")
else:
    print("No email or phone number found.")
