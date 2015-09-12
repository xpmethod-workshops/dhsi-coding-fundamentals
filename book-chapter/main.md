---
title: "Coding Fundamentals for Human(s|ists)"
authors:
- Phillip Polefrone
- John Simpson
- Dennis Tenen
bibliography: main.bib

---

We write this chapter as a general reflection on teaching computing
fundamentals in the humanities context, and more specifically in the wake of
teaching *Computing Foundations for Human(s|ists)* at the Digital Humanities
Summer Institute (DHSI), University of Victoria and *Computing in Context* at
Columbia university.[^ln-titlelink] These courses were intended for humanities
researchers with no previous programming experience who wanted to learn how
programs work by writing a few simple, useful programs of their
own.[^ln-courselink] The topics covered included working with files and folders
at the command line, text-stream manipulation with GNU Bash, regular
expressions, and Python basics like native data types, variables, functions,
and control structures. At the end of the course, our students worked on their
own and in small groups to create a small web scraper, an "essay grader," a
comma-separated value file manipulator, and a program that evaluates poetry
based on its measure of similarity to Byron's.

Our aim in this chapter is not to recapitulate the experience of teaching (we
would not have the space to do it here, in any case), but to reveal some of the
core principles that went into making the course, to talk about the rationale
behind our teaching philosophy, and, more broadly, to suggest an approach to
teaching programming in the humanities environment.

[^ln-titlelink]: "Human(s|ists)" is actually a regular expression, a way to
search text for specified patterns. In this case it picks out anything starting
with "Human" and ending in *either* "s" or "ists". So, it acts as a stand-in
for both "Humans" and "Humanists".

[^ln-courselink]: An archived version of the course can be accessed at
http://web.archive.org/web/20150614161609/https://github.com/denten-workshops/dhsi-coding-fundamentals/blob/master/README.md

<!---
JS: Should we say something about coding vs programming here?
DT: I don't have strong feelings about the distinction. Up to you.
PRP: Skipping for now---seems like the intro does what it needs to without the
distinction
--->

## 1 Critical Computing in the Humanities, Core Principles

It is our firm belief that teaching computational principles in the humanities
must be grounded in the practices of humanities research and answer to the
values held by that academic community. Inspired by a number of initiatives
advancing a similar philosophy, we refer to this approach as "critical
computing."[^ln-first] The following eight principles connect key ideas in
computation to values intrinsic to humanistic inquiry:

[^ln-first]: We are not the first nor the only instructors to think about
digital pedagogy this way, nor are we the only ones to be offering a course
based on these principles.  Software Carpentry, for example, has been
advocating a similar approach since its inception. Similarly, the *Programming
Historian* is "an online, open-access, peer-reviewed suite of tutorials that
help humanists learn a wide range of digital tools, techniques, and workflows
to facilitate their research." See also @harrell_toward_2015.

### 1.1 Target daily computation.

Contemporary computational devices are a foundation of daily life. They are
involved in everything from financial markets, to archival research, to the way
many keep in touch with friends and family. Yet for those without technical
training, the inner workings of these devices remain a source of mystery and,
consequently, frustration. Recognizing this, our courses target the underlying
structure of tools that many rely on for their daily computation, teaching our
students how these tools work (and not just how to use them). Beyond the
principles of programming, we want our students to understand the basics of
networking, security, and operating systems. By revealing the innards of
opaque computational "black boxes," we hope to empower our students to take
control of their everyday computational practice.

The most universal daily computing task of the humanities, regardless of
research interest, is writing. Our first step in addressing daily humanistic
computing in the classroom, then, is to create small "experiments" that address
a student's own writing. These might include a lab session in which students
analyze their own documents for commonly over-used "weasel words,"[^ln-weasel]
for example. Working with one's own documents introduces important
concepts---like "relative" and "absolute" paths, file formats, character
encoding, and small shell utilities like `grep` (used to search through text
files), `wc` (word count), or `sed` (stream editor for text
transformation)---that can later be extended into more advanced concepts in
system administration or natural language processing. Short exercises in
text-based programming can be put together to form the students' first
programs, performing tasks like "safely rename all the files in this folder
according to such-and-such rule," or "keep a daily log of my writing progress."

