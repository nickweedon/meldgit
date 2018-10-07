MeldGit
=======
Very simple wrapper script that can be used to run meld when using git via Cygiwn.
The only useful thing this script does is automatically convert each cygwin path passed to it, to the equivalent Windows path which meld expects.

To set this up with git, add the script to your path, install Windows Meld and then add this to you ~/.gitconfig file under cygwin:
```INI
[diff]
  tool = meld
  guitool = meld

[difftool]
  prompt = false

[difftool "meld"]
  cmd = meldgit.py --local "$LOCAL" --remote "$REMOTE"
```
