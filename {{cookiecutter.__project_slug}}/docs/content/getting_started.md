# Getting Started

Getting started with this package is easy.  To install it you just need to run the following command:
```console
$ pip install {{ cookiecutter.__package_name }}
```

::: {note}
This section is intended to be a place where you can show how easy it is to use your package.
Taylor it to your own needs and see the *Markup Tips* section at the end for some guidance on
the extended markdown elements that the Myst Parser gives you that you can use to build
content.
:::

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

![Figure 1](assets/figure_example.pdf){align=center}
