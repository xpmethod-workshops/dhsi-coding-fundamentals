---
title: "Critical Computing in the Humanities"
authors:
- Phillip R. Polefrone
- John Simpson
- Dennis Tenen
bibliography: main.bib

---

We write this chapter as a general reflection on teaching computing
fundamentals in the humanities context, and more specifically in the wake of
teaching *Computing Foundations for Human(s|ists)* at the Digital Humanities
Summer Institute (DHSI), University of Victoria and *Computing in Context* at
Columbia University.[^ln-titlelink] These courses were intended for humanities
researchers with no previous programming experience who wanted to learn how
programs work by writing a few simple, useful programs of their
own.[^ln-courselink] The syllabus was designed to foster a type of "digital
literacy" that goes beyond using prepackaged tools and software and into the
foundational skills that can support further self-guided exploration and
intellectual growth.

To these ends, the topics covered in our classes included working with files
and folders, advanced searching through large collections of texts,
algorithmic thinking, data manipulation, and text analysis. The tools we use
are few and simple: the command line interface included in most modern
computers, the ubiquitous and powerful Python programming language, and a text
editor. By the end of course, our students worked on their own and in small
groups to create a small web scraper, an "essay grader," a comma-separated
value file manipulator, and a program that evaluates poetry based on its
measure of similarity to Byron.

Our aim in this chapter is not to recapitulate the experience of teaching, but
to reveal some of the core principles that went into making the courses: to
talk about the rationale behind our teaching philosophy, and, more broadly, to
suggest an approach to teaching programming in the humanities.

We will elaborate on the above principles in three sections. "Critical
Computing in the Humanities" describes the ideas behind our approach to
computation, which is premised on extending rather than replacing
long-standing critical practices of humanistic inquiry. In the second section,
"Digital Humanities Core," these ideas lead us to a list of core skills for
the practicing digital humanist. These are meant to be neither totalizing nor
exhaustive. Rather, we outline several necessary prerequisites needed to
advance the great variety of work in the field. We conclude with a section
that details the "Three Locations of Computing," which orient the reader to
three significant sites of computation: the command line, the text editor, and
the programming language interpreter.

Ultimately, our essay gives the authors' unified take on the skills and
competencies required to advance research in the digital humanities and
computational culture studies. The outlined program should be used as a
guideline, not dogma. We hope it contributes to the broader conversation about
curricular development, certification, and student and faculty training.

[^ln-titlelink]: "Human(s|ists)" is actually a regular expression, a way to
search text for specified patterns. In this case it picks out anything starting
with "Human" and ending in *either* "s" or "ists". So, it acts as a stand-in
for both "Humans" and "Humanists".

[^ln-courselink]: An archived version of the DHSI course can be accessed at
http://web.archive.org/web/20150614161609/https://github.com/denten-workshops/dhsi-coding-fundamentals/blob/master/README.md

## 1 Critical Computing in the Humanities

Computational methodologies can complement the rich history of research in the
humanities. But to take hold, quantitative approaches to the study of culture
must be adapted to more closely align to extant ideals and practices. Inspired
by a number of initiatives advancing a similar philosophy, we refer to this
approach as "critical computing."[^ln-first] The following seven propositions
will connect technological preferences with values intrinsic to humanistic
inquiry:

1. Demystify everyday computation.

2. Use few, free, small, universal, and powerful tools that you can
alter and understand.

3. Privilege simplicity and human legibility over complexity and machine
efficiency.

4. Invest in technologies that align with the values of our community.

5. Identify research objectives prior to selecting the appropriate tools and
methodologies.

6. Divide big problems into small, modular components.

7. Be "lazy" by automating mundane tasks, but do it right by commenting your
code, taking notes, and sharing with others.

[^ln-first]: We are not the first nor the only instructors to think about
digital pedagogy this way, nor are we the only ones to be offering a course
based on these principles.  Software Carpentry, for example, has been
advocating a similar approach since its inception. Similarly, the *Programming
Historian* is "an online, open-access, peer-reviewed suite of tutorials that
help humanists learn a wide range of digital tools, techniques, and workflows
to facilitate their research." See also @harrell_toward_2015.

