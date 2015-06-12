---
what: Coding for Human(s|ists)
who: John Simpson and Dennis Tenen
where: University of Victoria, BC
when: June 8--12, 2015

---

## Resources
- [class forum][1]
- [tutorials][2]
- [DHnotes][3]

[1]: https://piazza.com/class/ia5h507lfcr47d
[2]: https://github.com/denten-workshops/dh-core
[3]: https://github.com/denten/dhnotes/wiki

## Class Description

This course is intended for humanities-based researchers with no programming
background whatsoever who would like to understand how programs work behind the
scenes by writing some simple but useful programs of their own. Over the week
the emphasis will be on understanding how computer programmers think so that
participants will be able to at least participate in high-level conceptual
discussions in the future with more confidence. These general concepts will be
reinforced and illustrated with hands-on development of simple programs that
can be used to help with text-based research and analysis right away. The
language used for most of the course will be Python because of its gentle
syntax and powerful extensions. Using the command-line interface and regular
expressions will also be emphasized. We will also spend some time taking
glimpses at what is happening in the other DHSI courses to understand how
reading and writing programming code goes well beyond what we touch on in this
class.

## Day 1 (4hr)

### Morning (10:15am-12:00pm)
- Welcome (John & Dennis)
  - Introductions
  - Overview of week
  - [Course Philosophy][6]
  - [Why command line?][7]
  - Why Python?

- Working Demo: Introduction to Terminal (John)
  - Cheatsheet
  - Regex
  - Simple problems using the cheatsheet

[6]: https://github.com/denten-workshops/dh-core#philosophy
[7]: https://github.com/denten/dhnotes/blob/master/cli-basics.md#why-command-line

### Afternoon (1:30pm-4:00pm)
- More [CLI basics][8].
- Lab: [Hunting the Whale][5]. (Dennis)

[4]: https://github.com/denten-courses/dhsi-coding-fundamentals/blob/master/labs/weasel.md
[5]: https://github.com/denten-courses/dhsi-coding-fundamentals/blob/master/labs/whale.md
[8]: https://github.com/denten/dhnotes/blob/master/cli-basics.md#table-of-contents

Intro to the Terminal. Terminal in the morning via a cheatsheet, a bit of a live 
demo, and then some problems that they can use the cheatsheet to solve.  Use of lab
activities in the afternoon that will push further into text manipulation in a Unix environment that is akin to what they might actually do with materials.

## Day 2 (6hr)

### Morning Session w/ Dennis (9:00am-12:00pm)

- [Text Manipulation at the Command Line][9]
- Exercise 1: Automate Moby
- [Anatomy of a Bash program][10]
- [Python 1][11]
- [Python 2][12]
- [Python 3][13]

| When to use Bash?                 | When to use Python       |
------------------------------------|--------------------------|
| - automate daily tasks            | - data science           |
| - manage files & folders          | - app development        |
| - remote server admin             | - NLTK                   |
| - data munging                    | - data visualization     |
| - quick & dirty text manipulation | - glue code              |
|                                   | - everything else        |


[9]: https://github.com/denten/dhnotes/blob/master/cli-basics/109-text.md
[10]: https://github.com/denten-courses/dhsi-coding-fundamentals/blob/master/write-log.sh
[11]: https://github.com/denten/dhnotes/blob/master/python/python-1.md
[12]: https://github.com/denten/dhnotes/blob/master/python/python-2.md
[13]: https://github.com/denten/dhnotes/blob/master/python/python-3.md

### Afternoon (1:30pm-4:00pm)
- Building the [Zodiac][14] I

[14]: https://github.com/denten-workshops/dhsi-coding-fundamentals/tree/master/python-live-code/zodiac

Light lecture in the morning that builds on experiences the day before,
focusing on the mindset of a programmer and important high-level programming
concepts.  Following this will be a small set of activities using python solely
in the terminal to give a sense of how these concepts are implemented
generally.  The second part of the morning will include a live coding demo
using python in the terminal and a text editor in a separate window to show how
to build an simple tool (Previously this was a Chinese zodiac symbol that
participants will be able to follow along with. See the zodiac folder for these
steps).  This provides two essential things: observation of an actual coding
process and a set of templates that they can draw on for the rest of the course
(and afterwards).

The afternoon will have them carrying out a lab assignment to further hone
their skills.

## Day 3 (6hr)

### Morning (9:00am-12:00pm)
- Building the [Zodiac][14] II

### Afternoon (1:30pm-4:00pm)
- Project brainstorm

## Day 4 (6hr)

1. Guest Speaker (reflections from DHSI 2014 class graduate)

2. Two approaches to coding environments.

`IDE = interpreter + text editor + file browser`

Two approaches:
- all rolled into one ([PyCharm](https://www.jetbrains.com/pycharm/))
- ipython (interpreter) + vim (text editor) + command line (manage files)

There is no wrong answer here. Chose tools that are 
[FOSS](http://en.wikipedia.org/wiki/Free_and_open-source_software), universal,
extensible.

3. A day in the life. What can be done with Python?

- LitClock Twitter Bot ([project
  page](http://xpmethod.plaintext.in/public-discourse/litclock.html), [twitter
account](https://twitter.com/litclock),
[code](https://github.com/dhcolumbia/litclock/blob/master/cron-bot.py),
[data](https://github.com/dhcolumbia/litclock/blob/master/tweets.csv)
- [Science
  Surveyor](http://xpmethod.plaintext.in/public-discourse/surveyor.html)
- [HuViz](http://alpha.orlando.dev.semandra.com/)- Alpha of the Orlando/CWRC
  Graph / Ontology Viewer Old Bailey Data Warehouse Interface 
- Prototype tool for mining a copy of the Old Bailey database held on a special
  server http://analytics.artsrn.ualberta.ca/digging2data/ TAPoR - Great place
to look up new tools. http://www.tapor.ca/ 

4. [NLTK Tutorial](https://github.com/denten/dhnotes/blob/master/python/python-4.md)

## Day 5 (3hr)

Project work all morning and project presentations in the afternoon. Where to
go from here. Resources. Paths to development.
