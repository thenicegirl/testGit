# Basic
## Config basic user information
```bash
git config --global user.name <Name>
git config --global user.email <Email>
```

## Create a new repository
```bash
git init
```

## Clone a repository from remote server
```bash
git clone <Url of remote repository>
```

## Display status of committing file in current workspace
```bash
git status
```

## Stage specific file (mark as file that will be commit)
```bash
git add <Path of file>
```

## Unstage specific file (unmark as file that will be commit)
```bash
git reset <Path of file>
```

## Commit and offer commit information
```bash
git commit -m "Comment"
```

## Display commit history
```bash
git log
```

## Push to remote repository
```bash
git push
```

## Pull from remote repository
```bash
git pull
```

# Advanced
## Modify (Amend) last commit
```bash
git commit --amend -m "<New commit information>"
```

## View all branches
```bash
git branch
```

## Create new branch
```bash
git branch <Branch name>
```

## Switch branch
```bash
git checkout <Branch name>
```

## Switch branch
```bash
git checkout <Branch name>
```

## Rename branch
```bash
git branch -m <Old name> <New name>
```

## Delete branch
```bash
git branch -d <Branch name>
```

## Rebase branch to master
```bash
git checkout <Branch name>
```

## Rebase branch to master
* Note: Need to switch branch before rebase
```bash
git checkout <Branch name>
git rebase master
```

## Merge branch to master using Fast-Forward
```bash
git checkout <Branch name>
git merge --ff-only master
```

## Abort the merge of this commit (when a conflict is encountered)
```bash
git merge --abort
```

## Hold uncommitted changes
```bash
git stash save "<An information>"
```

## Restore the previous staging changes and remove them from the staging list
```bash
git stash pop
```

## Check out the designated submission
```bash
git checkout <Hash of commit>
```

## Undo old commit
```bash
git revert <Hash of old commit>
```

## Undo old commit
* Note: Revert does not modify the old commit history, but generates the exact opposite modification of the previous commit in the working tree
```bash
git revert <Hash of old commit>
```

## View all operate in local repository using reflog
```bash
git reflog
```