---
---

```
# Find the Whale
grep "whale" moby.txt
```

To find the whale, use the `grep` command. The command itself is a shortening
of the commands "**G**lobally search a **Re**gular expression and
**P**rint"---a regular expression is a way of searching for patterns in a text.
The basic syntax of grep is: `grep [search string] [file to search]`. By
default it outputs any lines on which the search string appears. For more
detail and options, type `man grep` into the terminal.

```
# substitute whale for chicken globally
cat moby.txt | sed 's/whale/chicken/g' > chicken.txt
```

Now that we've found the whale, we can do whatever we want with it. Let's see
what happens if the white whale is a white chicken using `cat`, `sed`, pipes,
and redirections. The `cat` command con**cat**enates the text data from `moby.txt`, turning
it into a stream of data we can manipulate. 

Next, `sed`, the **s**erial **ed**itor, replaces the search string with
something else. The syntax is as follows: `s` tells sed to substitute
something; next comes the search string; after that, the replacement string;
and after that, the scope, which is `g` for global.

Finally, piping `|` passes the output of data from one
command to the next one, creating a stream of data transformations. Redirection
`>` stores the final output in the file named after the redirection---here,
`chicken.txt`.

```
# see what happened to the whales
grep "chicken" chicken.txt
```
You are already familiar with `grep`. Take a look at the output to see what
*Moby Dick* looks like with a chicken.

```
# remove punctuation.
cat moby.txt | tr -d "[:punct:]" > moby-nopunct.txt
```
Eventually, we'll want to create a frequency list for the words in *Moby Dick*.
First, we have to throw out punctuation so that 'whale' is not counted
differently from 'whale!' 

You know `cat`, piping, and redirection, but you don't know `tr` yet, or
**tr**anslate. Type `man tr` to see the full range of what `tr` can do, but
with the `-d` option specified it will delete every occurrence of a search
string from a text. In this case, instead of a specific search string, we will
search for a whole class of characters. We specify the punctuation character
class with `[:punct:]`. (Note: if this doesn't work on your machine, try
`[[:punct:]]`.)

Note that we are saving each transformation in its own, descriptively named
file. It is a good practice not to overwrite your original file to avoid losing
data.

```
# check if it worked
tail moby-nopunct.txt
```
Confirm that it had the desired result by returning the `tail` of the new file.

```
# translate all upper case into lower
cat moby-nopunct.txt | tr '[:upper:]' '[:lower:]' > moby-clean.txt
tail moby-clean.txt
```

We don't want any upper case characters, but we don't want to delete them
either. We'll use `tr` and character classes again to replace every upper case
character with its lower case equivalent. This time, we won't use the `-d`
flag.

```
# sort by word frequency
cat moby-clean.txt | sed 's/[[:space:]]/\'$'\n/g' | sort | uniq -c | sort -gr -k1 > word-count.txt
head word-count.txt
```

This might look complex, but it is made up of many steps you already know. The
`sed` command in this case will replace spaces with line breaks. The syntax
here is a little messy, but `\'$'\n` uses the newline character as a
replacement string. 

The `sort` and `uniq -c` commands go together. The second, `uniq`, eliminates
duplicate lines, but only contiguous duplicate lines. In other words, if these
letters were lines, it would reduce `abbbaab` to `abab`. We have to put all the
duplicates in a row so they are all eliminated, and therefore we use `sort`
before using `uniq`. The `-c` option includes a count of the duplicate string
after removing the extras.

After we have a count for each word, we want to sort again, but now based on
the numeric order of the count rather than the alphabetical order of the word.
We also want to have the most frequent words float to the top. The first two
options, `-g` and `-r` (combined as `-gr`), tell the computer to do a
**g**eneral numeric sort in **r**everse order. The next option, `-k1`,
specifies which part of the data to base the sort on. If a sample line of
`moby-clean.txt`, where we stored our counts, might be "whale 1234", it is
composed of two elements: the word and the number. BASH uses index notation,
meaning the word is the 0th element and the number is the 1st element.
Therefore, we use `-k` to tell it what to use as a **k**ey, and `1` to specify
the 1st element (the number). 

When you've stored the output, take a look at the most common words using
`head`. Do you notice anything interesting about this list? How far down do you
have to go until you find something that surprises you? What does it show us
about *Moby Dick* that we didn't know already?
