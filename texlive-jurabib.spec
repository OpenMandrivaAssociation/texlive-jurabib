%global tl_name jurabib
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.6
Release:	%{tl_revision}.1
Summary:	Extended BibTeX citation support for the humanities and legal texts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/jurabib
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/jurabib.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/jurabib.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/jurabib.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package enables automated citation with BibTeX for legal studies
and the humanities. In addition, the package provides commands for
specifying editors in a commentary in a convenient way. Simplified
formatting of the citation as well as the bibliography entry is also
provided. It is possible to display the (short) title of a work only if
an authors is cited with multiple works. Giving a full citation in the
text, conforming to the bibliography entry, is supported. Several
options are provided which might be of special interest for those
outside legal studies--for instance, displaying multiple full citations.
In addition, the format of last names and first names of authors may be
changed easily. Cross references to other footnotes are possible.
Language dependent handling of bibliography entries is possible by the
special language field.

