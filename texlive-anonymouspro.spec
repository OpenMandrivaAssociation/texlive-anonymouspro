Name:		texlive-anonymouspro
Version:	51631
Release:	2
Summary:	Use AnonymousPro fonts with LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/anonymouspro
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/anonymouspro.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/anonymouspro.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/anonymouspro.source.r%{version}.tar.xz
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
%{_texmfdistdir}/fonts/afm/public/anonymouspro
%{_texmfdistdir}/fonts/enc/dvips/anonymouspro
%{_texmfdistdir}/fonts/map/dvips/anonymouspro
%{_texmfdistdir}/fonts/tfm/public/anonymouspro
%{_texmfdistdir}/fonts/truetype/public/anonymouspro
%{_texmfdistdir}/fonts/type1/public/anonymouspro
%{_texmfdistdir}/fonts/vf/public/anonymouspro
%{_texmfdistdir}/tex/latex/anonymouspro
%doc %{_texmfdistdir}/doc/fonts/anonymouspro
#- source
%doc %{_texmfdistdir}/source/fonts/anonymouspro

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
