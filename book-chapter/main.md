---
title: "Coding Fundamentals for Human(s|ists)"
authors:
- Dennis Tenen
- John Simpson
bibliography: main.bib

---

## 0 Introduction

We write this chapter in reflection of teaching computing fundamentals in the
humanities context in general, and more specifically, in the wake of teaching
**Computing Foundations for Human(s|ists)** at the Digital Humanities Summer
Institute, University of Victoria. This week-long course was intended for
humanities-based researchers with no previous programming experience, and, as
we wrote in the course description, for those who would like to understand how
programs work by writing a few simple, but useful programs of their
own.[^ln-courselink] The topics covered included working with files and folders
at the command line, text stream manipulation with Bash Unix Shell, regular
expressions, along with Python basics like native data types, variables,
functions, and control structures. At the end of the course our students worked
on their own and in small groups to create a small web scraper, an "essay
grader," a comma separated value file manipulator, and a program that evaluated
poetry for its measure of similarity to Byron.

Our aim in this chapter is not so much to recapitulate that experience (we
would not have the space to do it here, in any case) but rather to reveal some
of the ideas that went into making the course, to talk about the rationale
behind our teaching philosophy, and, more broadly, to suggest an approach of
teaching programming in the humanities environment.

## 1 Critical Computing in the Humanities, Core Principles

It is our firm belief that the teaching of computational principles in the
humanities must happen in context: that is grounded in the practice of
humanities-based research and answering to the values held by the academic
community. We call this approach critical computing, which for us involves the
following nine principles:

[^ln-courselink]: An archived version of the course can be accessed at
http://web.archive.org/web/20150614161609/https://github.com/denten-workshops/dhsi-coding-fundamentals/blob/master/README.md

### 1.0 No black boxes! Empowered computing.

Computers are everywhere. They mediate everything from financial markets, to
archival research, and to the way many keep in touch with their friends and
family. Yet, for those without computational background, these devices remain a
source of mystery, magic, and frustration. Our course begins then with a
process of demystification. We want our students to understand not only the
principles of computer science, but the basics of software and electrical
engineering. As much as possible, we would like to reveal the innards of opaque
computational "black boxes," empowering our students to take control of their
everyday computational practice.

### 1.1 Use few, free, small, simple, universal, and powerful tools that you can hack and understand.

Librarians, students, and faculty are faced with a bewildering array of
software choices. Companies that promise "innovation" and "disruption" in the
classroom routinely approach administrators with offers to try and to buy
software at the institutional level. The imbalance of information between the
vendors and the users often results in wasted time and resources. In making the
decision to invest time and resources into our own computational practice, we
are inspired by the philosophy embodied by the *\*nix* family of operating
systems (Unix, Linux, Arch Linux, OpenBSD, and others). The *\*nix* community
has been advocating for the use of free (as in speech and as in beer) and open
source software (FOSS). FOSS software works in the academic humanities context
because free and open access code is available for inspection, and therefore,
for interpretation, critique, and modification.

Furthermore, the *\*nix* philosophy privileges small, modular pieces of
software that "do one thing and do it well." Such software can then be stringed
together with other small but powerful tools to achieve complex results.
Throughout, we seek to avoid proprietary file formats, non-standard interfaces,
and vendor lock-in. Simplicity, ease maintenance, and transparency are key for
creating a culture that lasts. The preference for openness and simplicity is
not just ideological, but also practical. In the past several decades,
following the same principles, *\*nix* family of operating systems has become
the dominant platform that powers everything from cellular phones, to robots,
drones, personal computers, and super clusters. This also means that our
investment of time into such ubiquitous interfaces can scale across time and
devices. When deciding what to use and what to teach, we seek out universal
tools that underlie a variety of computing practices, from library
infrastructure, to web design, to data science and critical-edition making.
More than anything, we seek out tools that we can understand and, if needed, to
customize to fit our own particular needs and contexts.

### 1.2  Wherever possible store data in human-readable text streams.

