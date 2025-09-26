LOGFILE = "sample_auth_small.log"

def simple_parser(line):

    tokens = line.split()
    if "from" in tokens:
        idx = tokens.index("from")
        if idx + 1 < len(tokens):
            return tokens[idx + 1]
    return None



unique_ips = set()
line_count = 0

with open("sample_auth_small.log", "r") as file:
    for line in file:
        line_count += 1
        parts = line.split()
        if "from" in parts:
            from_index = parts.index("from")
            if from_index + 1 < len(parts):
                ip = parts[from_index + 1]
                unique_ips.add(ip)

# Print results
print("Total lines read:", line_count)
print("Number of unique IPs:", len(unique_ips))
print("First 10 unique IPs (sorted):")
for ip in sorted(unique_ips)[:10]:
    print(ip)