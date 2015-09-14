#!/bin/bash
# This script saves time when constructing complex pandoc incantations
#
# USUAGE:
#           sh print.sh [-p | -d] filename.md
#
#           -p to produce .pdf
#           -d for .docx

## pass the file name as an argument
if [ $# -eq 0 ]
then
        echo "pass the file name"
        exit
fi

source=$2

# Use parameter expansion to strip the name
target="${source%%.*}"

# handle two options with getopts: -d for .docx and -p for .pdf

while getopts ":d:p:m:" opt; do
  case $opt in
    d)
      echo "printing $target.docx to print-plates/" >&2
      pandoc --filter pandoc-citeproc --csl csl/mla-note.csl -So \
          print-plates/"$target".docx "$source"
      ;;
    p)
      echo "printing $target.pdf to print-plates/" >&2
      pandoc --latex-engine=xelatex --filter pandoc-citeproc --csl \
          csl/mla-note.csl -So print-plates/"$target".pdf "$source"
      ;;
    m)
      echo "printing $target.md to print-plates/" >&2
      pandoc "$source" -f markdown -t markdown+hard_line_breaks -So \
          print-plates/"$target".md
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      ;;
  esac
done