The problem of file formats relates closely to the proliferation of closed
tools and platforms. It is most acutely felt by archivists faced with
preserving short-lived data structures from obsolete platforms from recent
past. For many humanists, who rarely work with truly large datasets or
collections (on the order of millions documents), the real risk of rapid
obsolescence offsets any hypothetical gains in speed or performance offered by
a new note-taking platform or a complex database. Conveniently for us, the Unix
philosophy privileges inputs and outputs in plain text format, which can be
used to store everything from personal notes, to article drafts, to huge
datasets of metadata. Unix provides many powerful utilities that operate on
plain text. In fact, a notion of human readability is encoded at the operating
system level. When faced with a list of compromises, in the name of design,
performance, efficacy, or legibility, we consistently prioritize legibility.
That choice informs our practice throughout. When working with audio or visual
material, for example, we similarly prefer widely-supported, non-proprietary
standards. When selecting a data format, we ask: does it need special software
to render? How long has it been around? and What organization is responsible
for maintaining the standard?

### 1.3 If you have to do something more than ~~once~~ a hundred times, automate.

Programmers are lazy. After doing a task more than a few times, a good
programmer's intuition will be to automate the task. For example, we often use
the `rsync` command to back up our documents. However, after a few months of
running it manually, the user can delegate that task to the built-in scheduler
called `cron`. The saying normally goes that if you do it more than *once*,
automate. However, one must know exactly what to automate. When backing up your
files, do you want to back up the whole system or a few select folders? How
often should the backup script run? The answers become apparent only after
extensive manual use. As we introduce automated "daemons" that run tasks on our
behalf, we want to make sure we think through any unintended side-effects:
technological, social, political.

### 1.4 Do it right the first time.

Although programmers are lazy, they are lazy in the right way. Doing things
badly, in a haphazard fashion, accumulates technological, intellectual, and
eventually an ethical debt, to oneself and to the community. Code comments are
the simplest example of this. It is easy to skip documenting one's code. "It
just works, why bother?" However, a piece of code that makes perfect sense
today, becomes obscure tomorrow. Without comments, time needs to be spent to
recreate the reasoning behind the original implementation. Similarly, we advise
our students against simply cutting and pasting code snippets from our
tutorials. We want them to follow our thinking, to annotate, and to review
their notes regularly. In the social context, lazy practices are unethical
because they "bank" against the labor of others, in the future, literally
borrowing someone else's time. Doing things the right way now, saves
unnecessary effort later.

### 1.5 Target daily computation.

Programming classes in the sciences often begin with coding for coding's sake,
intended an audience inherently interested in logic, math, and engineering. The
humanities must find its own intrinsic motivations for learning to code, broad
enough to appeal to the community at large. For this reason, we begin our class
with exercises that target daily computation and writing practice, common to
researchers at every stage of their development. We create little "experiments"
that address one's writing, for example. These include a lab session in which
students analyze their own documents for commonly over-used "weasel
words,"[^ln-weasel] for example. Working with one's own documents introduces
important concepts like "relative" and "absolute" paths, file formats, and
small shell utilities like `grep` (used to search through text files), `wc`
(word count), `sed` (stream editor for text transformation), that can later be
extended into more advanced concepts in system management or natural language
processing in Python. When put together, these small utilities form the
students' first programs, performing tasks like "safely rename all the files in
this folder according to such-and-such rule," or "keep a daily log of my
writing progress."

[^ln-weasel]: Weasel words are words that sound very meaningful, but instead of
adding, diminish the impact of persuasive writing. The "very" in the previous
sentence, for example.

### 1.6 Bootstrap and time well spent.

When thinking of what to teach or where to invest our time, we look for
"bootstrapping" effects that come from using powerful, universally available,
and extensible software. The command line, for example, useful at first for
file management and operating system exploration, later becomes an important
resource for remote server administration, web design, and data science. Skills
learned in the command line transfer to physical computing, fabrication, web
scraping, and text analysis. Learning about relative and absolute paths
locally, eventually helps to explain internet infrastructure, domain names, and
resource allocation. It leads to Secure Shell and Pretty Good Privacy (PGP),
both used by activists and journalists to protect their communications from
surveillance.

