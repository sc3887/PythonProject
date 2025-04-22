
import click
from repository import Repository

class Cli:

    def __init__(self, current):
        self.repository = Repository(current)
        print(self.repository)

    def create_cli(self):

        @click.group()
        def cli():
            """Management user interface repository"""
            pass

        @cli.command()
        def wit_init():
            try:
                self.repository.wit_init()
                click.echo("Initialized repository structure.")
            except Exception as e:
                click.echo(f"Error {e}")

        @cli.command()
        # @click.argument()
        def wit_add():
            try:
                self.repository.wit_add()
                # click.echo(f"file {file_name} added successfully.")
            except Exception as e:
                click.echo(f"Error {e}")

        @cli.command()
        # @click.argument("message")
        def wit_commit():
            try:
                self.repository.wit_commit()
                click.echo(f"Commited successfully.")
            except Exception as e:
                click.echo(f"Error {e}")

        @cli.command()
        def wit_log():
            try:
                self.repository.wit_log()
            except Exception as e:
                click.echo(f"Error {e}")

        @cli.command()
        def wit_status():
            try:
                self.repository.wit_status()
            except Exception as e:
                click.echo(f"Error {e}")

        @cli.command()
        # @click.argument("commit_hash")
        def wit_checkout():
            try:
                self.repository.wit_checkout()
            except Exception as e:
                click.echo(f"Error {e}")

        return cli