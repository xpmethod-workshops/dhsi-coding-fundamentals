---
title: "Computing Foundations for Human(s|ists)"
authors:
- Dennis Tenen
- John Simpson

---

We write this chapter in reflection of teaching **Computing Foundations for
Human Human(s|ists)** at the Digital Humanities Summer Institute, University of
Victoria. This week-long course was intended for humanities-based researchers
with no previous programming experience, and, as we wrote in the course
description, for those who would like to understand how programs work by
writing a few simple, but useful programs of their own.[^ln-courselink] The
topics covered included working with files and folders at the command line,
text stream manipulation with Bash Unix Shell, regular expressions, along with
Python basics like native data types, variables, functions, and control
structures. At the end of the course our students worked on their own and in
small groups to create a small web scraper, an "essay grader," a comma
separated value file manipulator, and a program that evaluated poetry for its
measure of similarity to Byron.

Our aim in this chapter is not so much to recreate that experience (we would
not have the space to do it here, in any case) but to reveal some of the ideas
that went into making the course, to talk about the rationale behind our
teaching philosophy, and, more broadly, to suggest an approach of teaching
programming in the humanities environment.

## Critical Computing in the Humanities

It is our firm belief that the teaching of computational principles in the
humanities must happen in context: that is, grounded in the practice of
humanities-based research and answering to the values held by the academic
community.  We call this approach critical computing, which for us involves the
following eight principles:

[^ln-courselink]: An archived version of the course can be accessed at
http://web.archive.org/web/20150614161609/https://github.com/denten-workshops/dhsi-coding-fundamentals/blob/master/README.md

1. No black boxes!

Computers are everywhere. They mediate everything from financial markets, to
archival research, and to the way many keep in touch with their friends and
family. Yet, for those without computational background, these devices remain a
source of mystery, magic, and frustration. Our course begins then with a
process of demystification. We want our students to understand not only the
principles of computer science, but the basics of software and electrical
engineering. As much as possible, we would like to reveal the innards of opaque
computational "black boxes," empowering our students to take control of their
everyday computational practice.

2. Use few, free, small, simple, universal, and powerful tools that you can
hack and understand.

Librarians, students, and faculty are faced with a bewildering array of
software choices. Companies that promise "innovation" and "disruption" in the
classroom routinely approach administrators with offers to try and to buy
software at the institutional level. The imbalance of information between the
vendors and the users, often results it wasted time and resources. In making
the decision to invest time and resources into our own computational practice,
we are inspired by the philosophy embodies by the *\*nix* family of operating
systems (Unix, Linux, Arch Linux, OpenBSD, and others). The *\*nix* community
has been advocating for the use of free (as in speech and as in beer) and open
source software (FOSS). FOSS software works in the academic humanities context
because the free and open access code is available for inspection, and
therefore, for interpretation, critique, and modification.

This means people and institutions can Furthermore, the *\*nix* philosophy
privileges small, modular pieces of software that "do one thing and do it
well." Such software can then be stringed together with other small but
powerful tools to achieve complex results. Throughout, we seek to avoid
proprietary file formats, non-standard interfaces, and vendor lock-in.
Simplicity, maintenance, and longevity are key for creating a culture that
lasts. The preference for openness and simplicity is not mere ideology. In the
last several decades, following the same principles, *\*nix* family of
operating systems has become the dominant platform that powers everything from
cellular phones, to robots, drones, personal computers, and super clusters.
This also means that our investment of time into such ubiquitous interfaces
scales across time and devices. In helping us decide what to use and to teach,
we seek out universal tools that underlie a variety of computing practices,
from library infrastructure, to web design, to data science and
critical-edition making.  More than anything, we want to learn tools that we
can understand and, eventually, to extend tailor to suit our own particular
needs.

3. Wherever possible store data in human-readable text streams.

The problem of file formats relates closely to the proliferation of closed
tools and platforms. It is most acutely felt by archivists faced with
preserving short-lived data structures from obsolete platforms from recent
past. For many humanists, who rarely work with truly large datasets or
collections (on the order of millions documents), the real risk of rapid
obsolescence offsets any hypothetical gains in speed or performance offered by
a new note-taking platform or a complex database. Conveniently for us, the Unix
philosophy privileges inputs and outputs in plain text format, which can be
used to store everything from personal notes, to article drafts, to huge
datasets of metadata in comma separated value format. Unix provides many
powerful tools to work with plain text as it encodes the notion of
human-readability at the operating system level. When working with
audio or visual material, we similarly prefer widely-supported non-proprietary
standards. When selecting a data format, we ask: does it need a special
software to render? How long has it been around? and What organization is
responsible for maintaining he standard?

4. If you have to do something more than ~~once~~ a hundred times, automate.

Programmers are lazy. After doing a task more than a few times, a good
programmer's intuition will be to automate the task. For example, we often use
the `rsync` command to back up our documents. However, after a few months of
running it manually, the user can delegate that task to the built-in scheduler
called `cron`. The adage usually holds that if you do it more than *once*,
automate. However, one must know exactly what to automate. When backing up your
files, do you want to back up the whole system or a few select folders? How
often should the backup script run? These questions become apparent after
extensive manual use. T

5. Do it right the first time.

Although programmers are lazy, they are lazy in the right way. Doing things
badly, in a haphazard fashion, accumulates technological, intellectual, and
eventually an ethical debt, to oneself and to the community. Code comments are
the simplest example of this. It is easy to skip documenting one's code. "It
just works, why bother?" However, a piece of code that makes perfect sense
today, becomes obscure tomorrow. Without comments, time needs to be spent to
recreate the reasoning behind the original implementation. As another example,
we advise our students against simply cutting and pasting code snippets from
our tutorials. We want them to follow our thinking, to annotate, and to review
their notes regularly. In the social context, lazy practices are unethical
because they "bank" against the labor of the following generations of scholars.
Doing things the right way now, saves unnecessary effort later.

6. Target daily computation.

Programming classes in the sciences often begin with coding for coding's sake,
targeting an audience inherently interested in logic, math, and engineering.
The humanities must find its own intrinsic motivations for learning to code,
broad enough to appeal to the community at large. For this reason, we begin our
class with exercises that target daily computation and writing practice, common
to researchers at every stage of their development. We create little
"experiments" that target one's writing, for example. These include include a
lab session in which students analyze their own documents for commonly
over-used "weasel words,"[^ln-weasel] for example. Working with one's documents
introduces important concepts like "relative" and "absolute" paths, file
formats, and small shell utilities like `grep` (used to search through text
files), `wc` (word count), `sed` (stream editor for text transformation), that
can later be extended into more advanced concepts in system management or
natural language processing in Python. When put together, these small utilities
form the students' first programs, performing tasks like "safely rename all the
files in this folder according to such-and-such rule," or "keep a daily log of my
progress."

[^ln-weasel]: Weasel words are words that sound very meaningful, but instead of
adding, diminish the impact of persuasive writing. The "very" in the previous
sentence, for example.

8.Bootstrap and time well spent.

When thinking of what to teach or where to invest our time, we look for the
"bootstrapping" effect that comes from using powerful, universally avaialable,
and extensible software. The command line, for example, useful at first for
file management, becomes an important resource for remote server administration
later, used also in physical computing, and in data ma

9. Divide big problems into small, modular components.


Keep poking, get help, take notes, comment, annotate, share, remix, and train
others.
