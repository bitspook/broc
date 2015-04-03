======================
Broc the Brownie Coder
======================

**Code for Brownie points**

A program for getting Brownie points for making more commits.

===========
How it work
===========  
* It sets git commit hooks in git repos (post-commit hook for now)
* Git hooks are used for collecting stats every time you make a commit, or pull new code (not implemented yet)

===============================
How it calculate brownie points
===============================
* Each commit is worth 1 brownie points
* Each brownie point for every file changed
* 50 additions are worth 1 brownie points
* 100 deletions are worth 1 brownie points
* Every 20 chars in a commit message are worth 1 brownie point. I think it should be 50

=========================
Why this scoring criteria
=========================

* I think more and small commit messages are good
* We can't always make small frequent commits, so no. of files/additions/deletions are also awarded
* I think commit messages should tell a story, the story of how the software is evolving. Commit messages are permanent documentation, so more points for more verbose commit messages. Longer commit messages are the easiest way to earn more brownie points, so write as long as you can about what changes you have made, what's up your mind right now, etc etc.

============
Installation
============
::
    pip install broc

=====
Usage
=====

::
    Usage: broc [OPTIONS] COMMAND [ARGS]...
    
    the brownie coder. Code for brownie points
    
    Options:
      --help  Show this message and exit.
    
    Commands:
      init   Start calculating brownie points for present git repo
      stats  Show today's stats (income and expenditure)
      spend  Spend <points> for <email> because <msg>

---------
broc init
---------
Run this from within a git repository to start milking it for brownie points. broc adds local `post-commit` git hooks, so you can choose which of your git repos should earn you brownie points.

---------------------
broc stats -e <email>
---------------------
email defaults to `git config --global --get user.email`

Show today's stats. At the moment, they look something like this: Most commands accept `-e` for email address. `broc` keeps track of brownie points with the email address of the author of commit, so it's configurable and defaults to global git user's email.


.. image:: https://i.imgur.com/5FNcsIS.png
:alt: broc stats output 

------------------------------------------------------------------------------------------------
broc spend -p <num> -m <message> -e <email> (defaults to `git config --global --get user.email`)
------------------------------------------------------------------------------------------------

```
  broc spend -p 50 -m "playing Coll Of Duty 4. Because I don't have GTA V" 
```

Spend <num> points for <message>. 


-------------------------------------------------------------------------------
Why spend? Shouldn't it be like earn some badge after a threshold or something?
-------------------------------------------------------------------------------

Read the inspiration section.

===========
Inspiration
===========

I work as a freelance software (mostly web) developer, but I often keep getting calls from startups/companies etc. A couple days back a rather cool startup contacted me with an offer to stay with them in a villa and code with a team while living with a team. It's a sort of fantasy actually. If I didn't have all these commitments I have, I would have said yes in a heartbeat. But my imagination flew. I was thinking how awesome it would be to have all the gadgets etc. Specially gaming consoles. I have a constant battle going for self-discipline, so it struck my head that
::
   "how I'll manage to write enough code while being able to play enough video games (without feeling bad about it)?"
   "Hmm..I would track my productivity"
   "How will I do that and utilize it for playing games?"
   "I'll convert my code into currency, and spend it on playing games"
   "Cool! But I wonder if there is some tool for doing that, I mean their are things for tracking time and all but..."
   "Wtf dude? I don't need people to write software for me. I write software for people"
   
   "But I am not joining the startup, am still freelancing, shall I build it?"
   "Let's build it so it would help us write good code too."

Then I thought of what problems I face when writing code, improvements I wanna make in my coding life. More often than not, I forget to commit my code. Although this is very rare, what happens pretty often are commit messages like "Some change", "Bug fix", "Change in this file" etc etc. I saw a good opportunity here to encourage improving my committing habits, so after few hours of work, here I am.

============
What's next?
============
I don't know. 'm gonna use this system daily, and if it proves to be worth the effort, I'll improve and enhance it. I have some ideas about having a pretty interface with a built-in web server (I wanted to try react for a long time for something more than dumb tutorials, this could be it), may be a cloud app too where everybody push showcase their brownie points, earn some badges may be. Oh wait! https://coderwall.com/ _Coderwall!