It may be appealing at first to hide computational complexity behind "simple"
visual interfaces. Yet, these interfaces do not share a common visual language
and they do not transfer well across software platforms. Our colleagues in
computer science sometimes worry[^ln-observe] that introducing command line
interfaces and raw coding environments may serve to alienate humanists. We
believe that limited, "dumbed-down" interfaces do even more harm. They further
alienate an audience that already feels removed from the material contexts of
their daily knowledge production. In building the foundations, we want our
students to spend their time well: to learn tools and skills that can support a
wide variety of activity within diverse cultural contexts. The extra care we
take in explaining the reasoning behind our technological choices works to
motivate the students through any initial difficulties of learning how to code
properly, without artificially hampered and patronizing simplification.

[^ln-observe]: Mention the CS chair observation.

### 1.7 Divide big problems into small, modular components.

Our goals in the classroom go beyond the instrumental. The ability to automate
machines is merely a side effect of programmatic thinking. To learn to think
like a programmer is useful in all contexts: it involves dividing big, complex,
and seemingly intractable problems into small, modular, solvable components.
Making a cake, for example, seems hard. But one can read, write, and follow a
recipe---an exercise that we use in our teaching. Similarly, large projects
from library administration to dissertation writing can benefit from the power
of programmatic thinking.

### 1.8 Keep poking, get help, take notes, comment, annotate, share, remix, and train others.

Finally, and this was noticed by several course observers over the years,
students in the humanities are sometimes curiously hesitant to explore their
machines. In the absence of a tinkering upbringing, they might be worried of
breaking expensive equipment or losing sensitive data. Demystifying the magical
black box and learning some habits that prevent irrevocable loss of data
addresses that fear, encouraging the students to tinker and to explore.
Researchers at the later stages of their career may be particularly reluctant
to ask for help or to express their questions in public. Our teaching approach
therefore encourages shared expertise. We model not being afraid to expose our
own gaps in knowledge. We ask students to keep copious notes, to annotate their
code, to share and improve on each other's work. Notes grow into tutorials,
tutorials into courses and workshops. Eventually, in following these
principles, we hope for our students to become catalysts of change in their own
communities of practice.

## 2 Digital Humanities Core

Programming can involve long stretches of frustration (Why does this not work?)
punctuated by short bursts of elation that comes with accomplishing something
difficult (It works!). Rather than viewing their initial lack of results as
failure, we attempt to channel feelings of hindrance into a sense of problem
solving and discovery, related to similarly difficult, but more familiar to our
students tasks of archival research and long-form analytical writing. Just like
writing, coding skills fall on a spectrum of proficiency that constitutes a
small, but foundational part, of a larger variegated skill set.

Depending on one's research interests and career path, a DH practitioner will
have some mixture of the following core skills (with examples in parenthesis):

- Text markup (plain text, *Markdown*, *Pandoc*, *TEI*)
- POSIX command line proficiency (*Bash*, regular expressions)
- Content management (*Jekyll*, *Wordpress*)
- Version control (*Git*, *GitHub*)
- Programming language (*Python*, *R*, *JavaScript*)
- Networking (SSH, VPN, hosting)
- Security (PGP)
- System administration (*AWS*, *Linux*, *Apache*, *MySql*)
- Project management (*GitHub Issues*, *BaseCamp*)
- Probability, statistics, algorithms