[^ln-weasel]: Weasel words are words that sound very meaningful, but instead of
adding, diminish the impact of persuasive writing. The "very" in the previous
sentence, for example.

### 1.2 Use few, free, small, simple, universal, and powerful tools that you can hack and understand.

Researchers, librarians, students, and faculty are faced with a bewildering
array of software choices. In making the decision to invest time and resources
into learning a new tool or methodology, we are guided by "Unix Philosophy" and
the free software movement. The Unix philosophy of computing prioritizes small,
modular pieces of software that "do one thing well" [@mcilroy_unix_1978]. Such
software can then be chained together with other small but powerful tools to
achieve complex results. Free software, besides being cost effective ("free as
in beer"), also opens the tool itself to humanistic inquiry. Code is said to be
free whet it is available for inspection, interpretation, critique, and
modification. It is, in the words of Richard Stallman, "free as in speech"
[@stallman_why_2007]. Above all, we seek out universal tools that we can
understand and, where needed, customize to fit our own particular needs and
contexts. These tools can be applied in diverse contexts like library
infrastructure, web design, data science, and the production of critical
editions.

### 1.3 Privilege human legibility.

Whenever possible we privilege legibility and longevity over terseness of
expression, cleverness, or performance. We begin by having our students
describe their program, step by step, in language natural to them and to their
task. Pseudocode in plain English becomes the basis for well documented
programs and readable code that can be easily maintained or adapted.

### 1.4 Store data in human-readable text streams.

The file formats we use to store data have serious implications for anyone's
ability to make use of that data in the future. As a format's underlying code
tends toward opacity, it becomes increasingly difficult for new programmers to
read during development and for others to draw on files in that format in the
future. The number and complexity of file formats relates closely to the
proliferation of closed tools and platforms: arcane file formats inhibit access
to their contents as raw data or, for that matter, any platform but the one for
which it is intended. The danger of a single-platform format is most acutely
felt by archivists faced with preserving short-lived data structures meant for
obsolete platforms of the recent past. For humanists who rarely work with truly
large datasets or collections, the risk of rapid obsolescence offsets any
hypothetical gains in speed or performance offered by a new note-taking
platform, a needlessly complex database, or a constantly upgrading proprietary
text editor.[^ln-plain] When selecting a data format, we ask: does it need
special software to render? How long has it been around? and What organization
is responsible for maintaining the standard?

[^ln-plain]: Conveniently for us, the Unix philosophy privileges inputs and
outputs in plain text format, which can be used to store everything from
personal notes, to article drafts, to huge datasets of metadata. Unix provides
many powerful utilities that work with plain text. In fact, the notion of human
readability is even encoded at the operating system level.

### 1.5 Divide big problems into small, modular components (algorithmic thinking).

Our goals in the classroom go beyond the instrumental. The ability to automate
machines is merely a side effect of algorithmic, analytical thinking. To learn
to think like a programmer is useful in many contexts: it involves dividing
big, complex, and seemingly intractable problems into small, modular, solvable
components. Writing a grant proposal, for example, a book, or a dissertation
may initially seem like a daunting and onerous task. Progress can be made once
it is divided into small, doable steps: like explaining a recipe for making a
cake (an exercise we use in the classroom).

<!---
JS: Seems this could be collapsed into 1.2 for the sake of simplicity
DT: I tried it, but I think it is a good point to stand on its own.
DT: What do you guys think of the order?
--->
### 1.6 If you have to do something more than ~~once~~ a hundred times, automate.

Programmers are smart and lazy. After doing a task more than a few times, a
good programmer's intuition will be to automate the task. For example, we often
use the `rsync` command to back up our documents; however, after a few months
of running it manually, the user can delegate that task to the built-in
scheduler called `cron`. Humanists may not have the same automating impulse,
but they can save just as much time with automation as anyone. As the daily
computing tasks of humanists are considered in these terms, inefficiencies and
causes of unnecessary repetition can be eliminated. The saying normally goes
that if you do it more than *once*, automate. One must know, however, exactly
*what* to automate. When backing up your files, do you want to back up the
whole system or a few select folders?  How often should the backup script run?
The answers become apparent only after extensive manual use. As we introduce
automated "daemons" that run tasks on our behalf, we want to make sure we think
through any unintended side-effects: technological, personal, and political.

### 1.7 Do it right---*the first time*.

Although programmers are lazy, they are lazy in the right way. Doing things
badly, in a haphazard fashion, accumulates technological, intellectual, and
eventually an ethical debt to oneself and one's community. Code comments (or
the lack of them) are a common site of egregious laziness: it is easy to skip
documenting one's code or document insufficiently. "It just works, why bother?"
However, a piece of code that makes perfect sense today may seem impenetrable
tomorrow. Without comments, time needs to be spent to recreate the reasoning
behind the original implementation. Similarly, we advise our students against
simply cutting and pasting code snippets from our tutorials. We want them to
follow our thinking, to annotate, and to review their notes regularly. In the
social context, lazy practices are unethical because they "bank" against the
labor of others in the future, saving one's own time now at the expense of
someone else's later. Doing things the right way the first time costs less than
making up for it down the line.

