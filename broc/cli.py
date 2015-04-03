import click
import broc

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
def stats():
    """Show today's stats (income and expenditure)"""
    click.echo("Showing stats")

@cli.command()
@click.option('--points', default=1, help="Number of points you spent")
@click.option('--msg', default="Because I want to. Biatch!", help="Reason you spent those poor brownie points. You spent the brownie points :'(")
def spend(points, msg):
    """Spend <points> because <msg>"""
    points = click.style(str(points), fg='red')
    msg = click.style(msg, fg='cyan')
    click.echo("Spend {0} points because {1}".format(points, msg))
