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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package contains the Bera Type 1 fonts, and a zip archive containing
files to use the fonts with LaTeX. Bera is a set of three font families:
Bera Serif (a slab-serif Roman), Bera Sans (a Frutiger descendant), and
Bera Mono (monospaced/typewriter). Support for use in LaTeX is also
provided. The Bera family is a repackaging, for use with TeX, of the
Bitstream Vera family.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/fonts
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/fonts
%dir %{_datadir}/texmf-dist/fonts/afm
%dir %{_datadir}/texmf-dist/fonts/map
%dir %{_datadir}/texmf-dist/fonts/tfm
%dir %{_datadir}/texmf-dist/fonts/type1
%dir %{_datadir}/texmf-dist/fonts/vf
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/fonts/bera
%dir %{_datadir}/texmf-dist/fonts/afm/public
%dir %{_datadir}/texmf-dist/fonts/map/dvips
%dir %{_datadir}/texmf-dist/fonts/tfm/public
%dir %{_datadir}/texmf-dist/fonts/type1/public
%dir %{_datadir}/texmf-dist/fonts/vf/public
%dir %{_datadir}/texmf-dist/tex/latex/bera
%dir %{_datadir}/texmf-dist/fonts/afm/public/bera
%dir %{_datadir}/texmf-dist/fonts/map/dvips/bera
%dir %{_datadir}/texmf-dist/fonts/tfm/public/bera
%dir %{_datadir}/texmf-dist/fonts/type1/public/bera
%dir %{_datadir}/texmf-dist/fonts/vf/public/bera
%doc %{_datadir}/texmf-dist/doc/fonts/bera/LICENSE
%doc %{_datadir}/texmf-dist/doc/fonts/bera/README
%doc %{_datadir}/texmf-dist/doc/fonts/bera/bera.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/bera/bera.txt
%{_datadir}/texmf-dist/fonts/afm/public/bera/fveb8a.afm
%{_datadir}/texmf-dist/fonts/afm/public/bera/fver8a.afm
%{_datadir}/texmf-dist/fonts/afm/public/bera/fvmb8a.afm
%{_datadir}/texmf-dist/fonts/afm/public/bera/fvmbo8a.afm
%{_datadir}/texmf-dist/fonts/afm/public/bera/fvmr8a.afm
%{_datadir}/texmf-dist/fonts/afm/public/bera/fvmro8a.afm
%{_datadir}/texmf-dist/fonts/afm/public/bera/fvsb8a.afm
%{_datadir}/texmf-dist/fonts/afm/public/bera/fvsbo8a.afm
%{_datadir}/texmf-dist/fonts/afm/public/bera/fvsr8a.afm
%{_datadir}/texmf-dist/fonts/afm/public/bera/fvsro8a.afm
%{_datadir}/texmf-dist/fonts/map/dvips/bera/bera.map
%{_datadir}/texmf-dist/fonts/tfm/public/bera/fveb8a.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bera/fveb8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bera/fveb8r.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bera/fveb8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bera/fvebo8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bera/fvebo8r.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bera/fvebo8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bera/fver8a.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bera/fver8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bera/fver8r.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bera/fver8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bera/fvero8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bera/fvero8r.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bera/fvero8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bera/fvmb8a.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bera/fvmb8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bera/fvmb8r.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bera/fvmb8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bera/fvmbo8a.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bera/fvmbo8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bera/fvmbo8r.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bera/fvmbo8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bera/fvmr8a.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bera/fvmr8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bera/fvmr8r.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bera/fvmr8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bera/fvmro8a.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bera/fvmro8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bera/fvmro8r.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bera/fvmro8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bera/fvsb8a.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bera/fvsb8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bera/fvsb8r.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bera/fvsb8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bera/fvsbo8a.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bera/fvsbo8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bera/fvsbo8r.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bera/fvsbo8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bera/fvsr8a.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bera/fvsr8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bera/fvsr8r.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bera/fvsr8t.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bera/fvsro8a.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bera/fvsro8c.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bera/fvsro8r.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bera/fvsro8t.tfm
%{_datadir}/texmf-dist/fonts/type1/public/bera/fveb8a.pfb
%{_datadir}/texmf-dist/fonts/type1/public/bera/fver8a.pfb
%{_datadir}/texmf-dist/fonts/type1/public/bera/fvmb8a.pfb
%{_datadir}/texmf-dist/fonts/type1/public/bera/fvmbo8a.pfb
%{_datadir}/texmf-dist/fonts/type1/public/bera/fvmr8a.pfb
%{_datadir}/texmf-dist/fonts/type1/public/bera/fvmro8a.pfb
%{_datadir}/texmf-dist/fonts/type1/public/bera/fvsb8a.pfb
%{_datadir}/texmf-dist/fonts/type1/public/bera/fvsbo8a.pfb
%{_datadir}/texmf-dist/fonts/type1/public/bera/fvsr8a.pfb
%{_datadir}/texmf-dist/fonts/type1/public/bera/fvsro8a.pfb
%{_datadir}/texmf-dist/fonts/vf/public/bera/fveb8c.vf
%{_datadir}/texmf-dist/fonts/vf/public/bera/fveb8t.vf
%{_datadir}/texmf-dist/fonts/vf/public/bera/fvebo8c.vf
%{_datadir}/texmf-dist/fonts/vf/public/bera/fvebo8t.vf
%{_datadir}/texmf-dist/fonts/vf/public/bera/fver8c.vf
%{_datadir}/texmf-dist/fonts/vf/public/bera/fver8t.vf
%{_datadir}/texmf-dist/fonts/vf/public/bera/fvero8c.vf
%{_datadir}/texmf-dist/fonts/vf/public/bera/fvero8t.vf
%{_datadir}/texmf-dist/fonts/vf/public/bera/fvmb8c.vf
%{_datadir}/texmf-dist/fonts/vf/public/bera/fvmb8t.vf
%{_datadir}/texmf-dist/fonts/vf/public/bera/fvmbo8c.vf
%{_datadir}/texmf-dist/fonts/vf/public/bera/fvmbo8t.vf
%{_datadir}/texmf-dist/fonts/vf/public/bera/fvmr8c.vf
%{_datadir}/texmf-dist/fonts/vf/public/bera/fvmr8t.vf
%{_datadir}/texmf-dist/fonts/vf/public/bera/fvmro8c.vf
%{_datadir}/texmf-dist/fonts/vf/public/bera/fvmro8t.vf
%{_datadir}/texmf-dist/fonts/vf/public/bera/fvsb8c.vf
%{_datadir}/texmf-dist/fonts/vf/public/bera/fvsb8t.vf
%{_datadir}/texmf-dist/fonts/vf/public/bera/fvsbo8c.vf
%{_datadir}/texmf-dist/fonts/vf/public/bera/fvsbo8t.vf
%{_datadir}/texmf-dist/fonts/vf/public/bera/fvsr8c.vf
%{_datadir}/texmf-dist/fonts/vf/public/bera/fvsr8t.vf
%{_datadir}/texmf-dist/fonts/vf/public/bera/fvsro8c.vf
%{_datadir}/texmf-dist/fonts/vf/public/bera/fvsro8t.vf
%{_datadir}/texmf-dist/tex/latex/bera/bera.sty
%{_datadir}/texmf-dist/tex/latex/bera/beramono.sty
%{_datadir}/texmf-dist/tex/latex/bera/berasans.sty
%{_datadir}/texmf-dist/tex/latex/bera/beraserif.sty
%{_datadir}/texmf-dist/tex/latex/bera/t1fve.fd
%{_datadir}/texmf-dist/tex/latex/bera/t1fvm.fd
%{_datadir}/texmf-dist/tex/latex/bera/t1fvs.fd
%{_datadir}/texmf-dist/tex/latex/bera/ts1fve.fd
%{_datadir}/texmf-dist/tex/latex/bera/ts1fvm.fd
%{_datadir}/texmf-dist/tex/latex/bera/ts1fvs.fd