### 1.8 Bootstrapping and time well spent.

When thinking of what to teach or where to invest our time, we look for
"bootstrapping" effects that come from using powerful, universally available,
and extensible software---that is, teaching skills and concepts that will have
the highest impact because they transfer to the greatest number of contexts or
tasks. The command line, for example, useful at first for file management and
operating system exploration, later becomes an important resource for remote
server administration, web design, and data science. Furthermore, the skills
learned in the process of becoming comfortble on the command line transfer to
physical computing, fabrication, web scraping, and text analysis. Learning
about relative and absolute paths locally will make it easier to understand
internet infrastructure, domain names, and resource allocation. It leads to
Secure Shell and Pretty Good Privacy (PGP), used by activists and journalists
to protect their communications from surveillance.

With the goal of bootstrapping in mind, one can see the real value of lessons
that many might eschew for fear that they are too technical or complicated. It
may be appealing at first to hide computational complexity behind "simple"
visual interfaces, for example, but these interfaces do not share a common
visual language and they do not transfer well across software platforms. Our
colleagues in computer science sometimes worry that introducing command line
interfaces and raw coding environments may alienate humanists. We believe that
limited, "dumbed-down" interfaces do even more harm. They further mystify
computing to an audience that already feels removed from the material contexts
of their daily knowledge production. In building the foundations, we want our
students to spend their time well: to learn tools and skills that can support a
wide variety of activity within diverse cultural contexts. The extra care we
take in explaining the reasoning behind our technological choices can motivate
the students through any initial difficulties of learning how to code "the hard
way," without shortcuts or artificial limitations.

<!---
JS: Mention the CS chair observation?
DT: I don't think we should mention his name. But perhaps a footnote, if you
can find a way to phrase it.
--->


## 2 Digital Humanities Core

Programming can involve long stretches of frustration (Why does this not work?)
punctuated by the short bursts of elation that come with accomplishing
something difficult (It works!). Rather than allowing students to view their
initial lack of results as failures, we attempt to channel feelings of
hindrance into a practice of problem solving and discovery, related to
similarly difficult but more familiar tasks of archival research and long-form
analytical writing. Just like writing, coding falls on a spectrum of
proficiency that constitutes a small but foundational part of a larger,
variegated skill set.

Depending on one's research interests and career path, as a DH practitioner one
will have some mixture of the following core skills (with examples in
parenthesis):

- Text markup (plain text, *Markdown*, *Pandoc*, *TEI*)
- Command line interface proficiency (*Bash*, pipes, regular expressions)
- Content management (*Jekyll*, *Wordpress*)
- Version control (*Git*, *GitHub*)
- Programming language (*Python*, *R*, *JavaScript*)
- Networking (SSH, VPN, hosting)
- Security (PGP)
- System administration (*AWS*, *Linux*, *Apache*, *MySql*)
- Project management (*GitHub Issues*, *BaseCamp*)
- Probability, statistics, and algorithms