### 1.1 Demystify everyday computation

Contemporary computational devices are a foundation of daily life. They are
involved in everything from financial markets, to archival research, to the
way many keep in touch with friends and family. Yet for those without
technical training, the inner workings of these devices remain a source of
mystery and, consequently, frustration. Recognizing this, our courses target
the underlying structure of tools that many rely on for their daily
computation, teaching our students how these tools work (and not just how to
use them). Beyond the principles of programming, we want our students to
understand the basics of networking, system administration, and project
management. By revealing the innards of opaque computational "black boxes," we
hope to empower our students to take control of their everyday digital
practice.

The most universal daily computing task of the humanities, regardless of
research interest, is writing. For this reason, we structure our early classes
by creating small "experiments" that address our students' own writing habits.
Such exercises might include a lab session in which students analyze their own
documents for commonly overused "weasel words,"[^ln-weasel] for example.
Working with one's own documents introduces important technical
concepts---like "relative" and "absolute" paths, file formats, character
encoding, and small shell utilities like `grep` (used to search through text
files), `wc` (word count), or `sed` (stream editor for text
transformation)---that can later be extended into more advanced concepts in
data manipulation or natural language processing. Short text-manipulation
exercises form the students' first programs, performing tasks like "safely
rename all the files in this folder according to such-and-such rule," or "keep
a daily log of my writing progress."

[^ln-weasel]: Weasel words are words that sound very meaningful, but diminish
instead of adding to the impact of persuasive writing. The "very" in the
previous sentence, for example, is a weasel word.

### 1.2 Use few, free, small, universal, and powerful tools that you can alter and understand.

Researchers, librarians, students, and faculty are faced with a bewildering
array of software choices. In deciding whether to invest time and resources
into learning a new tool or methodology, we are inspired by the free software
movement in general and the Unix operating system philosophy in particular.
The Unix philosophy of computing prioritizes small, modular pieces of software
that "do one thing well" [@mcilroy_unix_1978]. Such software can then be
chained together with other small but powerful tools to achieve complex
results. Free software, besides being cost effective ("free as in beer"), also
makes the tool itself available to inspection, interpretation, revision, and
ultimately critique. Transparency and the ability to modify code to suit one's
own needs is what makes code "free free as in speech" [@stallman_why_2007].
Above all, we seek out universal tools that we can understand and, where
needed, customize to fit our own particular applications. These tools can be
applied in diverse contexts like library infrastructure, web design, data
science, and the production of critical editions.

When thinking of what to teach or where to invest our time, we look for
"bootstrapping" effects that come from using powerful, universally available,
and extensible software. In other words, we privilege skills and concepts that
will have the highest impact in the long run by transferring to the greatest
number of contexts or tasks. The command line, for example, useful at first to
manage files, later becomes an important resource for data gathering, cleanup,
and analysis. Learning about relative and absolute paths locally makes it
easier to understand networking protocols and uniform resource locators
(URLs). It leads to the ability to administer servers remotely and to encrypt
one's communications---skills needed for journalists, activists, librarians,
and scholars alike.

### 1.3 Privilege simplicity and human legibility over complexity and machine efficiency.

Whenever possible we privilege simplicity and human legibility over complexity
and machine performance. The tools and file formats that we use in our
research and archival efforts have serious implications for the long-term
health of the academic ecosystem. The ubiquitous use of Microsoft Word and
Adobe Acrobat file formats, for example, makes it difficult to publish, store,
and to gather insight even from our own published work. As humanists begin to
adopt the use of complex tools and databases, needless complexity becomes even
more of a barrier to knowledge sharing.

