natural_units
=============

### Overview

The Natural Units convention file for [GNU units](https://www.gnu.org/software/units/).

#### Definition

Natural Units convention is defined by
$$
\def\kB{k_{\rm B}}
\def\un#1{\,{\rm #1}}
c = \hbar = \kB = 1,
$$
where $$$c, \hbar$$$, and $$$\kB$$$ are the speed of light, the Planck constant and the Boltmann constant, respectively.

Also we adopt Heaviside-Lorentz convention for the vacuum permittivity $$$\epsilon_0$$$ and the vacuum permeability $$$\mu_0$$$:
$$
\mu_0 = c^2/\epsilon_0 = 1.
$$

With this convention, the fine structure constant is
$$
\alpha = \frac{e^2}{4\pi},
$$
where $$$e\approx 0.303$$$ is the positron charge.

#### Data Source and Convention

Values are taken from	 [PDG Review of Particle Physics 2014](http://inspirehep.net/record/1315584).

Planck mass is symbolized by `Mpl`, while reduced Planck mass is by `M`.

Light year (`ly`) is defined as $$$c\cdot365.25\un{day}$$$, while `yr` denotes `tropicalyear`.


### How to use

#### Installation of GNU units

On Debian/Ubuntu,

```
apt-get install units
```

On MacOSX with [Homebrew](http://brew.sh/),

```
brew install units
brew link units
```

Note that ***this file is for GNU units, not for BSD units*** preinstalled in OSX. You can check version by `units -v` (for BSD units) or `units -V` (for GNU units).

#### Examples

```
$ natural_units:> units -f natural.units
units: unit name without a definition at line 103 of file 'natural.units'
112 units, 42 prefixes, 0 nonlinear units

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

This is telling $$$1\un{s}=3\times10^8\un{m}$$$, $$$100\un{fb} = 2.6\times10^{-10}/{\rm GeV^2}$$$, etc.

#### Validations

```
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

Also, as shown in the Appendix of [Peskin's QFT book](http://www.slac.stanford.edu/~mpeskin/QFT.html),

```
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

### Author

Sho Iwamoto @ [http://www.misho-web.com/](http://www.misho-web.com/)