Computational practice in the humanities begins with text. Whatever our home
discipline, we are all involved in the reading and writing of texts. It is
natural, then, to commence training with textual transformations: to understand
how text is produced and where it resides physically, on the machine. Learning
to author in a markup language like HTML or Markdown is often a first step into
the world of critical computing. Text transformations lead to the operating
system and the file hierarchy. Tasks like regular backups and desktop
organization can be used to familiarize students with foundational concepts
like relative and absolute file paths or the distinction between plain text and
binary formats.

Our core principle of starting with daily computation also suggests covering
version control and content management early in the curriculum. Although not an
easy subject, version control comes naturally to a community used to thinking
about drafts, manuscripts, and revisions. Increasingly, version control systems
can also be used to host websites, stream data, and create full-blown
publishing platforms. For example, *The Programming Historian* journal uses
*Jekyll*, a static website generator, and GitHub Pages for publishing and
distribution. Using that model to create personal academic profiles, image
galleries, or critical editions, digital humanists can use version control
systems to have a greater hand in the conditions of their academic production.
These systems can also influence scholarly practices and processes: by
prompting users for notes with each commit, Git encourages note-taking and
journaling throughout the versioning process. Finally, multi-user version
control can be used to increase transparency in academic collaborations.
Similar to the scientist's lab notebook, the Git journal fixes the flow of
ideas and labor by recording the distribution of tasks in a collaborative
environment, helping teams keep track of work for accurate
attribution.[^ln-versionlink]

A programming language occupies a central place in computational practice. All
forms of digitality pass through some form of encoding and automation. Only a
small step separates text transformations, command line shells, and content
management systems from a programming language. We often "trick" our students
into programming by automating simple tasks like word substitution from the
command line. The same task could then be repeated using *Python* or *R*,
reinforcing skills learned earlier in the process while building on those
skills to go to the next level of complexity. While text transformations at the
command line are useful for small tasks and for pedagogical purposes, most
serious computational textual analysis or natural language processing will
require knowledge of a programming language such as Python, R, or Haskell.
Later, we will discuss which tasks are appropriate to the command line and
which to coding.

Because the internet plays such a key role in transforming academic practice,
knowing the basics of networking---infrastructure, routing, packet switching,
protocols, security, encryption---is also key to pursuing higher-level goals
like preserving free speech online, protecting a journalist's sources, or
bypassing censorship filters. The care and maintenance of personal document
archives---research papers, article drafts, and book manuscripts---leads
naturally into server management. The server is where many of the skills
learned earlier come to fruition. Running websites requires a long "stack" of
technological components. These are almost impossible to use well without
knowledge of the command line, a programming language, and networks.

No project is complete without some sense of planning and organization. Project
management is an important part of computation in the private sector, and it is
an increasingly formalized part of software engineering. Projects fail and
succeed by the measure of their ability to coordinate action across time zones
and continents. When teaching programming, we ask our students to start with
"scoping" their projects in plain English first, then to transform these
technical specifications into pseudocode, which finally serves as the basis for
program design and architecture. We ask our students to submit these documents
along with code and consider them as important as a functioning program.

Finally, programming fundamentally involves a measure of algorithmic thinking.
On some abstract level, the specific languages, tools, and implementations are
secondary to the logical structures that support all higher level activity.
This may be the most difficult obstacle to tackle. Every word cloud, every
topic model, and network visualization tool hides a number of assumptions
driven by sophisticated logic that comes from the fields of statistics and
computer science. Without training in the methods on which these tools are
based, we are bound to remain mere consumers of technology rather than active
participants in its formation. Critical computing practice, like critical
thought, requires a measure of logical and mathematical literacy.

