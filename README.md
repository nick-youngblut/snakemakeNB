jupyterSM
=========


#### Sections

- [Examples](#examples)
- [Installation and updating](#installation-and-updating)
- [Usage](#usage)
- [Changelog](#changelog)


## Examples




## Installation and updating

[[top](#sections)]

The pushbullet line magic can be installed with pip by executing:

```bash
pip install pushmsg
```

The development version of pushmsg line magic can be installed from GitHub by executing:

```bash
pip install -e git+https://github.com/nick-youngblut/pushmsg#egg=pushmsg
```


## Usage

[[top](#sections)]

After successful installation, the `pushmsg` magic extension can be loaded via:

`%load_ext pushmsg`

To get an overview of all available options, type:

`%pushmsg?`

To add an Pushbullet API key:

`%pushmsg -a my_key=o.FgVQMqK5IvASJOxllx`

To send a message:

`%pushmsg "my long job is complete!"`


## Changelog

[[top](#sections)]
