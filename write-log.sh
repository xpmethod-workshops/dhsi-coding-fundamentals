#!/bin/bash

src=/home/denten/gDrive/papers/projects/workbench/plain-text/
path=/home/denten/gDrive/papers/projects/workbench/plain-text/code/progress

old_words=$(tail -1 $path/log.txt | cut -f 1 -d ' ')
stamp="$(date --iso-8601)"

# use < to display counts only, otherwise wc includes the file name
# count all .md files in the root dir one level deep
for f in $(find $src -maxdepth 1 -name '*.md'); do wc -w < $f >> $path/tmp.txt; done

# add numbers in the tmp file and append to words.csv
new_words="$(awk '{ sum += $1 } END { print sum }' $path/tmp.txt)"

# calculate number of words written
total=$(expr $new_words - $old_words)

# happy message
echo "You wrote "$total" words since last time for a total of "$new_words".
Well done, sir."

# write to log
if [ $total != 0 ]
    then
        echo $new_words $total $stamp >> $path/log.txt
fi

# clean up
rm -f $path/tmp.txt