We do not mean for this list to represent a comprehensive statement about
computation in the humanities. Rather, we would argue that most projects,
however large or small, employ at least *some* aspects from the above "dream
list." The ubiquity of these modular components is what classifies them as
"core" or "foundational" competencies. Few people apart from professional
computer scientists and software engineers would claim mastery over the full
stack of what is mentioned here. It is much more likely for digital humanists
to develop proficiency in one or several areas of practice. Yet any one of the
above foundational competencies have spillover effects that "level up" the rest
of the list. An intensive, week-long class, like the one that we teach at
DHSI, can only begin to address a small part of the larger, complicated puzzle.

[^ln-versionlink]: Given that we have looked to Software Carpentry for some of
the methodology that we employ in the course it should be noted that we do not
spend any time on version control via tools such as Git or Mercurial. This was
done initially so that more time could be spent on programming concepts,
hands-on coding work, and unpacking the black box that is the command line.
The importance of version control for efficient and effective coding via
protecting against loss and enabling collaboration with others is recognized
and future versions of the course may include it as a consequence. As with all
training that is already time constrained down to the essentials, the challenge
is what to take out to add this in.

## 3 Three Locations of Computing

<!---
JS: Our approach owes a small debt to Software Carpentry since this is what I
have based a good chunk of the content on the first year and some of this got
rolled
into the second. This is likely the place to acknowledge it.
DT: No problem. Let's do it in footnotes though.
--->

We often begin our courses by outlining the above "big picture" principles,
challenges, and considerations. Like learning a foreign language, programming
takes time and patience to master. And as is the case with any difficult skill,
motivation to practice correlates to chances of long-term success. Developing
the intellectual motivation to stick with the program is therefore one of our
paramount goals. For this reason, we begin the course with the "frustration
points" of everyday computing. In our experience, even simple tasks like
saving a file from an internet browser is rife with anxiety and frustration:
Where did that file go? How do I find it again? What type of file is it? Modern
operating systems conceal such information from average users.

Our task as instructors is to channel that frustration into opportunities for
discovery. Students, university faculty, and librarians intrinsically approach
documents, file systems, and datasets as matters of critical importance,
embodying the fruits of long-standing commitment and hard-earned labor. We can
therefore harness the patience and care they bring to their research to bare on
computing fundamentals. In our experience, students respond enthusiastically to
the mission of reclaiming the material contexts of their daily intellectual
production.

As suggested by the metaphor of software development "environment," a site of
computation denotes both the interface through which the human engages the
machine and the type of interaction the interface demands. A site is also a
conceptual space, though, each with its own logic and set of values.
Consequently, we identify three locations as key sites of digital literacy: the
command line, the language interpreter, and the text editor.

### 3.1 Command Line

The first of these locations is the command line, a Unix shell and a command
language for text-based call-and-response "dialogue" between the user and the
Unix-based operating system. On the level of the operating system, all
operations are in some sense on files. For this reason, the aspiring coder must
develop a firm grasp of files and folders, along with their corresponding
manipulation techniques. The command line is where the power user interacts
with files and folders. Everything from downloading a sample corpus, to writing
research papers, to debugging code eventually leads to the command line. The
command line serves as the base of our operations. A new project start with a
new folder. The completion of the project will often involve the publication
and the sharing of files across email clients and code repositories. We
therefore begin and end each session with the command line.

One way to think of the command line is as a powerful alternative to tools like
*File Explorer* (Windows) and *Finder* (Macintosh). Unlike these popular point
and click programs, the command line interface (CLI from now on) is a
text-based, dialog-driven mode of interaction with the operating system. On
some deeper level, the machine "speaks" in binary code. The command line
"interprets" English-like commands (in a language called Bash)[^ln-bash] into binary. In
this when deleting a file, one can instruct the machine to `rm filename.txt`
instead of dragging and dropping it to the waste bin. Note that "dropping into
the waste bin" merely offers a visual metaphor for the underlying bit-wise
operations. The CLI alternative turns the metaphor into a more exact command
`rm`, which stands for "remove." Similarly to direct the computer to move a
file, we would use the `mv` command. Unlike their visual and metaphorical
counterparts, the Bash commands contain many advanced options, accessible
through the manual, or `man`. As expected,`man mv` displays the manual pages
for the move command.

