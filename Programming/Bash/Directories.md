# Changing Directory
If we want the directory stay as where the shell script finishes we need to run the script in the same process as the terminal.

To change directory while running a shell script, we have to use `source`/`.` command when executing the script.
So that it will run in the same process as the parent shell.
```
$ source ./script.sh
$ . ./script.sh
```

# ~ in Variables
Do Not Use ~ to represent home path.
Sometime it will not expanded and the path will become invalid.

Use `$HOME` instead whenever a home directory is needed
```
FOO=~/bar        # stores /home/wolf/bar
FOO="~/bar"      # stores ~/bar (invalid)
FOO=$HOME/bar    # stores /home/wolf/bar
FOO="$HOME/bar"  # stores /home/wolf/bar
```