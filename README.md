# LeetCode Solvings

A repository of my solutions to various [LeetCode](https://leetcode.com/) problems I have attempted over time.

## Code

### Organization

The folder structure is based on where I encountered a problem. If a problem was given as a Daily Challenge the `./daily_challenges` is where it is and so on.

### Code Dependencies

I use [Poetry](https://python-poetry.org/) to make the virtual environments and manage my dependencies of solutions. Most solutions are written using Python's standard library, but development dependencies for linting and formatting are stored and updated there.

### Code Quality

I use various linters and formatters. Currently on the repository via [pre-commit](pre-commit.com):

- [Black](https://black.readthedocs.io/en/stable/)
- [Ruff](https://astral.sh/ruff)

### Testing

The entire repository works with [pytest](https://docs.pytest.org/). The following are some helpful commands for running tests.

```bash
# test every file
pytest
# test every file, but fail quickly
pytest -x
# test files of a certain pattern
pytest -k <PATTERN>
```


## Changelog

Using [changie](https://changie.dev/) I keep track of problems added and other small improvements

Creating change fragments is simple in this way

```bash
changie new # interactive shell takes you through the rest
```

When all my changes are done:

```bash
# usually just let my preset .changie.yaml determine what semver changes happen
changie batch auto
```

Then during a merge to `main` I can just do:

```bash
changie merge
```
