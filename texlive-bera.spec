# revision 20031
# category Package
# catalog-ctan /fonts/bera
# catalog-date 2008-01-28 20:53:41 +0100
# catalog-license other-free
# catalog-version undef
Name:		texlive-bera
Version:	20080128
Release:	10
Summary:	Bera fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/bera
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bera.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bera.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package contains the Bera Type 1 fonts, and a zip archive
containing files to use the fonts with LaTeX. Bera is a set of
three font families: Bera Serif (a slab-serif Roman), Bera Sans
(a Frutiger descendant), and Bera Mono (monospaced/typewriter).
Support for use in LaTeX is also provided. The Bera family is a
repackaging, for use with TeX, of the Bitstream Vera family.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/bera/fveb8a.afm
%{_texmfdistdir}/fonts/afm/public/bera/fver8a.afm
%{_texmfdistdir}/fonts/afm/public/bera/fvmb8a.afm
%{_texmfdistdir}/fonts/afm/public/bera/fvmbo8a.afm
%{_texmfdistdir}/fonts/afm/public/bera/fvmr8a.afm
%{_texmfdistdir}/fonts/afm/public/bera/fvmro8a.afm
%{_texmfdistdir}/fonts/afm/public/bera/fvsb8a.afm
%{_texmfdistdir}/fonts/afm/public/bera/fvsbo8a.afm
%{_texmfdistdir}/fonts/afm/public/bera/fvsr8a.afm
%{_texmfdistdir}/fonts/afm/public/bera/fvsro8a.afm
%{_texmfdistdir}/fonts/map/dvips/bera/bera.map
%{_texmfdistdir}/fonts/tfm/public/bera/fveb8a.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fveb8c.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fveb8r.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fveb8t.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvebo8c.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvebo8r.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvebo8t.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fver8a.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fver8c.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fver8r.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fver8t.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvero8c.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvero8r.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvero8t.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvmb8a.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvmb8c.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvmb8r.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvmb8t.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvmbo8a.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvmbo8c.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvmbo8r.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvmbo8t.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvmr8a.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvmr8c.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvmr8r.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvmr8t.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvmro8a.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvmro8c.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvmro8r.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvmro8t.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvsb8a.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvsb8c.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvsb8r.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvsb8t.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvsbo8a.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvsbo8c.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvsbo8r.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvsbo8t.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvsr8a.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvsr8c.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvsr8r.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvsr8t.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvsro8a.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvsro8c.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvsro8r.tfm
%{_texmfdistdir}/fonts/tfm/public/bera/fvsro8t.tfm
%{_texmfdistdir}/fonts/type1/public/bera/fveb8a.pfb
%{_texmfdistdir}/fonts/type1/public/bera/fver8a.pfb
%{_texmfdistdir}/fonts/type1/public/bera/fvmb8a.pfb
%{_texmfdistdir}/fonts/type1/public/bera/fvmbo8a.pfb
%{_texmfdistdir}/fonts/type1/public/bera/fvmr8a.pfb
%{_texmfdistdir}/fonts/type1/public/bera/fvmro8a.pfb
%{_texmfdistdir}/fonts/type1/public/bera/fvsb8a.pfb
%{_texmfdistdir}/fonts/type1/public/bera/fvsbo8a.pfb
%{_texmfdistdir}/fonts/type1/public/bera/fvsr8a.pfb
%{_texmfdistdir}/fonts/type1/public/bera/fvsro8a.pfb
%{_texmfdistdir}/fonts/vf/public/bera/fveb8c.vf
%{_texmfdistdir}/fonts/vf/public/bera/fveb8t.vf
%{_texmfdistdir}/fonts/vf/public/bera/fvebo8c.vf
%{_texmfdistdir}/fonts/vf/public/bera/fvebo8t.vf
%{_texmfdistdir}/fonts/vf/public/bera/fver8c.vf
%{_texmfdistdir}/fonts/vf/public/bera/fver8t.vf
%{_texmfdistdir}/fonts/vf/public/bera/fvero8c.vf
%{_texmfdistdir}/fonts/vf/public/bera/fvero8t.vf
%{_texmfdistdir}/fonts/vf/public/bera/fvmb8c.vf
%{_texmfdistdir}/fonts/vf/public/bera/fvmb8t.vf
%{_texmfdistdir}/fonts/vf/public/bera/fvmbo8c.vf
%{_texmfdistdir}/fonts/vf/public/bera/fvmbo8t.vf
%{_texmfdistdir}/fonts/vf/public/bera/fvmr8c.vf
%{_texmfdistdir}/fonts/vf/public/bera/fvmr8t.vf
%{_texmfdistdir}/fonts/vf/public/bera/fvmro8c.vf
%{_texmfdistdir}/fonts/vf/public/bera/fvmro8t.vf
%{_texmfdistdir}/fonts/vf/public/bera/fvsb8c.vf
%{_texmfdistdir}/fonts/vf/public/bera/fvsb8t.vf
%{_texmfdistdir}/fonts/vf/public/bera/fvsbo8c.vf
%{_texmfdistdir}/fonts/vf/public/bera/fvsbo8t.vf
%{_texmfdistdir}/fonts/vf/public/bera/fvsr8c.vf
%{_texmfdistdir}/fonts/vf/public/bera/fvsr8t.vf
%{_texmfdistdir}/fonts/vf/public/bera/fvsro8c.vf
%{_texmfdistdir}/fonts/vf/public/bera/fvsro8t.vf
%{_texmfdistdir}/tex/latex/bera/bera.sty
%{_texmfdistdir}/tex/latex/bera/beramono.sty
%{_texmfdistdir}/tex/latex/bera/berasans.sty
%{_texmfdistdir}/tex/latex/bera/beraserif.sty
%{_texmfdistdir}/tex/latex/bera/t1fve.fd
%{_texmfdistdir}/tex/latex/bera/t1fvm.fd
%{_texmfdistdir}/tex/latex/bera/t1fvs.fd
%{_texmfdistdir}/tex/latex/bera/ts1fve.fd
%{_texmfdistdir}/tex/latex/bera/ts1fvm.fd
%{_texmfdistdir}/tex/latex/bera/ts1fvs.fd
%doc %{_texmfdistdir}/doc/fonts/bera/LICENSE
%doc %{_texmfdistdir}/doc/fonts/bera/README
%doc %{_texmfdistdir}/doc/fonts/bera/bera.pdf
%doc %{_texmfdistdir}/doc/fonts/bera/bera.txt

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20080128-2
+ Revision: 749566
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20080128-1
+ Revision: 717907
- texlive-bera
- texlive-bera
- texlive-bera
- texlive-bera
- texlive-bera