Furthermore, because Bash commands are in themselves a type of a programming
language, they can be chained together and automated to produce complex
behavior. Imagine, for example, writing a book or a dissertation in a directory
that contains several files in plain text format (.txt), each corresponding to a
chapter. The writer can then use the following script to produce the total
word count:

```
wc -w ~/user/documents/book/*txt | tail -n 1 | sed 's/[a-z ]//g' >> log.txt
```

The above "incantation" does four things:


1. Count the words in all of the `.txt` files found in the present directory.

    Input:

    ```
    wc -w *md
    ```
    Output:

    ```
    11717 1-chapter.txt
    12457 2-chapter.txt
    13780 3-chapter.txt
    10542 3-chapter.txt
    74850 total
    ```

2. Isolate the total count from the individual file counts.

    Input:

    `tail -n 1`

Output:

    `74850 total`

3. Remove the word "total" and keep only the number count.

    Input:

    `sed 's/[a-z ]//g'`

    Output:

    `74850`

4. Append the count to the log file.

    `>> log.txt`


The vertical line (`|`) and angle bracket (`>>`) allow us to chain the commands
into a system of pipes and redirects, passing the text output of one operation
to another. Once saved to disk, this small script can be set to run
automatically at a predetermined time interval and used to keep a daily log of
one's writing activity.

Learning the command line is not just a matter of opening up new ways of
interacting with files, though. In learning command line basics, students
become familiar with concepts that will establish foundational techniques that
will be built upon in higher-level contexts, in true bootstrapping style. The
above exercise can be used to discuss the difference between relative and
absolute file pats (`~/usr/documents/book/*txt` vs.
`/usr/documents/book/*txt`). It contains the basics of regular expressions
(`[a-z ]`). And because the output of `wc -w` is a string, the excercise can be
used as the basis for string manupalation and later data normalization and
rudimentary natrual language processing. Finally, such excercises can lead to
the basics of remote server management, networking, security, and encryption.

[^ln-bash]: "Bash is the GNU Project's shell. Bash is the Bourne Again SHell.
Bash is an sh-compatible shell that incorporates useful features from the Korn
shell (ksh) and C shell (csh). It is intended to conform to the IEEE POSIX
P1003.2/ISO 9945.2 Shell and Tools standard. It offers functional improvements
over sh for both programming and interactive use. In addition, most sh scripts
can be run by Bash without modification" [@free_software_foundation_gnu_2007].

 http://www.gnu.org/software/bash/

### 3.2 Python

The second is Python, a
widely-used modern programming language, that, like Bash, privileges simplicity
and human readability. 

As we have begun to explain above, Python is a programming language that has
attained widespread popularity in part because of the elegant simplicity of its
syntax and its vast adaptability. 

Same structure as above. 

1. Explain what it is. 
control structures + data types + built-in functions + syntax + interpreter
Why Python

2. Why.

3. Easy examples we cover in class (zodiac fortune teller or an choose your own
adventure exercise). control structures + data types + built-in functions +
syntax + interpreter

3. A glimplse of more advanced possibilities. 

4. When to use one over the other (see chart)

| When to use Bash                  | When to use Python       |
+-----------------------------------|--------------------------+
| - automate daily tasks            | - data science           |
| - manage files & folders          | - app development        |
| - remote server administration    | - NLTK                   |
| - data munging[^ln-munge]         | - data visualization     |
| - quick & dirty text manipulation | - glue code              |
|                                   | - everything else        |

[^ln-munge]: Data munging is a recursive computer acronym that stands for
"Munge Until No Good," referring to a series of discrete and potentially
destructive data transformation steps [@raymond_mung_2004].

### 3.3 Text Editor

The third is the humble-seeming text editor: the most common digital tool of
humanities scholarship, among the least often considered, but perhaps the most
important.

Explain the difference between interactive, conversational, exploratory type of programming and
"saving the conversation" for the future in the text editor.

Why text editors are important (plain text).

