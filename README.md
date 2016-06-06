---
what: Computing Fundamentals for Human(s|ists)
where: University of Victoria, BC
when: Summer 2016
---

[John Simpson](https://twitter.com/symulation)  
[Dennis Yi Tenen](https://twitter.com/dennistenen)

## Class Description

This course is intended for humanities-based researchers with no programming
background whatsoever who would like to understand how programs work behind
the scenes by writing some simple but useful programs of their own. Over the
week the emphasis will be on understanding how computer programmers think so
that participants will be able to at least participate in high-level
conceptual discussions in the future with more confidence. These general
concepts will be reinforced and illustrated with hands-on development of
simple programs that can be used to help with text-based research and analysis
right away.

The programming language used for most of the course will be Python because of
its gentle syntax and powerful extensions. Using the command-line interface
and regular expressions will also be emphasized. We will also spend some time
taking glimpses at what is happening in the other DHSI courses to understand
how reading and writing programming code goes well beyond what we touch on in
this class.

## Day 1: Shell (4.5hr)

We will spend the day working with the terminal, learning the basics of the
file system, data flow programming, and text manipulation. The goal is to get
comfortable with the conversational, call and response style of programming.

- 1.1 Welcome
  - 1.1.1 Introductions
  - 1.1.2 Overview of week
  - 1.1.3 [Course
    Philosophy](https://github.com/denten-workshops/dh-core#philosophy)
  - 1.1.4 [Why command
    line?](https://github.com/dh-notes/dhnotes/blob/master/tutorials/command-line/000-cli.md)

- 1.2 Intro to Shell
  - [1.2.1] Plain text
  - [1.2.2](https://github.com/dh-notes/dhnotes/blob/master/tutorials/command-line/101-gps.md)
    Finding your way
  - [1.2.3](https://github.com/dh-notes/dhnotes/blob/master/tutorials/command-line/102-files.md)
    Files & Folders
  - [1.2.4](https://github.com/dh-notes/dhnotes/blob/master/tutorials/command-line/104-pipes.md)
    Pipes and redirects
  - [1.2.5](https://github.com/dh-notes/dhnotes/blob/master/tutorials/command-line/106-filters.md)
    Filters
  - [1.2.6](https://github.com/dh-notes/dhnotes/blob/master/tutorials/command-line/109-text.md)
    Basic Text Manipulation

- 1.3 Coding with John: A Simple Scraper with `Curl` and `RegEx`

- 1.4 Code Review: Prosecheck

- 1.5 Lab: [Hunting the Whale]()

## Day 2: Python I (6hr)

| When to use Shell?                | When to use Python       |
------------------------------------|--------------------------|
| - automate daily tasks            | - data science           |
| - manage files & folders          | - app development        |
| - remote server admin             | - NLTK                   |
| - data munging                    | - data visualization     |
| - quick & dirty text manipulation | - glue code              |
|                                   | - everything else        |

- Intro to Python
    - [006][6] Types & Variables
    - [007][7] Control Structures
    - [008][8] Lists and Other Iterables
    - [009][9] Functions
    - [010][10] Libraries: TextBlob

[6]: https://github.com/dh-notes/dhnotes/blob/master/tutorials/python/python-1.md
[7]: https://github.com/dh-notes/dhnotes/blob/master/tutorials/python/python-2.md
[8]: https://github.com/dh-notes/dhnotes/blob/master/tutorials/python/python-3.md
[9]:
[10]:

- Coding with John: Essay Grader

- Code Review: RikersBot

- Lab: [Animal Contexts] [11]

Light lecture in the morning that builds on experiences the day before,
focusing on the mindset of a programmer and important high-level programming
concepts. Following this will be a small set of activities using python solely
in the terminal to give a sense of how these concepts are implemented
generally.  The second part of the morning will include a live coding demo
using python in the terminal and a text editor in a separate window to show
how to build an simple tool that will report the corresponding symbol of the
Chinese Zodiac for a given input year that participants will be able to follow
along with.  See the zodiac folder for these steps.  This provides two
essential things:

1. observation of an actual coding process
2. a generic template demonstarting the core features of many programs that can be drawn on for the rest of the course and into the future.

## Day 3 (6hr)

- Completing building the [Zodiac][14] (John)
- Reading and annotating Python code (Dennis & John)
- Project brainstorm and initial planning (Dennis & John)

We will complete any remaining steps from the Zodiac tool demo and then move
to an activity where the participants are given working code examples and
asked to add comments to these.  This exercise will help participants
understand the structure of programs better while underscoring the importance
of commenting code in the first place.

Today we will also move from a command line + text editor environment for
programming to the Jupyter Notebook environment that is provided within the
Anaconda install.

In the afternoon participants will begin planning their project for Day four
and five.

## Day 4 (6hr)

The bulk of today will be spent by participants in teams developing the projects that they began planning the day before.  Participants will also be introduced to an *Integrated Development Environment (IDE)*, so there will be three options for how to develop a program:

1. Command line + text editor
2. Jupyter notebooks
3. [PyCharm](https://www.jetbrains.com/pycharm/) (a Python specific IDE)

There is no wrong answer here. Try to choose tools that are 
[FOSS](http://en.wikipedia.org/wiki/Free_and_open-source_software), universal, and
extensible.

It is hoped that we will have a Guest Speaker (reflections from DHSI 2014 class graduate) but this has not yet been confirmed. **Do we have someone for this year?**

Some time will be spent on an activity we call *Code from real life*, which will highlight some project that actually use Python in sophisticated ways, including:

- LitClock Twitter Bot ([project
    page](http://xpmethod.plaintext.in/public-discourse/litclock.html),
[twitter account](https://twitter.com/litclock),
[code](https://github.com/dhcolumbia/litclock/blob/master/cron-bot.py),
[data](https://github.com/dhcolumbia/litclock/blob/master/tweets.csv))
- [Science
    Surveyor](http://xpmethod.plaintext.in/public-discourse/surveyor.html)
- [HuViz](http://alpha.orlando.dev.semandra.com/) - Alpha of the Orlando/CWRC
    Graph / Ontology Viewer 
- [Old Bailey Data Warehouse Interface](http://analytics.artsrn.ualberta.ca/digging2data/) - a tool prototype for mining a copy of the Old Bailey database held on a special server.
- [Time slider and map of Canadian Libraries and Archives](http://cwrc.ca/rsc-src/) - Students in *this class* used Python with regular expressions to extract the addresses of 2009 libraries/archivs from a PDF.
 

- 1hr write a short 1-2 paragraph description of your project. Concentrate on
the goals of the *what* you are trying to accomplish, not the technical
details. Spend some time discussing what tools and datasets you would need for
the project. For example a simple project description may be:

> Using Python NLTK, our group would like to build an "essay grader" which
> would take as its input a sample essay and output a score, based on several
> parameters like sentence length variation and richness of vocabulary.

- 1hr translate or "formalize" your goals into a series of step by step
instructions in pseudocode.

- [NLTK
mini tutorial](https://github.com/denten/dhnotes/blob/master/python/python-4.md),
CSV and RegEx mini tutorials

- project work for the rest of the day

## Day 5 (3h)

**9:30 - 11:30am**

Reevaluate the scope of your project. Cut out inessential functionality. We are 
trying to get to a "minimally viable" prototype stage. Take notes via code comments 
throughout.

**11:3 - noon**

Concluding remarks. Showcase and Plenary meeting after.



## Project Code Share

- [imsdb scraper](https://github.com/denten-workshops/dhsi-coding-fundamentals/tree/master/code-samples/imsdb)

> reads a provided CSV file containing the names, authors, and URLs of film
scripts from an online database, downloads each of them and names the file
according to the AuthorName_FilmTitle.html conventionhh

- [the extractors](https://github.com/denten-workshops/dhsi-coding-fundamentals/tree/master/code-samples/extractors)

> this program takes an HTML file and extracts only the part containing the
> film script then strips out all HTML code and saves it as a .txt file

## Where to go from here?

- [What a well-informed person ought to know
about computers and communications](http://dl.acm.org/citation.cfm?id=2380975) by Brian Kirnighan
- [Data Science at the Command Line](http://datascienceatthecommandline.com/) by Jeroen Jannsens
- [DH Notes](https://github.com/denten/dhnotes/wiki)
- [Digital Humanities Research Portal](https://www.computecanada.ca/research-portal/digital-humanities-working-group/), Compute Canada
- [Foundations of Statistical Natural Language Processing](http://nlp.stanford.edu/fsnlp/) by Chris Manning and Hinrich Schütze
- [Natural Language Processing with Python](http://www.nltk.org/book/) by  Steven Bird, Ewan Klein, and Edward Loper
- [CODE
The Hidden Language of Computer Hardware and Software](http://www.charlespetzold.com/code/) by Charles Petzold 
- [Project Jupyter](https://github.com/jupyter)
- [PyLadies](https://github.com/pyladies)
- [Python Software Foundation](https://www.python.org/psf/)
- [The Programming Historian](http://http://programminghistorian.org)
- [Think Python: How to Think Like a Computer Scientist](by Allen B. Downey) by Allen B. Downey

[1]: https://piazza.com/class/ia5h507lfcr47d 

[2]: https://github.com/denten-workshops/dh-core 

[3]: https://github.com/denten/dhnotes/wiki
