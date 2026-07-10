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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The fonts are a monowidth set, designed for use by coders. They appear
as a set of four TrueType, or Adobe Type 1 font files, and LaTeX support
is also provided.

