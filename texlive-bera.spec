%global tl_name bera
%global tl_revision 77682

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Bera fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/bera
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bera.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bera.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package contains the Bera Type 1 fonts, and a zip archive containing
files to use the fonts with LaTeX. Bera is a set of three font families:
Bera Serif (a slab-serif Roman), Bera Sans (a Frutiger descendant), and
Bera Mono (monospaced/typewriter). Support for use in LaTeX is also
provided. The Bera family is a repackaging, for use with TeX, of the
Bitstream Vera family.

