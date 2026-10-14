## Purpose

## Goals

## Non-goals

## Current behavior
- Eliza chatbot (server/Eliza/commented_eliza.py): loads a script file,
  matches user input against keyword rules, replies, and can switch
  between topic scripts (anxious, anger, depressed, disorder). Runs from
  the terminal only.
- Flask server: one placeholder endpoint, /api/test. Does not use Eliza.
- React client: placeholder homepage. Does not call the server.
- Known issues: test file has unresolved merge conflicts; Layout
  component renders nothing; "depression.txt" reference doesn't match
  the "depressed.txt" file.

## Plan
