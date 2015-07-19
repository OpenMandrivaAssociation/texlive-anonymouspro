# revision 32582
# category Package
# catalog-ctan /fonts/anonymouspro
# catalog-date 2014-01-05 20:16:26 +0100
# catalog-license lppl1.3
# catalog-version 2.0
Name:		texlive-anonymouspro
Version:	2.0
Release:	5
Summary:	Use AnonymousPro fonts with LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/anonymouspro
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/anonymouspro.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/anonymouspro.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/anonymouspro.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The fonts are a monowidth set, designed for use by coders. They
appear as a set of four TrueType, or Adobe Type 1 font files,
and LaTeX support is also provided.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/anonymouspro/AnonymousPro-Bold.afm
%{_texmfdistdir}/fonts/afm/public/anonymouspro/AnonymousPro-BoldItalic.afm
%{_texmfdistdir}/fonts/afm/public/anonymouspro/AnonymousPro-Italic.afm
%{_texmfdistdir}/fonts/afm/public/anonymouspro/AnonymousPro-Regular.afm
%{_texmfdistdir}/fonts/enc/dvips/anonymouspro/AnonymousPro-01.enc
%{_texmfdistdir}/fonts/enc/dvips/anonymouspro/AnonymousPro-02.enc
%{_texmfdistdir}/fonts/enc/dvips/anonymouspro/AnonymousPro-03.enc
%{_texmfdistdir}/fonts/enc/dvips/anonymouspro/AnonymousPro-symbols.enc
%{_texmfdistdir}/fonts/map/dvips/anonymouspro/AnonymousPro.map
%{_texmfdistdir}/fonts/tfm/public/anonymouspro/AnonymousPro-Bold-01.tfm
%{_texmfdistdir}/fonts/tfm/public/anonymouspro/AnonymousPro-Bold-02.tfm
%{_texmfdistdir}/fonts/tfm/public/anonymouspro/AnonymousPro-Bold-03.tfm
%{_texmfdistdir}/fonts/tfm/public/anonymouspro/AnonymousPro-Bold-Symbols-base.tfm
%{_texmfdistdir}/fonts/tfm/public/anonymouspro/AnonymousPro-Bold-Symbols-u.tfm
%{_texmfdistdir}/fonts/tfm/public/anonymouspro/AnonymousPro-Bold-base.tfm
%{_texmfdistdir}/fonts/tfm/public/anonymouspro/AnonymousPro-Bold-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/anonymouspro/AnonymousPro-Bold-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/anonymouspro/AnonymousPro-Bold.tfm
%{_texmfdistdir}/fonts/tfm/public/anonymouspro/AnonymousPro-BoldItalic-01.tfm
%{_texmfdistdir}/fonts/tfm/public/anonymouspro/AnonymousPro-BoldItalic-02.tfm
%{_texmfdistdir}/fonts/tfm/public/anonymouspro/AnonymousPro-BoldItalic-03.tfm
%{_texmfdistdir}/fonts/tfm/public/anonymouspro/AnonymousPro-BoldItalic-Symbols-base.tfm
%{_texmfdistdir}/fonts/tfm/public/anonymouspro/AnonymousPro-BoldItalic-Symbols-u.tfm
%{_texmfdistdir}/fonts/tfm/public/anonymouspro/AnonymousPro-BoldItalic-base.tfm
%{_texmfdistdir}/fonts/tfm/public/anonymouspro/AnonymousPro-BoldItalic-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/anonymouspro/AnonymousPro-BoldItalic-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/anonymouspro/AnonymousPro-BoldItalic.tfm
%{_texmfdistdir}/fonts/tfm/public/anonymouspro/AnonymousPro-BoldSC-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/anonymouspro/AnonymousPro-Italic-01.tfm
%{_texmfdistdir}/fonts/tfm/public/anonymouspro/AnonymousPro-Italic-02.tfm
%{_texmfdistdir}/fonts/tfm/public/anonymouspro/AnonymousPro-Italic-03.tfm
%{_texmfdistdir}/fonts/tfm/public/anonymouspro/AnonymousPro-Italic-Symbols-base.tfm
%{_texmfdistdir}/fonts/tfm/public/anonymouspro/AnonymousPro-Italic-Symbols-u.tfm
%{_texmfdistdir}/fonts/tfm/public/anonymouspro/AnonymousPro-Italic-base.tfm
%{_texmfdistdir}/fonts/tfm/public/anonymouspro/AnonymousPro-Italic-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/anonymouspro/AnonymousPro-Italic-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/anonymouspro/AnonymousPro-Italic.tfm
%{_texmfdistdir}/fonts/tfm/public/anonymouspro/AnonymousPro-Regular-01.tfm
%{_texmfdistdir}/fonts/tfm/public/anonymouspro/AnonymousPro-Regular-02.tfm
%{_texmfdistdir}/fonts/tfm/public/anonymouspro/AnonymousPro-Regular-03.tfm
%{_texmfdistdir}/fonts/tfm/public/anonymouspro/AnonymousPro-Regular-Symbols-base.tfm
%{_texmfdistdir}/fonts/tfm/public/anonymouspro/AnonymousPro-Regular-Symbols-u.tfm
%{_texmfdistdir}/fonts/tfm/public/anonymouspro/AnonymousPro-Regular-base.tfm
%{_texmfdistdir}/fonts/tfm/public/anonymouspro/AnonymousPro-Regular-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/anonymouspro/AnonymousPro-Regular-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/anonymouspro/AnonymousPro-Regular.tfm
%{_texmfdistdir}/fonts/tfm/public/anonymouspro/AnonymousPro-RegularSC-t1.tfm
%{_texmfdistdir}/fonts/truetype/public/anonymouspro/AnonymousPro-Bold.ttf
%{_texmfdistdir}/fonts/truetype/public/anonymouspro/AnonymousPro-BoldItalic.ttf
%{_texmfdistdir}/fonts/truetype/public/anonymouspro/AnonymousPro-Italic.ttf
%{_texmfdistdir}/fonts/truetype/public/anonymouspro/AnonymousPro-Regular.ttf
%{_texmfdistdir}/fonts/type1/public/anonymouspro/AnonymousPro-Bold.pfb
%{_texmfdistdir}/fonts/type1/public/anonymouspro/AnonymousPro-BoldItalic.pfb
%{_texmfdistdir}/fonts/type1/public/anonymouspro/AnonymousPro-Italic.pfb
%{_texmfdistdir}/fonts/type1/public/anonymouspro/AnonymousPro-Regular.pfb
%{_texmfdistdir}/fonts/vf/public/anonymouspro/AnonymousPro-Bold-Symbols-u.vf
%{_texmfdistdir}/fonts/vf/public/anonymouspro/AnonymousPro-Bold-t1.vf
%{_texmfdistdir}/fonts/vf/public/anonymouspro/AnonymousPro-Bold-ts1.vf
%{_texmfdistdir}/fonts/vf/public/anonymouspro/AnonymousPro-BoldItalic-Symbols-u.vf
%{_texmfdistdir}/fonts/vf/public/anonymouspro/AnonymousPro-BoldItalic-t1.vf
%{_texmfdistdir}/fonts/vf/public/anonymouspro/AnonymousPro-BoldItalic-ts1.vf
%{_texmfdistdir}/fonts/vf/public/anonymouspro/AnonymousPro-BoldSC-t1.vf
%{_texmfdistdir}/fonts/vf/public/anonymouspro/AnonymousPro-Italic-Symbols-u.vf
%{_texmfdistdir}/fonts/vf/public/anonymouspro/AnonymousPro-Italic-t1.vf
%{_texmfdistdir}/fonts/vf/public/anonymouspro/AnonymousPro-Italic-ts1.vf
%{_texmfdistdir}/fonts/vf/public/anonymouspro/AnonymousPro-Regular-Symbols-u.vf
%{_texmfdistdir}/fonts/vf/public/anonymouspro/AnonymousPro-Regular-t1.vf
%{_texmfdistdir}/fonts/vf/public/anonymouspro/AnonymousPro-Regular-ts1.vf
%{_texmfdistdir}/fonts/vf/public/anonymouspro/AnonymousPro-RegularSC-t1.vf
%{_texmfdistdir}/tex/latex/anonymouspro/AnonymousPro.sty
%{_texmfdistdir}/tex/latex/anonymouspro/t1anonymouspro.fd
%{_texmfdistdir}/tex/latex/anonymouspro/ts1anonymouspro.fd
%{_texmfdistdir}/tex/latex/anonymouspro/uanonymouspro.fd
%doc %{_texmfdistdir}/doc/fonts/anonymouspro/AnonymousPro-01.etx
%doc %{_texmfdistdir}/doc/fonts/anonymouspro/AnonymousPro-02.etx
%doc %{_texmfdistdir}/doc/fonts/anonymouspro/AnonymousPro-03.etx
%doc %{_texmfdistdir}/doc/fonts/anonymouspro/AnonymousPro-drv.tex
%doc %{_texmfdistdir}/doc/fonts/anonymouspro/AnonymousPro-map.tex
%doc %{_texmfdistdir}/doc/fonts/anonymouspro/AnonymousPro-symbols.etx
%doc %{_texmfdistdir}/doc/fonts/anonymouspro/AnonymousPro.pdf
%doc %{_texmfdistdir}/doc/fonts/anonymouspro/FONTLOG.txt
%doc %{_texmfdistdir}/doc/fonts/anonymouspro/OFL.txt
%doc %{_texmfdistdir}/doc/fonts/anonymouspro/README
%doc %{_texmfdistdir}/doc/fonts/anonymouspro/README_Mark-Simonson.txt
%doc %{_texmfdistdir}/doc/fonts/anonymouspro/anonymouspro-fixlatin.mtx
%doc %{_texmfdistdir}/doc/fonts/anonymouspro/anonymouspro-fixtextcomp.mtx
#- source
%doc %{_texmfdistdir}/source/fonts/anonymouspro/AnonymousPro.dtx
%doc %{_texmfdistdir}/source/fonts/anonymouspro/AnonymousPro.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
