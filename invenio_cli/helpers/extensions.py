import importlib.metadata as importlib_metadata

from invenio_cli.commands.steps import Step


def extend_steps(command: str, steps: list[Step]) -> list[Step]:
    """Extend the given list of steps with additional steps."""

    for ep in importlib_metadata.entry_points(group="invenio_cli.extensions"):
        ep.load()(command, steps)

    return steps
