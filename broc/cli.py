import click
import broc
import db

@click.group()
def cli():
    """the brownie coder. Code for brownie points"""
    pass

@cli.command()
def init():
    """Start calculating brownie points for present git repo"""
    git_hooks_dir = broc.get_git_hooks_dir()
    if git_hooks_dir:
        broc.link_file_in_dir_as('post-commit', git_hooks_dir, 'post-commit')
        return click.echo(click.style("Created git hook in present git repo", fg='green'))

    return click.echo(click.style("Not a git repo", fg='red'))

@cli.command()
@click.option('-p', default=0, help="Number of points you spent")
@click.option('-m', default="because I wanted to. Biatch!", help="Reason for which you spent those poor brownie points. You spent the brownie points :'(")
@click.option('-e', help="Email address of the user who want to spend brownie points. Defaults to global git user", default='')
def spend(p, m, e):
    """Spend <points> for <email> because <msg>"""
    points = p
    msg = m
    email = broc.GIT_CONFIG['email'] if not e else e

    if points > 0:
        db.add_spend_entry(points, msg, email)

    points = click.style(str(points), fg='red')
    msg = click.style(msg, fg='red')
    email = click.style(email, fg='cyan')
    click.echo("{2} spent {0} points {1}".format(points, msg, email))


@cli.command()
@click.option('-e', help="Email address of the user who want to spend brownie points. Defaults to global git user", default='')
def stats(e):
    """Show today's stats (income and expenditure)"""
    email = e if e else broc.GIT_CONFIG['email']

    balance = db.get_total_brownie_points(email)
    today_income, today_expenditure = db.get_todays_stats(email)

    earned = click.style('Today Earned: ' + str(today_income), fg='green')
    spent = click.style('Today Spent: ' + str(today_expenditure), fg='red')
    total = click.style('Brownie Balance: ', fg='cyan')
    balance = click.style(str(balance), fg=(lambda b: 'green' if b > 0 else 'red')(balance))

    click.echo(earned)
    click.echo(spent)
    click.echo(total + balance)