Simplicity should not be confused with simple-mindedness. As with clarity in
writing, clarity in computation comes from painstaking mastery of method and
technique. Such mastery is fundamentally difficult, but it is to be preferred
to shortcuts that sacrifice clarity for illusory "ease" of use. The student
just entering the field of digital humanities and computational culture
studies faces the choice of learning to program machines universally, or
learning multiple, fragmentary, and non-standardized tools that have limited
salience outside of the classroom. The proliferation of tools that obscure
fundamental concepts as to avoid "scaring" beginners adds complexity in the
long run. Opaque and artificially hampered tools disempower an audience
otherwise eager to take on new intellectual challenges. Their use prevents us
from communicating with other computationally-minded disciplines and from
competing meaningfully in the wider job market.

### 1.4 Invest in technologies that align with the values of our community.

The non-transparent nature of many popular file tools and file storage formats
extracts a heavy toll on our community. Each tool that we add to our "tool
chain" increases the cognitive burden of training, support, and peer review.

It may be appealing at first to hide computational internals behind "simple"
visual interfaces. Yet these interfaces do not share a common visual language;
the labor of learning one interface therefore does not not transfer well
across other software platforms. Our colleagues in computer science sometimes
worry that introducing command line interfaces and raw coding environments may
alienate humanists. We believe that limited, "dumbed-down" interfaces do even
more harm, further mystifying computing to an audience that already feels
removed from the material contexts of their daily knowledge production. In
building the foundations, we want our students to spend their time well: to
learn tools and skills that can support a wide variety of activity within
diverse cultural contexts. The extra care we take in explaining the reasoning
behind our technological choices can motivate the students through any initial
difficulties of learning how to code "the hard way," without shortcuts or
artificial limitations.

In considering new tools and methodologies humanists who rarely work with
truly large data would to well to weigh the risk of rapid obsolescence of
closed systems against any hypothetical gains in speed or performance offered
by a new note-taking platform, database system, or a proprietary text
editor.[^ln-plain] When selecting a tool or a data format for storage, we ask:
Does it need special software to render? How long has it been around?  Does
the community that support it align with our values? Our choice of the Python
programming language, for example, was guided by the fact that Python encodes
simplify and human readability into technical specifications.[^ln-pep] It has
broad support from the scientific computing community and in the private
sector. It is administered by a non-profit organization, which has articulated
a clear diversity statement, has elected a trans woman to its board of
directors in 2015, and routinely sponsors efforts, like PyLadies and
PyCaribbean, which increase participation from publics traditionally
underrepresented in the technology sector.

[^ln-pep]: Python Enhancement Proposal 20 reads: "Simple is better than
complex. Complex is better than complicated Sparse is better than dense.
Readability counts.

[^ln-plain]: The Unix philosophy privileges inputs and outputs in plain text
format, which can be used to store everything from personal notes, to article
drafts, to huge datasets of metadata. Unix provides many powerful utilities
that work with plain text. In fact, the notion of human readability is even
encoded at the operating system level.

### 1.5 Identify research objectives prior to selecting the appropriate tools and methodologies.

Because the tools that we teach are universal, we are able to better tailor
our courses to the diverse needs of our students. In formulating their
research objectives, beginners often make the mistake of starting with the
tool. In this way someone may describe their interests as "using topic
modeling on a corpus of nineteenth century literature." To this we reply: To
what ends?  Clearly articulated research objectives suggest appropriate tool
and methodologies, and not the other way around. Thus the question of "genre
formation in the ninetieth century," for example, is what could lead to the
use of topic modeling, where the study of narrative would perhaps be better
served by other means, like event detection or automatic plot summarization.
Our goal therefore is to give the students a glimpse of a rich and variegated
toolkit that could help advance a variety of research objectives.

### 1.6 Divide big problems into small, modular components.

Our goals in the classroom go beyond the instrumental. The ability to automate
machines is merely a side effect of algorithmic, analytical thinking. To learn
to think like a programmer is useful in many contexts: it involves dividing
big, complex, and seemingly intractable problems into small, modular, solvable
components. Writing a grant proposal, for example, a book, or a dissertation
may initially seem like a daunting and onerous task. Progress can be made once
it is divided into small, doable steps, as though it were a recipe for making
a cake (an exercise we use in the classroom). Our coding exercises therefore
often begin by having our students describe their research objectives, step by
step, in language natural to them and to their task.

