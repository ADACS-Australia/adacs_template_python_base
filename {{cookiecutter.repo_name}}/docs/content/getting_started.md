# Getting Started

Getting started with this package is easy.  To install it you just need to run the following command:
```console
$ pip install {{ cookiecutter.__package_name }}
```

<!-- AUTHOR NOTE: Replace this entire page with content specific to your project.
     Start with a short description of what your project does and a quick example.
     The "Markup Tips" section below shows the MyST Markdown syntax available to you;
     remove it once you no longer need it as reference. -->

## Markup Tips

Some useful elements include:

### Code Blocks

Command line execution can be marked-up as follows:

```console
$ pip install {{ cookiecutter.__package_name }}
```

Python code can be marked-up as follows:

```Python
import numpy as np

my_array = np.ndarray([0,100])
```

### Admonitions

A tip can be marked-up as follows:

:::{tip}
Help for the executable for this project can be obtained in a terminal as follows:
```sh
$ {{ cookiecutter.__package_name }} -h
```
:::

A note can be marked-up as follows:

::: {note}
This is an important thing to know.  Please take note.
:::

### Figures

A figure can be included as follows:

![Figure 1](../assets/figure_example.png){align=center}
