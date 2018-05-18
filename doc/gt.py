linuxuser@5gws004-linux:~/Desktop/projects/monitoringSystem/MonitoringSystem$ cd 
linuxuser@5gws004-linux:~$ cd g
bash: cd: g: No such file or directory
linuxuser@5gws004-linux:~$ cd Desktop/
linuxuser@5gws004-linux:~/Desktop$ cd git/
linuxuser@5gws004-linux:~/Desktop/git$ ls
OnlineQuiz
linuxuser@5gws004-linux:~/Desktop/git$ git clone https://github.com/raveena17/birthday-app.git
Cloning into 'birthday-app'...
warning: You appear to have cloned an empty repository.
Checking connectivity... done.
linuxuser@5gws004-linux:~/Desktop/git$ ls
birthday-app  OnlineQuiz





linuxuser@5gws004-linux:~/Desktop/git$ git clone https://github.com/raveena17/birthday_application.git
Cloning into 'birthday_application'...
warning: You appear to have cloned an empty repository.
Checking connectivity... done.

linuxuser@5gws004-linux:~/Desktop/git$ cd birthday
bash: cd: birthday: No such file or directory

linuxuser@5gws004-linux:~/Desktop/git$ cd birthday_application/


linuxuser@5gws004-linux:~/Desktop/git/birthday_application$ ls
birthday  birthday_application  db.sqlite3  manage.py


linuxuser@5gws004-linux:~/Desktop/git/birthday_application$ git status
On branch master

Initial commit

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	birthday/
	birthday_application/
	db.sqlite3
	manage.py

nothing added to commit but untracked files present (use "git add" to track)
linuxuser@5gws004-linux:~/Desktop/git/birthday_application$ git add *
linuxuser@5gws004-linux:~/Desktop/git/birthday_application$ git commit -m "First Commit"
[master (root-commit) 0d3b406] First Commit
 Committer: linuxuser <linuxuser@5gws004-linux.fifthgentech.local>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly. Run the
following command and follow the instructions in your editor to edit
your configuration file:

    git config --global --edit

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 36 files changed, 12057 insertions(+)
 create mode 100644 birthday/.models.py.swp
 create mode 100644 birthday/__init__.py
 create mode 100644 birthday/admin.py
 create mode 100644 birthday/apps.py
 create mode 100644 birthday/management/__init__.py
 create mode 100644 birthday/management/commands/__init__.py
 create mode 100644 birthday/management/commands/send_daily_birthday_wishes.py
 create mode 100644 birthday/migrations/0001_initial.py
 create mode 100644 birthday/migrations/0002_auto_20170830_1350.py
 create mode 100644 birthday/migrations/__init__.py
 create mode 100644 birthday/models.py
 create mode 100644 birthday/static/css/jquery.dataTables.min.css
 create mode 100644 birthday/static/css/style.css
 create mode 100644 birthday/static/images/birthday.jpeg
 create mode 100644 birthday/static/images/birthday.jpg
 create mode 100644 birthday/static/images/birthday_employee.jpg
 create mode 100644 birthday/static/images/index.jpeg
 create mode 100644 birthday/static/images/invitation.jpeg
 create mode 100644 birthday/static/images/save.gif
 create mode 100644 birthday/static/images/save.png
 create mode 100644 birthday/static/js/jquery-1.12.4.js
 create mode 100644 birthday/static/js/jquery.dataTables.min.js
 create mode 100644 birthday/static/style.css
 create mode 100644 birthday/templates/birthday_list.html
 create mode 100644 birthday/templates/employee_details.html
 create mode 100644 birthday/templates/home.html
 create mode 100644 birthday/templates/register.html
 create mode 100644 birthday/tests.py
 create mode 100644 birthday/urls.py
 create mode 100644 birthday/views.py
 create mode 100644 birthday_application/__init__.py
 create mode 100644 birthday_application/settings.py
 create mode 100644 birthday_application/urls.py
 create mode 100644 birthday_application/wsgi.py
 create mode 100644 db.sqlite3
 create mode 100755 manage.py
linuxuser@5gws004-linux:~/Desktop/git/birthday_application$ git push
warning: push.default is unset; its implicit value has changed in
Git 2.0 from 'matching' to 'simple'. To squelch this message
and maintain the traditional behavior, use:

  git config --global push.default matching

To squelch this message and adopt the new behavior now, use:

  git config --global push.default simple

When push.default is set to 'matching', git will push local branches
to the remote branches that already exist with the same name.

Since Git 2.0, Git defaults to the more conservative 'simple'
behavior, which only pushes the current branch to the corresponding
remote branch that 'git pull' uses to update the current branch.

See 'git help config' and search for 'push.default' for further information.
(the 'simple' mode was introduced in Git 1.7.11. Use the similar mode
'current' instead of 'simple' if you sometimes use older versions of Git)

Username for 'https://github.com': raveena17
Password for 'https://raveena17@github.com': 
Counting objects: 43, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (42/42), done.
Writing objects: 100% (43/43), 383.18 KiB | 0 bytes/s, done.
Total 43 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), done.
To https://github.com/raveena17/birthday_application.git
 * [new branch]      master -> master
linuxuser@5gws004-linux:~/Desktop/git/birthday_application$ 
