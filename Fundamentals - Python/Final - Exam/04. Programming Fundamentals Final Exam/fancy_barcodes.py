import re
number_of_barcodes = int(input())
valid_barcodes = []

for _ in range(number_of_barcodes):
    barcode = input()
    pattern = r"(\@\#+)([A-Z][a-z0-9A-Z]{4,}[A-Z])(\@\#+)"
    match = re.match(pattern, barcode)
    if not match:
        print("Invalid barcode")
    else:
        extract_nums = re.findall("\d", match.group())
        if not extract_nums:
            print(f"Product group: 00")
        else:
            print(f"Product group: {''.join(extract_nums)}")

