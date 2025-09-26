from collections import defaultdict

def ip_parse(line):

    tokens = line.split()
    if "from" in tokens:
        idx = tokens.index("from")
        if idx + 1 < len(tokens):
            return tokens[idx + 1]
    return None

counts = defaultdict(int)       #create a dictionary to keep track of IPs

with open("sample_auth_small.log") as f:
    for line in f:
        if "Failed password" in line or "Invalid user" in line:
            # extract ip
            ip = ip_parse(line)
            if ip:
                counts[ip] += 1
print(counts)