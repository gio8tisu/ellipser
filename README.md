# Python Ellipser
Limits the width of each line in FILE(s) to MAX_LEN without cutting in the middle of a word.
If a line exceeds a given number of characters, the line is ellipsed
(cut and \[...\] is appended).

This is a simple example of a Python project.

## `ellipser` CLI
The `ellipser` executable reads files or standard input and outputs ellipsed lines.
Examples:
```bash
cat <FILE> | ellipser
```
```bash
cat <FILE1> | ellipser - <FILE2>
```
```bash
ellipser <FILE1> <FILE2>
```

## `EllipsisFormatter` class
This class is defined inside the `ellipsis.py` module.
It only defines one method: `format(str)`.

This method receives a string and cuts it trying not to cut in the middle of a word.
If the resulting cut is too short (for example a very long word), it will cut in the middle of a word.
