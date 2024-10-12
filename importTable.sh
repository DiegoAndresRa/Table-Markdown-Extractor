#!/bin/bash

web_page=$1
table_file=$2

html_file='input.html'
# Get source html code
curl -o $html_file $web_page &>/dev/null

# Get line from the begining and end of the table
limits=($(grep -n -E '<\/?table[^>]*>' $html_file | head -n 2 | awk -F: '{print $1}'))

bg=${limits[0]}
end=${limits[1]}

# Get table's code
sed -n "$bg,$end p" $html_file > $table_file

if [ $? -eq 0 ];then echo "Table's code in $table_file";fi

rm input.html
