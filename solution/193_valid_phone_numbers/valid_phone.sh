# Read from the file file.txt and output all valid phone numbers to stdout.
# (xxx) xxx-xxxx or xxx-xxx-xxxx. 
set -e

grep -P '^(\d{3}-|\(\d{3}\) )\d{3}-\d{4}$' file.txt