Computational practice in the humanities begins with text. Whatever our home
discipline, we are all involved in the reading and writing of texts. It is
natural then to commence training with textual transformations: to understand
how text is produced and where it resides physically, on the machine. Learning
to author in a mark up language like HTML or Markdown is often a first step
into the world of critical computing. Text transformations lead to the
operating system and the file hierarchy. Tasks like regular backups and desktop
organization can be used to familiarize the student with foundational concepts
like relative and absolute file paths, or the distinction between plain text
and binary formats. The idea of starting with daily computation also suggests
covering version control and content management early in the curriculum.
Although not an easy subject, version control comes naturally to a community
used to thinking about drafts, manuscripts, and revisions. Increasingly,
version control systems can also serve to host websites, to stream data, and to
create full-blown publishing platforms. For example, *The Programming
Historian* journal uses *Jekyll*, a static website generator, and GitHub Pages
for publishing and distribution. Using that model to create personal academic
profiles, image galleries, or critical editions is another good way to engage
the humanities community. Git has the additional benefit of encouraging
students to take notes and to journal alongside their work. Similar to the
scientist's lab notebook, the Git journal fixes the flow of ideas and labor,
helping teams keep track of work and attribution.

A programming language occupies a central place in computational practice. All
forms of digitality pass through some form of encoding and automation. Only a
small step separates text transformations, command line shells, and content
management systems from a Turing-complete programming language. We often
"trick" our students into programming by automating simple tasks like word
substitution from the command line. The same task could then be repeated using
*Python* or *R*, reinforcing skills learned earlier in the process. Because the
internet plays such a key role in transforming academic practice, knowing the
basics of networking: infrastructure, routing, packet switching, protocols,
security, encryption are also key to higher level activity like preserving free
speech online, protecting a journalist's sources, or bypassing censorship
filters. The care and maintenance of personal document archives---research
papers, article drafts, and book manuscripts---grows into server management.
The server is where many of the skills learned earlier come to fruition. The
running of websites requires a long "stack" of technological components. These
are almost impossible to use well without knowledge of the command line, a
programming language, and computer networks.

No project is complete without some sense of planning and organization. Project
management is an important part of computation in the private sector, and, an
increasingly formalized part of software engineering.  Projects fail and
succeed by the measure of their ability to coordinate action across time zones
and continents. When teaching programming, we ask our students to start with
"scoping" their projects in plain English first, then to transform these
technical specifications into pseudocode, which then serves as the basis for
program design and architecture. We ask our students to submit these documents
along with code and consider them as important as a functioning program.

Finally, programming fundamentally involves a measure of algorithmic thinking.
On some abstract level, the specific languages, tools, and implementations are
secondary to the logical structures that support all higher level activity.
This may be the most difficult obstacle to tackle. Every word cloud, every
topic model, and network visualization tool hides a number of assumptions
driven by sophisticated logic that comes from the fields of statistics and
computer science. Without training in the methods we are bound to remain mere
consumers of technology. Critical computing practice, like critical thought,
requires a measure of logical and mathematical literacy.

We do not mean for this list to represent a comprehensive statement about
computation in the humanities. Rather, we would argue that most projects,
however large or small, employ at least *some* aspects from most of the above
categories. Their ubiquity is what classifies them as "core" or "foundational"
competencies. Few people apart from professional computer scientists and
software engineers would claim mastery over the full stack of what is mentioned
here. It is much more likely for digital humanists to develop proficiency in
one or several areas of practice. Yet any one of the above foundational
competencies have "spillover" effects in "leveling up" the rest of the list.
Our intensive, week-long class can only begin to address a small part of the
larger, complicated puzzle.

## 3 Bash and Python

### 3.0 Why Bash?

    core skill
    simple
    powerful
    lasting
    universal
    hackable
    fun


> Bash is the GNU Project's shell. Bash is the Bourne Again SHell. Bash is an
sh-compatible shell that incorporates useful features from the Korn shell (ksh)
and C shell (csh). It is intended to conform to the IEEE POSIX P1003.2/ISO
9945.2 Shell and Tools standard. It offers functional improvements over sh for
both programming and interactive use. In addition, most sh scripts can be run
by Bash without modification.1

http://www.gnu.org/software/bash/

### 3.1 Why Python?

What is a programming language?

control structures + data types + built-in functions + syntax + interpreter
Why Python

    core skill
    simple
    powerful
    lasting
    universal
    hackable
    fun

### When to use them?

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
