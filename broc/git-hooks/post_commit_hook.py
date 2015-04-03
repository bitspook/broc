#!/usr/bin/env python
import broc
from click import echo, style
from shell import shell
from broc import db
from datetime import datetime


repo = broc.get_git_root()

(hash, msg, email, author, timestamp) = shell('git log -1 --pretty=format:%H|||%s|||%ae|||%an|||%at').output()[0].split('|||')

created_at = datetime.fromtimestamp(float(timestamp))

stats_pairs = map(
    lambda s: s.split('\t')[:2],
    shell('git diff HEAD~ --numstat').output()
)


if not stats_pairs:
    (additions, deletions, num_files_changed) = 0, 0, 0
else:
    num_files_changed = len(stats_pairs)
    # stats_pairs = [['11', '13'], ['22', '0'], ['22', '0'], ['22', '0']]
    # additions =  [int(i[0]) for i in stats_pairs]
    # total additions = reduce(lambda x,y: x+y, [int(i[0]) for i in stats_pairs])
    (additions, deletions) = (reduce(lambda x,y: x+y, [int(i[0]) for i in stats_pairs]), #sum all the additions
                              reduce(lambda x,y: x+y, [int(i[1]) for i in stats_pairs])) #sum all the deletions

brownie_points = broc.calculate_brownie_points(len(msg), num_files_changed, additions, deletions)

db.add_commit_entry(repo, hash, msg, brownie_points, created_at, author, email)

echo("Brownie points earned: " + style(str(brownie_points), fg='green'))
