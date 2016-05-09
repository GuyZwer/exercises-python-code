s = str(raw_input())

if any(c for c in s if c.isalnum()):
    print True
else:
    print False
if any(c for c in s if c.isalpha()):
    print True
else:
    print False
if any(c for c in s if c.isdigit()):
    print True
else:
    print False
if any(c for c in s if c.islower()):
    print True
else:
    print False
if any(c for c in s if c.isupper()):
    print True
else:
    print False


