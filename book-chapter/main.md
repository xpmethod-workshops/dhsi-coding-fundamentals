---
title: "Computing Foundations for Human(s|ists)"
authors:
- Dennis Tenen
- John Simpson
---

We write this chapter in reflection of teaching **Computing Foundations for
Human Human(s|ists)** at Digital Humanities Summer Institute at University of
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




[^ln-courselink]: An archived version of the course can be accessed at
http://web.archive.org/web/20150614161609/https://github.com/denten-workshops/dhsi-coding-fundamentals/blob/master/README.md

No black boxes!

Use few, small, simple, universal, and powerful tools that you can hack and
understand.

Wherever possible store data in human-readable text streams.

Do it right. Doing it badly accumulates intellectual, technological, and
ethical debt.

If you have to do something more than once a hundred times,† automate.

Divide big problems into small, modular components.

Bootstrap and time well spent.‡

Keep poking, get help, take notes, comment, annotate, share, remix, and train
others.

This chapter is intended for humanities-based researchers with no programming
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
