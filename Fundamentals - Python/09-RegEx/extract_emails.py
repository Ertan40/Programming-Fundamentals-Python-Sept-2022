import re

sentence = input()
pattern = r"\s(([a-z0-9]+[\.\-\_a-z0-9]*)@[a-z\-]+(\.[a-z]+)+)\b"

e_mails = re.findall(pattern, sentence)
for mails in e_mails:
    print(mails[0])