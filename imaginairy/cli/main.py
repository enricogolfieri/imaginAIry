import logging

import click

from imaginairy.cli.colorize import colorize_cmd
from imaginairy.cli.describe import describe_cmd
from imaginairy.cli.edit import edit_cmd
from imaginairy.cli.edit_demo import edit_demo_cmd
from imaginairy.cli.imagine import imagine_cmd
from imaginairy.cli.shared import ColorShell, ImagineColorsCommand
from imaginairy.cli.train import prep_images_cmd, prune_ckpt_cmd, train_concept_cmd
from imaginairy.cli.upscale import upscale_cmd

logger = logging.getLogger(__name__)


@click.command(
    prompt="🤖🧠> ",
    intro="Starting imaginAIry shell...",
    help_headers_color="yellow",
    help_options_color="green",
    context_settings={"max_content_width": 140},
    cls=ColorShell,
)
@click.pass_context
def aimg(ctx):
    """
    🤖🧠 ImaginAIry.

    Pythonic generation of images via AI
    """
    import sys

    is_shell = len(sys.argv) == 1
    if is_shell:
        print(ctx.get_help())


aimg.command_class = ImagineColorsCommand


aimg.add_command(colorize_cmd, name="colorize")
aimg.add_command(describe_cmd, name="describe")
aimg.add_command(edit_cmd, name="edit")
aimg.add_command(edit_demo_cmd, name="edit-demo")
aimg.add_command(imagine_cmd, name="imagine")
aimg.add_command(prep_images_cmd, name="prep-images")
aimg.add_command(prune_ckpt_cmd, name="prune-ckpt")
aimg.add_command(train_concept_cmd, name="train-concept")
aimg.add_command(upscale_cmd, name="upscale")


@aimg.command()
def version():
    """Print the version."""
    from imaginairy.version import get_version

    print(get_version())


@aimg.command("system-info")
def system_info():
    """
    Display system information. Submit this when reporting bugs.
    """
    from imaginairy.debug_info import get_debug_info

    for k, v in get_debug_info().items():
        k += ":"
        click.secho(f"{k: <30} {v}")
