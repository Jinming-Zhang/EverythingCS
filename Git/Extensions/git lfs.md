# Git Large File System
`git-lfs` is a git extension that helps handling large files in git repositories.
It is a **command-line tool** that can be used in conjunction with git.
To use git-lfs in remote git repositories, the git host provider needs to be aware of such extension first.

# Install git-lfs
Just like any other command line tools, `git-lfs` can be installed through package manager:
```
sudo apt install git-lfs
```
---
After installation, we can initialize it for the system so that it can take effects automatically when we cloning a git-lfs enabled repository.
```
git-lfs install
```
---

# Enable git-lfs
Inside a git repository, run
```
git-lfs install
```
This will install a pre-push hook in the repository, that will check/perform relevant git-lfs operations automatically before each push.
We also need to check if any setting needs to be done for specific git host providers.

### Track Files using git-lfs
We need to specify/add files that git-lfs should track:
```
git-lfs track "*.file"
```
Inside the double-quote is pattern same as in .gitignore.

Files that tracked by `git-lfs` can be found in [[gitattributes|.gitattributes]] file that is created/updated whenever `git-lfs track <pattern>` is ran.

Run `git-lfs track` without a pattern will display a list of patterns that are currently tracked by git-lfs.
```
git-lfs track
```

### Untrack a file from git-lfs
- Remove the pattern in `.gitattributes`
- or by running `git-lfs untrack <pattern>`:
	 ```
	 git-lfs untrack "*.mp4"
	 ```