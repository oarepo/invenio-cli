import importlib.metadata as importlib_metadata

from invenio_cli.commands.steps import Step
from invenio_cli.helpers.cli_config import CLIConfig


def extend_steps(command: str, cli_config: CLIConfig, steps: list[Step]) -> list[Step]:
    """Extend the given list of steps with additional steps."""

    for ep in importlib_metadata.entry_points(
        group=f"invenio_cli.extensions.{command}"
    ):
        ep.load()(cli_config, steps)

    return steps