### 1.7 Be "lazy" by automating mundane tasks, but do it right by commenting your code, taking notes, and sharing with others.

Pseudocode in plain English becomes the basis for well documented programs and
readable code. Modular and well documented code does a service to the
community: it is a pleasure to maintain and it communicates the purpose of the
program clearly. It teaches others just as it allows them to further adept the
codebase to suit their own needs, to further share and to remix.

Good programmers are lazy in the right way. After doing a task more than a few
times, a programmer's intuition will be to automate the task. For example, we
often use the `rsync` command to back up our documents; however, after a few
months of running it manually, we can delegate that task to the built-in
scheduler called `cron`. Similar strategies can be used to improve
bibliographic management, manuscript preparation, and research and editorial
workflows.[^ln-caleb]

Although programmers are lazy, they are lazy in the right way. Doing things
badly or in a haphazard fashion accumulates technological, intellectual, and
eventually an ethical debt owed to ourselves and to our peers. Code comments
(or the lack of them) are a common site of egregious laziness: it is easy to
skip documenting your code or to document insufficiently. It just works, one
might say, why bother? However, a piece of code that makes perfect sense today
may seem impenetrable tomorrow. Without comments code becomes difficult to
alter and to maintain. For these reasons we advise our students against simply
cutting and pasting code snippets from our (or anyone else's) tutorials. We
want them to think independently, to annotate, and to review their notes. In
the broader academic context, lazy practices are unethical because they "bank"
against the labor of others in the future. They make research more difficult
to share and to replicate.

<!---
JS: Mention the CS chair observation?
DT: I don't think we should mention his name. But perhaps a footnote, if you
can find a way to phrase it.
--->

[^ln-caleb]: The public GitHub code repository of W. Caleb McDaniel, a
historian at Rice University, is exemplary in this regard.

## 2 Digital Humanities Core

Programming can involve long stretches of frustration ("Why does this not
work?") punctuated by the short bursts of elation that come with accomplishing
something difficult ("It works!"). Rather than allowing students to view their
initial lack of results as failures, we attempt to channel feelings of
hindrance into a discipline of problem solving and discovery. The "difficulty"
of coding can be made more productive when related to the analogous and more
familiar challenges associated with archival research, academic writing, and
foreign language acquisition. Understood in such a broader context, coding
constitutes a small but foundational part of a larger, variegated academic
skill set.

Depending on one's research interests and career path, a DH practitioner will
need to acquire a subset of the following core skills (with examples of
particular technologies in parenthesis):

- Text markup (plain text, *Markdown*, *Pandoc*, *TEI*)
- Command line interface proficiency (*Bash*, pipes, regular expressions)
- Content management (*Jekyll*, *Wordpress*)
- Version control (*Git*, *GitHub*)
- Programming language (*Python*, *R*, *JavaScript*)
- Networking (cloud computing, Virtual Private Networks)
- Security (Pretty Good Privacy, Secure Socket Shell)
- System administration (*Linux*, *Apache*, *MySql*)
- Project management (*GitHub Issues*, *BaseCamp*)
- Design (data visualization, typography, user experience)
- Probability, statistics, and algorithms

We do not mean for this list to represent a comprehensive statement about
computation in the humanities. Rather, we would argue that most projects,
however large or small, employ at least *some* aspects from the above "dream
list." The ubiquity of these modular components is what classifies them as
"core" or "foundational" competencies. Few people *including* computer
scientists and software engineers would claim mastery over the full range of
skills we have represented above. Rather, individual practitioners are likely
to develop proficiency in one or several areas of expertise. An expert in
digital publishing for example will have drastically different requirements
from someone interested in geographic information systems or computational
methods.

Critical computing in the humanities begins with text. Whatever our home
discipline, we are all involved in the reading and writing of texts. Text
gives us intrinsic motivation to explore our own computer environments: to
understand how documents are produced and where they reside physically within
the machine. Learning to author documents in a markup language like HTML or
Markdown naturally leads to more advanced topics like the basics of operating
systems, file system hierarchy standards, and version control. Mundane but
necessary academic skills like regular file backup, bibliographic management,
and the organization of research materials, can be used to familiarize
students with foundational concepts like relative and absolute file paths or
the distinction between plain text and binary formats.

The core principle of demystifying everyday computation leads to the topic of
content management and version control early in the curriculum. Although not
an simple subject, version control comes naturally to a community used to
thinking about drafts, manuscripts, and revisions. Increasingly, version
control systems are used to host websites, share data, and to publish. For
example, the editors of *The Programming Historian* use GitHub, a version
control system, to publish and to distribute their journal. The team behind
*Project Gitenberg* "leverages the power of the Git version control system and
the collaborative potential of Github to make books more open." As of 2015,
*Gitenberg* hosts more than 43,000 books. Using a similar model to create
personal academic profiles, compile image galleries, or edit critical
editions, our students learn while experimenting with aspects of academic
production directly relevant to their careers. Furthermore, version control
systems improve the quality of academic collaboration. Git and similar tools
act as powerful research notebooks. They encourage all researchers involved to
keep meticulous notes, which make it possible to document the flow ideas and
labor and to attribute work fairly. For these reason we encourage the use
version control early on and expect such systems to play an increasing role in
academic evaluation.

A programming language occupies a central place in computational practice. All
forms of digitality pass through some form of encoding and automation. Only a
small step separates text manipulation at the command line using simple shell
scripts from more advanced research-oriented programming languages like
*Python*, *R*, and *Haskell*. We often "trick" our students into programming
by automating simple tasks like word counting and file management at the
command line. Thus small tasks like "create a directory," "move a file,"
"count all words in this directory" can eventually grow into text analysis.

Because the internet plays such a key role in transforming academic practice,
knowing the basics of networking---infrastructure, routing, packet switching,
protocols, security, and encryption---is also key to pursuing higher-level
goals like preserving free speech online, protecting a journalist's sources,
or bypassing censorship filters, particularly in places where politics and
geography impinge on intellectual freedom. The care and maintenance of
personal document archives---research papers, article drafts, and book
manuscripts---naturally leads into server management. The server is where many
of the skills learned earlier come to fruition. Running websites requires a
long "stack" of technological components. Advanced technologies "in the stack"
like the Apache HTTP server, MySQL relational database management system, and
the PHP programming language are difficult (if not impossible) to master
without prior knowledge of the command line, networking, and programming
fundamentals.

No project is complete without some sense of planning and organization.
Project management is an important part of computation in the private sector,
and it is an increasingly formalized part of software engineering. Projects
succeed and fail by the measure of their ability to coordinate action across
differences in time, temperament, and geography. When teaching programming, we
ask our students to start with "scoping" their projects in plain English
first, then to transform these technical specifications into pseudocode, which
finally serves as the basis for program design and architecture. We ask our
students to submit these documents along with code and consider them an
essential part of the project's output. In addition to getting better results,
attention to project management prepares our students for working in groups
outside of academia.

Because computational projects in the digital humanities often involve the
creation of public-facing tools and archives, they necessarily overlap with
the fields of data visualization, and graphic, user interface, and user
experience design. Johanna Drucker has been a powerful voice in urging our
community to encounter design both in practice and as an object of study
[CITE]. The disciplines of human-computer interaction and human factor
engineering hold exciting possibilities for a productive collaboration between
schools of engineering and the humanities.

Finally, programming fundamentally involves a measure of algorithmic thought
and statistical reasoning. Without logic there can be no computation.
Ultimately, the art of programming involves the ability to think
algorithmically, to atomize complexity into discrete programmable steps, to
formalize intuition, and to build models. Logic and statistical reasoning
underlie every word cloud, every topic model, and every network visualization
tool. Critical computing practice, like critical thought, requires access to
deep structure. Those who aspire to become active and equal participants in
the formation of computational knowledge (rather than mere passive recipients
of tools and methodologies developed elsewhere) must at some point confront
the established standards for training required for quantitative work in any
field.

An intensive, week-long class, like the one that we teach at DHSI, can only
begin to address a small portion of the skills required to run a successful
project in the digital humanities. A diverse team of practitioners with
complementary expertise will likely comprise any given digital humanities
project. For this reason, in our teaching, we concentrate on the following
"three locations of computing," which support nearly all aspects of
specialization represented above. Some familiarity with a text editor, the
command line, and a programming language improves general digital literacy,
useful to the librarian, the information scientist, and the computational
humanist alike.

## 3 Three Locations of Computing

We often begin our courses by outlining the above "big picture" principles,
challenges, and considerations. Like learning a foreign language, programming
takes time and patience to master. And as is the case with any difficult
skill, motivation to practice best correlates to chances of long-term success.
Developing the intellectual motivations to stick with the program is therefore
one of our paramount goals. For this reason, we strive to address the common
"frustration points" of everyday computing. In our experience, even simple
tasks like downloading an online file can be rife with anxiety for many
students: Where did that file go? How do I find it again?  What type of file
is it? Is it safe to open it? Modern operating systems conceal the details
needed to make informed decisions from the average user. Practitioners
interested in fields like information science, critical software studies,
platform studies, game theory, or media archeology must learn to extend their
inquiry beyond the available surfaces.

Our task as instructors is to reveal the hidden mechanics of computation.
Moments of apprehension can be turned into opportunities for discovery.
Students, university faculty, and librarians naturally approach documents,
file systems, and datasets as matters of critical importance. Such artifacts
preserve much precious intellectual labor. For this reason, in our experience,
students respond enthusiastically to the mission of reclaiming the material
contexts of their daily intellectual production.

As suggested by the metaphor of the software development "environment," a site
of computation denotes an interface through which humans engage with machines.
A site is also a conceptual space, containing a logic or a grammar of
interaction. We find three such sites in searching for the universal grounds
of general digital literacy: the command line, the language interpreter, and
the text editor.

### 3.1 Command Line Interface

All operations on the level of the operating system are in some sense
performed on files. A new project starts with a new folder, a grant proposal
with a new document. The completion of the project and the submittal of the
grant proposal essentially involve the transmission of files across email
clients and code repositories. The aspiring coder must therefore develop a
firm grasp of the file system topography. The command line presents one of the
oldest and most empowered ways of interacting if the machine. Despite its
retro appearances, the modern command line offers an intuitive, text based,
"call and response" style of machine programming consistent across a
remarkable variety of platforms: from mobile phones to supercomputers. The
power user manipulates files at the command line. Everything from downloading
a sample corpus, to writing a research paper, to debugging code eventually
leads to the command line. We therefore embrace it from the beginning of the
course. It forms the base of our operations.

On the level of hardware the machine "speaks" in binary code. The command line
"interprets" English-like commands (in a language called Unix
Shell)[^ln-shell] into binary. When deleting a file, for example, one
instructs the machine to `rm filename.txt` instead of dragging and dropping it
into the trash folder, as one would using a graphical user interface. Note
that "dropping into the trash folder" merely offers a visual metaphor for the
underlying bitwise operations. The CLI alternative turns the metaphor into a
more exact command `rm`, which stands for "remove." Similarly, to direct the
computer to move a file, we would use the `mv` command. Unlike their visual
and metaphorical counterparts, the Bash commands contain many advanced
options, which are explained in the manual accessible through the `man`
command. In this example, `man mv` displays the manual pages for the move
command.

[^ln-shell]: @bourne_unix_1978

Furthermore, because Bash commands are in themselves a type of a programming
language, they can be chained together and automated to produce complex
behavior. Imagine, for example, writing a book or a dissertation in a directory
that contains several files in plain text format (.txt), each corresponding to a
chapter. The writer can then use the following script to produce the total
word count:

```
wc -w ~/user/documents/book/*txt | tail -n 1 | sed 's/[a-z ]//g' >> log.txt
```

The above "incantation" tells the computer to do four things:


1. Count the words in all of the `.txt` files found in the present directory.

    Input:

    ```
    wc -w *txt
    ```
    Output:

    ```
    11717 1-chapter.txt
    12457 2-chapter.txt
    13780 3-chapter.txt
    10542 3-chapter.txt
    48496 total
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
on to the next one. Once saved to disk, this small script can be set to run
automatically at a predetermined time interval and used to keep a daily log of
one's writing activity.

Learning the command line is not just a matter of opening up new ways of
interacting with files, though. In learning command line basics, students
become familiar with foundational concepts and techniques that will be built
upon in higher-level contexts, in true bootstrapping style. The above exercise
can be used to discuss the difference between relative and absolute file paths
(`~/usr/documents/book/*txt` vs.  `/usr/documents/book/*txt`). It contains the
basics of regular expressions (`[a-z ]`). And because the output of `wc -w` is
a string, the exercise can be used as the basis for string manipulation and,
later, data normalization and rudimentary natural language processing. Finally,
such exercises can lead to the basics of remote server management, networking,
security, and encryption.

### 3.2 Python

The second of our foundational sites of computing is the Python interpreter.
Where the command line "translates" from *Bash* into machine code, the *Python*
interpreter translates from *Python*. *Bash* traces its roots to the late
1970s. It is a domain-specific command language, designed specifically to
interact with the operating system. Its longevity makes it stable and
ubiquitous. *Python* became popular in the early 2000s. Unlike *Bash*, it is a
general-purpose, high-level programming language.

| When to use Bash                  | When to use Python              |
|:----------------------------------|:--------------------------------|
| - automate daily tasks            | - data science                  |
| - manage files & folders          | - app development               |
| - remote server administration    | - natural language processing   |
| - data munging[^ln-munge]         | - data visualization            |
| - quick & dirty text manipulation | - web scraping                  |
|                                   | - corpus analysis               |
|                                   | - everything else               |

We chose *Python* among other excellent choices (like *R* and *Haskell*) for
several reasons. First, *Python* is popular. According to the TIOBE language
popularity index, *Python* holds roughly 3.6% of the market, trailing only
behind *Java* and C-family languages (*C*, *C++*, *C#*)
[@tiobe_software_tiobe_2015]. Although detailed statistics by field are not
available, we infer that in the domain of scientific computing and data science
*Python* holds the majority share of the market. This is important, because it
means that learning *Python* is a good investment of time. It can lead to jobs
outside of academia, and projects using *Python* will have an easier time
hiring outside experts due to the popularity of the language.

*Python*'s popularity has an important side-effect. Being a general-purpose
language, it has been adapted to a wide variety of contexts, from machine
learning to web application development. The larger *Python* framework
consequently offers a rich variety of software libraries and toolkits. Most
tasks needed to perform academic research or library administration have likely
been addressed in an existing library and are available for use. The student
can therefore apply skills learned in one area of research to another, without
loss of expertise or productivity.

Finally, besides being popular and flexible, *Python* is a human-friendly
language. Human-readability is one of its stated aims. the Python Enhancement
Proposal 20 (PEP20), known as the "Zen of Python" reads [@smith_pep_2015]:

```
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
```

We feel that in privileging code legibility, the *Python* philosophy fits well
with the values of humanistic inquiry. The human-friendly readability of the
language on the technical level reflects its possibilities on the social level:
legibility can translate to accessibility across communities and in groups too
often under-represented in programming circles. The Python Software Foundation,
an organization "devoted to advancing open source technology related to the
Python programming language," publishes a diversity statement and maintains a
mailing list devoted to the topic. The community fosters initiatives like
Pyladies, "an international mentorship group with a focus on helping more women
become active participants and leaders in the Python open-source community,"
and the Minorities in Python Conference (held in June 2015, in San Francisco).

[^ln-munge]: Data munging is a recursive computer acronym that stands for
"Munge Until No Good," referring to a series of discrete and potentially
destructive data transformation steps [@raymond_mung_2004].

### 3.3 Text Editor

The humble text editor is the third and possibly most important site of
computing in the digital humanities: in addition to supporting programming, the
right text editor can make useful interventions in the writing process in
general. For this reason, we ask our students to reevaluate their relationship
with consumer-grade tools like Microsoft Word and Google Docs. To write code we
need a *plain text* editor that does not add any hidden formatting characters
to our program instructions. We also need an editor that we can modify and
extend without being hampered by proprietary licenses or restrictions. Many
text editors meet our criteria. Among them are *Atom*, *Emacs*, *Leafpad*,
*Notepad++*, and *Vim*.

Where conversing directly with *Bash* or *Python* interpreters allows for an
"interactive," back-and-forth style of programming, the text editor gives a
measure of permanence to the conversation. When working with data sets we often
begin with exploratory data analysis at the command line, aimed at
familiarizing ourselves with the data and at forming intuitions about its
explanatory potential. Once those intuitions are formed, we can move to writing
and debugging code in the text editor that will test those intuitions against
the dataset as a whole. The Python interpreter remains open in the background
to test individual lines of code before they make it into our program, but the
text editor makes these projects portable, durable, and scalable.

About halfway through the session, the students are ready to formulate a
project of their own. Rather than using prepackaged exercises, we encourage our
students to formulate small research projects related to their own work or
research.  In our last class, a group of librarians built a program to copy
selected metadata from one `.csv` file to another while checking for errors in
data formatting (like a properly formatted date, for example). Another group
built an automatic essay grader. Yet another analyzed poetry for its similarity
to Byron. A fourth group wrote a script that automates the downloading of a
film script corpus.

All of these projects begin with a set of step-by-step instructions in English.
Thus, a simple essay grader may be expressed as follows:

1. Open and read a file.
2. Calculate variation of sentence lengths.
3. Assign a score based on variation.
4. Calculate a measure of linguistic variety.
5. Assign a vocabulary score.
6. Find common spelling mistakes and "weasel words" that are a sign of weak
writing.
7. Average the scores to come up with a total grade.

In this way, students work alone or in groups to define the scope of their
program. Beginning with this step also institutes another type of code
legibility, the legibility of value-driven heuristics. In another recent course
at Columbia University, students building an automatic essay-grader had to
explain and defend the basis of their grading criteria. In doing so, they
revealed their own values as writers and initiated a spirited debate about
algorithmic judgments of clarity and style. Some students focused on limiting
sentence length while others privileged linguistic variety. Other students
unabashedly established their metrics based on their own stylistic traits,
assuming that they would be implicitly doing so anyway. Revealing the basis of
these judgments in the classroom can spur discussion, but it also facilitates
transparency in the final program.

When the scope and logic of the program have been determined, we work with
individual groups to help translate the English-language heuristic into
workable Python code. Inevitably, the programs grow more sophisticated. In the
above example, students used published work to test their grading algorithm. In
a longer course, we may have introduced supervised learning techniques to
classify essays for quality based on similarity to work that has already been
evaluated.The difficulty of the project may be tailored to the length of the
course and the level of individual expertise. During such free-form
"laboratory" sessions we encourage students to help each other and to share
expertise with their peers.

The command line, the Python interpreter, and the text editor provide the
foundations of critical computing in the humanities. We do not expect all of
our students to become programmers. But at the very least, they become exposed
to a powerful problem-solving method and to operating system internals used
widely in all aspects of computation, from sending email to writing a
paper.[^ln-coauthor]

## Further Reading

- @kernighan_d_2011
- @janssens_data_2014
- [DH Notes](https://github.com/denten/dhnotes/wiki)
- @manning_foundations_1999
- @bird_natural_2009
- @petzold_code:_2000
- @chacon_pro_2014
- [Project Jupyter](https://github.com/jupyter)
- [PyLadies](https://github.com/pyladies)
- [Python Software Foundation](https://www.python.org/psf/)
- [The Programming Historian](http://http://programminghistorian.org)
- @dawney_think_2015

[^ln-coauthor]: A detailed history of author contributions can be found on our
GitHub page at
[https://github.com/denten-workshops/dhsi-coding-fundamentals/commits/master/book-chapter/main.md](https://github.com/denten-workshops/dhsi-coding-fundamentals/commits/master/book-chapter/main.md)