Finish with a chart. When to use interactive programming (data exploration) and
when to build programs (what is the opposite of interactive. I can help in this
section.


| Interactive Programming           | Text Ed |
+-----------------------------------|--------------------------+

### Conclusion

More directly, there are six properties that these locations embody that make
them particularly suitable for an introduction to humanities computing class.
Because the text editor is a more highly variable location than the other two,
we will discuss these properties first in terms of the command line and Python:

1. Ubiquity. Command line interfaces are standard across all Unix-derived
systems, which includes Linux, Mac OS, Chrome OS, Android, and many others
powering everything from Raspberry Pis to supercomputing clusters. Similarly,
Bash, Python, and tools that help write Python code, are available on any
system that a student of the class is likely to encounter.[^bash-nix-os]
Because of their versatility, both are used in a wide range of environments by
large user communities. This also means that help is widely available.

[^bash-nix-os]: While Bash is confined to \*nix-style operating systems there
are emulators that reproduce its functionality on most systems that a student
in the class is likely to encounter.

2. Simplicity. The syntax used in both Bash and Python is relatively
straightforward. In Bash, most tasks can be broken down into a series of
single-line commands that can be chained together through pipes (|) and
redirects (> and >>). Python does away with much of the frustrating syntax of
languages that came before it, saving users from the need to keep track of
byzantine chains of brackets and other syntactical tangles. The elegance of
Python's syntax not only aids in learning and retention: it also adheres to the
ethos of legibility we discuss in our core principles above. 

3. Power. Bash and Python are powerful enough that, between them, a digital
humanist is able to realize almost any task imaginable (and possible). They may
not be the most suitable environments or languages for every task, of course,
but in combination they form the digital humanist's swiss army knife, allowing
its user to accomplish most anything that is needed.

4. Durability. As with data structures, we favor tool that are unlikely to
become obsolete. Neither Bash nor Python are going away anytime soon, meaning
that solutions written in either will continue to be functional for the
foreseeable future.

5. Hackability. It is relatively straightforward to write one's own
commands/methods within both Bash and Python *and to see how those that
currently exist were written*. While this is not something that we cover in our
courses, the possibility for end users to investigate and expand the languages
that they are working on is a basic tenet of empowering users by unlocking what
would otherwise be black boxes---and, therefore, inaccessible.

6. Fun. The power, versatility, and relative accessibility of these tools means
that they are able to be *fun* as well as effective. Both Bash and Python
invite an interactive methodology that is at once engaging and interesting,
drawing students forward in their learning.

These three locations build solid foundations for critical practice in the
digital humanities. All more advanced stuff rests on these foundations. In
starting here we dispell anxiety and illusion.[^ln-coauthor]

<!---
JS: Could we collapse this into 1.0?. Possibly add in the
importance of teaching them how to help themselves...

DT: Let's move to the conclusion (done). We'd need to transition into here
better. Re-word as a conclusion.
--->

Keep poking, get help, take notes, comment, annotate, share, remix, and train
others.

Finally, and this noticed by several course observers over the years, students
in the humanities are sometimes curiously hesitant to explore their machines.
In the absence of a tinkering upbringing and in the presence of cultural
divides that regularly reinforce norms like "Those in the Arts and Humanities
can't do programming, math, science, etc.", they might be worried of breaking
expensive equipment or losing sensitive data. Demystifying the magical black
box and learning some habits that prevent irrevocable loss of data addresses
that fear, encouraging the students to tinker and to explore. Researchers at
the later stages of their career may be particularly reluctant to ask for help
or to express their questions in public. Our teaching approach therefore
encourages shared expertise. We model not being afraid to expose our own gaps
in knowledge. We ask students to keep copious notes, to annotate their code, to
share and improve on each other's work. Notes grow into tutorials, tutorials
into courses and workshops. Eventually, in following these principles, we hope
for our students to become catalysts of change in their own communities of
practice.

[^ln-coauthor]: A note on coathorship: a detailed history of author
contributions can be found on our GitHub page at
[https://github.com/denten-workshops/dhsi-coding-fundamentals/commits/master/book-chapter/main.md](https://github.com/denten-workshops/dhsi-coding-fundamentals/commits/master/book-chapter/main.md)

