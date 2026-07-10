%global tl_name anonymouspro
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.2
Release:	%{tl_revision}.1
Summary:	Use AnonymousPro fonts with LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/anonymouspro
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/anonymouspro.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/anonymouspro.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/anonymouspro.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The fonts are a monowidth set, designed for use by coders. They appear
as a set of four TrueType, or Adobe Type 1 font files, and LaTeX support
is also provided.

%prep
%setup -q -c -a1 -a2
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
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/fonts
%dir %{_datadir}/texmf-dist/fonts/afm
%dir %{_datadir}/texmf-dist/fonts/enc
%dir %{_datadir}/texmf-dist/fonts/map
%dir %{_datadir}/texmf-dist/fonts/tfm
%dir %{_datadir}/texmf-dist/fonts/truetype
%dir %{_datadir}/texmf-dist/fonts/type1
%dir %{_datadir}/texmf-dist/fonts/vf
%dir %{_datadir}/texmf-dist/source/fonts
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/fonts/anonymouspro
%dir %{_datadir}/texmf-dist/fonts/afm/public
%dir %{_datadir}/texmf-dist/fonts/enc/dvips
%dir %{_datadir}/texmf-dist/fonts/map/dvips
%dir %{_datadir}/texmf-dist/fonts/tfm/public
%dir %{_datadir}/texmf-dist/fonts/truetype/public
%dir %{_datadir}/texmf-dist/fonts/type1/public
%dir %{_datadir}/texmf-dist/fonts/vf/public
%dir %{_datadir}/texmf-dist/source/fonts/anonymouspro
%dir %{_datadir}/texmf-dist/tex/latex/anonymouspro
%dir %{_datadir}/texmf-dist/fonts/afm/public/anonymouspro
%dir %{_datadir}/texmf-dist/fonts/enc/dvips/anonymouspro
%dir %{_datadir}/texmf-dist/fonts/map/dvips/anonymouspro
%dir %{_datadir}/texmf-dist/fonts/tfm/public/anonymouspro
%dir %{_datadir}/texmf-dist/fonts/truetype/public/anonymouspro
%dir %{_datadir}/texmf-dist/fonts/type1/public/anonymouspro
%dir %{_datadir}/texmf-dist/fonts/vf/public/anonymouspro
%doc %{_datadir}/texmf-dist/doc/fonts/anonymouspro/AnonymousPro-01.etx
%doc %{_datadir}/texmf-dist/doc/fonts/anonymouspro/AnonymousPro-02.etx
%doc %{_datadir}/texmf-dist/doc/fonts/anonymouspro/AnonymousPro-03.etx
%doc %{_datadir}/texmf-dist/doc/fonts/anonymouspro/AnonymousPro-drv.tex
%doc %{_datadir}/texmf-dist/doc/fonts/anonymouspro/AnonymousPro-map.tex
%doc %{_datadir}/texmf-dist/doc/fonts/anonymouspro/AnonymousPro-symbols.etx
%doc %{_datadir}/texmf-dist/doc/fonts/anonymouspro/AnonymousPro.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/anonymouspro/FONTLOG.txt
%doc %{_datadir}/texmf-dist/doc/fonts/anonymouspro/OFL.txt
%doc %{_datadir}/texmf-dist/doc/fonts/anonymouspro/README.md
%doc %{_datadir}/texmf-dist/doc/fonts/anonymouspro/README_Mark-Simonson.txt
%doc %{_datadir}/texmf-dist/doc/fonts/anonymouspro/anonymouspro-fixlatin.mtx
%doc %{_datadir}/texmf-dist/doc/fonts/anonymouspro/anonymouspro-fixtextcomp.mtx
%{_datadir}/texmf-dist/fonts/afm/public/anonymouspro/AnonymousPro-Bold.afm
%{_datadir}/texmf-dist/fonts/afm/public/anonymouspro/AnonymousPro-BoldItalic.afm
%{_datadir}/texmf-dist/fonts/afm/public/anonymouspro/AnonymousPro-Italic.afm
%{_datadir}/texmf-dist/fonts/afm/public/anonymouspro/AnonymousPro-Regular.afm
%{_datadir}/texmf-dist/fonts/enc/dvips/anonymouspro/AnonymousPro-01.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/anonymouspro/AnonymousPro-02.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/anonymouspro/AnonymousPro-03.enc
%{_datadir}/texmf-dist/fonts/enc/dvips/anonymouspro/AnonymousPro-symbols.enc
%{_datadir}/texmf-dist/fonts/map/dvips/anonymouspro/AnonymousPro.map
%{_datadir}/texmf-dist/fonts/tfm/public/anonymouspro/AnonymousPro-Bold-01.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/anonymouspro/AnonymousPro-Bold-02.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/anonymouspro/AnonymousPro-Bold-03.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/anonymouspro/AnonymousPro-Bold-Symbols-base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/anonymouspro/AnonymousPro-Bold-Symbols-u.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/anonymouspro/AnonymousPro-Bold-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/anonymouspro/AnonymousPro-Bold-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/anonymouspro/AnonymousPro-Bold.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/anonymouspro/AnonymousPro-BoldItalic-01.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/anonymouspro/AnonymousPro-BoldItalic-02.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/anonymouspro/AnonymousPro-BoldItalic-03.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/anonymouspro/AnonymousPro-BoldItalic-Symbols-base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/anonymouspro/AnonymousPro-BoldItalic-Symbols-u.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/anonymouspro/AnonymousPro-BoldItalic-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/anonymouspro/AnonymousPro-BoldItalic-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/anonymouspro/AnonymousPro-BoldItalic.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/anonymouspro/AnonymousPro-BoldSC-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/anonymouspro/AnonymousPro-Italic-01.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/anonymouspro/AnonymousPro-Italic-02.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/anonymouspro/AnonymousPro-Italic-03.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/anonymouspro/AnonymousPro-Italic-Symbols-base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/anonymouspro/AnonymousPro-Italic-Symbols-u.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/anonymouspro/AnonymousPro-Italic-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/anonymouspro/AnonymousPro-Italic-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/anonymouspro/AnonymousPro-Italic.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/anonymouspro/AnonymousPro-Regular-01.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/anonymouspro/AnonymousPro-Regular-02.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/anonymouspro/AnonymousPro-Regular-03.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/anonymouspro/AnonymousPro-Regular-Symbols-base.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/anonymouspro/AnonymousPro-Regular-Symbols-u.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/anonymouspro/AnonymousPro-Regular-t1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/anonymouspro/AnonymousPro-Regular-ts1.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/anonymouspro/AnonymousPro-Regular.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/anonymouspro/AnonymousPro-RegularSC-t1.tfm
%{_datadir}/texmf-dist/fonts/truetype/public/anonymouspro/AnonymousPro-Bold.ttf
%{_datadir}/texmf-dist/fonts/truetype/public/anonymouspro/AnonymousPro-BoldItalic.ttf
%{_datadir}/texmf-dist/fonts/truetype/public/anonymouspro/AnonymousPro-Italic.ttf
%{_datadir}/texmf-dist/fonts/truetype/public/anonymouspro/AnonymousPro-Regular.ttf
%{_datadir}/texmf-dist/fonts/type1/public/anonymouspro/AnonymousPro-Bold.pfb
%{_datadir}/texmf-dist/fonts/type1/public/anonymouspro/AnonymousPro-BoldItalic.pfb
%{_datadir}/texmf-dist/fonts/type1/public/anonymouspro/AnonymousPro-Italic.pfb
%{_datadir}/texmf-dist/fonts/type1/public/anonymouspro/AnonymousPro-Regular.pfb
%{_datadir}/texmf-dist/fonts/vf/public/anonymouspro/AnonymousPro-Bold-Symbols-u.vf
%{_datadir}/texmf-dist/fonts/vf/public/anonymouspro/AnonymousPro-Bold-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/anonymouspro/AnonymousPro-Bold-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/anonymouspro/AnonymousPro-BoldItalic-Symbols-u.vf
%{_datadir}/texmf-dist/fonts/vf/public/anonymouspro/AnonymousPro-BoldItalic-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/anonymouspro/AnonymousPro-BoldItalic-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/anonymouspro/AnonymousPro-BoldSC-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/anonymouspro/AnonymousPro-Italic-Symbols-u.vf
%{_datadir}/texmf-dist/fonts/vf/public/anonymouspro/AnonymousPro-Italic-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/anonymouspro/AnonymousPro-Italic-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/anonymouspro/AnonymousPro-Regular-Symbols-u.vf
%{_datadir}/texmf-dist/fonts/vf/public/anonymouspro/AnonymousPro-Regular-t1.vf
%{_datadir}/texmf-dist/fonts/vf/public/anonymouspro/AnonymousPro-Regular-ts1.vf
%{_datadir}/texmf-dist/fonts/vf/public/anonymouspro/AnonymousPro-RegularSC-t1.vf
%doc %{_datadir}/texmf-dist/source/fonts/anonymouspro/AnonymousPro.dtx
%doc %{_datadir}/texmf-dist/source/fonts/anonymouspro/AnonymousPro.ins
%{_datadir}/texmf-dist/tex/latex/anonymouspro/AnonymousPro.sty
%{_datadir}/texmf-dist/tex/latex/anonymouspro/t1anonymouspro.fd
%{_datadir}/texmf-dist/tex/latex/anonymouspro/ts1anonymouspro.fd
%{_datadir}/texmf-dist/tex/latex/anonymouspro/uanonymouspro.fd
