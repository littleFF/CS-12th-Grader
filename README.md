# CS-12th-Grader

## Task Nov 10th:
***
* Run your first github project on your computer:


learn to know how to read a markdown file in github

From: https://github.com/will8211/unimatrix/blob/master/README.md
***

# UniMatrix

Python script to simulate the display from "The Matrix" in terminal. Uses half-width katakana unicode characters by default, but can use custom character sets. Accepts keyboard controls while running.

Based on CMatrix by Chris Allegretta and Abishek V. Ashok. The following option should produce virtually the same output as CMatrix:
```
$ unimatrix -n -s 96 -l o
```
## Install

Linux users can use curl to install:
```
sudo curl -L https://raw.githubusercontent.com/will8211/unimatrix/master/unimatrix.py -o /usr/local/bin/unimatrix
sudo chmod a+rx /usr/local/bin/unimatrix
```
If you do not have curl, you can alternatively use a recent wget:
```
sudo wget https://raw.githubusercontent.com/will8211/unimatrix/master/unimatrix.py -O /usr/local/bin/unimatrix
sudo chmod a+rx /usr/local/bin/unimatrix
```
You can also install it with pip:
```
pip install git+https://github.com/will8211/unimatrix.git
```

Users of Arch-based distros can get it from the AUR as ```unimatrix-git```, although it might not be the most recent version.



## Task Nov 11th:
***
Register an github account, and commit an introduction to my repo.



## Task Dec 1st:
***
1. checkout a repository

when using a remote server, your command will be
```
git clone https://github.com/littleFF/CS-12th-Grader.git
```



2. Move your project directory into CS-12th-Grader and name it XXX's word cloud project


3. Add & commit
```
git add <filename>
git add *
```
This is the first step in the basic git workflow. To actually commit these changes use
```
git commit -m "Commit message"

```
Now the file is committed to the HEAD, but not in your remote repository yet.

4. Pushing changes
Your changes are now in the HEAD of your local working copy. To send those changes to your remote repository, execute 
```
git push origin master
```
Change master to whatever branch you want to push your changes to. 

If you have not cloned an existing repository and want to connect your repository to a remote server, you need to add it with
```
git remote add origin <server>
```
Now you are able to push your changes to the selected remote server

5. Remember

update & merge
to update your local repository to the newest commit, execute 
```
git pull
```





# wordcloud-kin
