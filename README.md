I'm trying to get used to Python, this is the first re-usable project.

This script will get the Linx/OSX Terminal size and then "draws" a border around an defined text. I also has Options to center, adjust left, or adjust right the text.

This is script is used for me in OSX as auto-exec script when I open a Terminal window.

To do the same, goto Terminal > Preferences > Profile > Shell and enter the following in the "execute command" textfield:
```sh
  if [ -f FILEPATH ]; then python FILEPATH; fi
```
Of course, replace `FILEPATH`with your path to the script.
