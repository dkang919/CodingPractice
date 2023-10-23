## Method 1

# Read from the file file.txt and output all valid phone numbers to stdout.

grep -e "^[0-9]\{3\}\-[0-9]\{3\}\-[0-9]\{4\}$" -e "^([0-9]\{3\}) [0-9]\{3\}\-[0-9]\{4\}$" file.txt



## Method 2

# Read from the file file.txt and output all valid phone numbers to stdout.
p=\([0-9][0-9][0-9]\)\ [0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]
p2=[0-9][0-9][0-9]-[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]

while read -r line; 
do
  case "$line" in
    $p)
    echo "$line"
    ;;
    $p2)
    echo "$line"
    ;;
  esac
done < file.txt