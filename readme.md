[![Build Status](https://api.travis-ci.org/misho104/natural_units.svg?branch=master)](https://travis-ci.org/misho104/natural_units)
[![License: MIT](https://img.shields.io/badge/License-MIT-ff25d1.svg)](https://github.com/misho104/natural_units/blob/master/LICENSE)

# natural_units

The [Natural Units](https://en.wikipedia.org/wiki/Natural_units) convention file for [GNU units](https://www.gnu.org/software/units/).

## TL;DR

### Debian/Ubuntu

```console
$ apt-get install units

$ units -V   # check that you are running **GNU Units**, not BSD units.

GNU Units version 2.1x
with readline, with utf8, locale en_US
Units data file is '/usr/share/units/definitions.units'

$ units -f natural.units

113 units, 42 prefixes, 0 nonlinear units
You have: 1m
You want: s
    1m = 3.335641e-09 s
    1m = (1 / 2.9979246e+08) s
```

### macOS + Homebrew

```console
$ brew install gnu-units

$ gunits -V   # double-check that you are running **GNU Units**, not BSD units.

GNU Units version 2.1x

$ gunits -vf natural.units

113 units, 42 prefixes, 0 nonlinear units

You have: 1 / fm
You want: GeV
    1 / fm = 0.19732696 GeV
    1 / fm = (1 / 5.0677312) GeV
```

## Overview

`natural.units` is a definition file of the [natural units](https://en.wikipedia.org/wiki/Natural_units) for [GNU units](https://www.gnu.org/software/units/).

***This is only for GNU units, not for BSD units pre-installed in macOS.***
You can check version by `units -v` (for BSD units) or `units -V` (for GNU units).

### Definition

In the natural units, all the units are given in terms of energy (giga electron volt, GeV) with defining
  **c = &hbar; = k<sub>B</sub> = 1**,
where c, &hbar; and k<sub>B</sub> are respectively the speed of light, the Planck constant and the Boltzmann constant.

For electromagnetism, we use the Lorentz-Heaviside convention, where the vacuum permittivity, &epsilon;<sub>0</sub>, and the vacuum permeability, &mu;<sub>0</sub>, are defined by
  **&mu;<sub>0</sub> = c<sup>2</sup>/&epsilon;<sub>0</sub> = 1**.
The fine structure constant is given by
  **&alpha; = e^2/4&pi;**,
where the elementary charge is given by
  **e = 1.60&times;10<sup>-19</sup> C = 0.303**.

## How to use

  1. Install GNU units.
  2. Prepare the file `natural.units`.
  3. Run and convert!

### Installation of GNU units

You can install **GNU** Units with `apt-get` (Debian/Ubuntu) or via [Homebrew](http://brew.sh/) (macOS) by

```console
apt-get install units   # Debian / Ubuntu
brew install gnu-units  # macOS
```

You should check that you are running **GNU** units, not **BSD** units (pre-installed in macOS), by

```console
$ units -V   # Debian / Ubuntu + apt-get
$ gunits -V  # macOS + Homebrew

GNU Units version 2.1x
```

### Run with `natural.units`

Run GNU Units with the file `natural.units`, downloaded from this GitHub repository:

```console
units -f natural.units    # Debian / Ubuntu + apt-get
gunits -f natural.units   # macOS + Homebrew
```


### Troubleshooting

You will encounter error message below if you are running *BSD* Units:

```output
units: redefinition of unit '#' on line 2 ignored
units: redefinition of unit '#' on line 3 ignored
units: redefinition of unit '#' on line 3 ignored
units: unexpected end of unit on line 3
units: redefinition of unit '#' on line 4 ignored
...
```

In this case, you have to recheck that you have installed **GNU** units and that you are using the correct command.

## Examples and some validations

### Basic examples

```console
$ units -f natural.units

You have: 1s
You want: m
    * 2.9979246e+08
    / 3.335641e-09
You have: 100 fb
You want: /GeV^2
    * 2.5681899e-10
    / 3.893793e+09
You have: 3 pc
You want: m
    * 9.2570327e+16
    / 1.0802598e-17
You have: 4.2K
You want:
    Definition: 3.6192796e-13 GeV
You have: 200 fm
You want: MeV
    * 1.0135462
    / 0.98663482
You have: 200 fm
You want: MeV
    reciprocal conversion
    * 0.98663482
    / 1.0135462
You have: 1 Mpl
You want: m
    reciprocal conversion
    * 1.6161943e-35
You have: sqrt(4 pi epsilon0)
You want: C
    * 1.8755459e-18
    / 5.331781e+17
```

### Basic validations

```console
$ units -f natural.units

You have: 4pi hbar c / e^2
You want:
    Definition: 137.036

You have: 4pi/e^2
You want:
    Definition: 137.03599

You have: c
You want:
    Definition: 2.99792458e8 m/s = 1

You have: hbar
You want:
    Definition: 1.054571726e-34 J s = 1

You have: e
You want:
    Definition: 1.602176565e-19 C = 0.30282213

You have: kB
You want:
    Definition: 1.3806488e-23 J/K = 1

You have: mu0
You want:
    Definition: 4 pi 1e-7 H/m = 1

You have: epsilon0
You want:
    Definition: 1/mu0 c^2 = 1
```

### More validations

See the Appendix of [Peskin's QFT book](http://www.slac.stanford.edu/~mpeskin/QFT.html).

```console
$ units -f natural.units

You have: 1 GeV
You want: g
    * 1.7826618e-24

You have: 1/GeV
You want: fm
    * 0.19732696

You have: 1/GeV^2
You want: mb
    * 0.3893793

You have: 1 e V / m
You want:
    Definition: 1.9732696e-25 GeV^2

You have: 1 e tesla
You want:
    Definition: 5.9157135e-17 GeV^2
```

## Data Source and Convention

Values are taken from [PDG Review of Particle Physics 2014](http://inspirehep.net/record/1315584).

Planck mass is symbolized by `M_pl`, while reduced Planck mass is by `M`.

Light year (`ly`) is defined as
  **c &times; 365.25day**
following [NIST publication 811](https://www.nist.gov/pml/special-publication-811), while `yr` denotes `tropicalyear` as is in PDG table.

## Author

Sho Iwamoto @ [http://www.misho-web.com/](http://www.misho-web.com/)
