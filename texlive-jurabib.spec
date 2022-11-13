Name:		texlive-jurabib
Version:	15878
Release:	1
Summary:	Extended BibTeX citation support for the humanities and legal texts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/jurabib
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jurabib.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jurabib.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jurabib.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package enables automated citation with BibTeX for legal
studies and the humanities. In addition, the package provides
commands for specifying editors in a commentary in a convenient
way. Simplified formatting of the citation as well as the
bibliography entry is also provided. It is possible to display
the (short) title of a work only if an authors is cited with
multiple works. Giving a full citation in the text, conforming
to the bibliography entry, is supported. Several options are
provided which might be of special interest for those outside
legal studies--for instance, displaying multiple full
citations. In addition, the format of last names and first
names of authors may be changed easily. Cross references to
other footnotes are possible. Language dependent handling of
bibliography entries is possible by the special language field.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bib/jurabib/book.bib
%{_texmfdistdir}/bibtex/bib/jurabib/comment.bib
%{_texmfdistdir}/bibtex/bib/jurabib/jbtest.bib
%{_texmfdistdir}/bibtex/bib/jurabib/jbtesthu.bib
%{_texmfdistdir}/bibtex/bst/jurabib/jox.bst
%{_texmfdistdir}/bibtex/bst/jurabib/jurabib.bst
%{_texmfdistdir}/bibtex/bst/jurabib/jureco.bst
%{_texmfdistdir}/bibtex/bst/jurabib/jurunsrt.bst
%{_texmfdistdir}/tex/latex/jurabib/dajbbib.ldf
%{_texmfdistdir}/tex/latex/jurabib/dejbbib.ldf
%{_texmfdistdir}/tex/latex/jurabib/dujbbib.ldf
%{_texmfdistdir}/tex/latex/jurabib/enjbbib.ldf
%{_texmfdistdir}/tex/latex/jurabib/fijbbib.ldf
%{_texmfdistdir}/tex/latex/jurabib/frjbbib.ldf
%{_texmfdistdir}/tex/latex/jurabib/itjbbib.ldf
%{_texmfdistdir}/tex/latex/jurabib/jblong.cfg
%{_texmfdistdir}/tex/latex/jurabib/jurabib.cfg
%{_texmfdistdir}/tex/latex/jurabib/jurabib.sty
%{_texmfdistdir}/tex/latex/jurabib/nojbbib.ldf
%{_texmfdistdir}/tex/latex/jurabib/ptjbbib.ldf
%{_texmfdistdir}/tex/latex/jurabib/spjbbib.ldf
%doc %{_texmfdistdir}/doc/latex/jurabib/changes.txt
%doc %{_texmfdistdir}/doc/latex/jurabib/docs/english/jbendoc.pdf
%doc %{_texmfdistdir}/doc/latex/jurabib/docs/english/jbendoc.tex
%doc %{_texmfdistdir}/doc/latex/jurabib/docs/german/jbgerdoc.pdf
%doc %{_texmfdistdir}/doc/latex/jurabib/docs/german/jbgerdoc.tex
%doc %{_texmfdistdir}/doc/latex/jurabib/jbtest.pdf
%doc %{_texmfdistdir}/doc/latex/jurabib/jbtest.tex
%doc %{_texmfdistdir}/doc/latex/jurabib/jbtest.url
%doc %{_texmfdistdir}/doc/latex/jurabib/jbtestbt.tex
%doc %{_texmfdistdir}/doc/latex/jurabib/jbtestbu.tex
%doc %{_texmfdistdir}/doc/latex/jurabib/jbtestcb.tex
%doc %{_texmfdistdir}/doc/latex/jurabib/jbtestcb1.tex
%doc %{_texmfdistdir}/doc/latex/jurabib/jbtestcb2.tex
%doc %{_texmfdistdir}/doc/latex/jurabib/jbtesthu.tex
%doc %{_texmfdistdir}/doc/latex/jurabib/jbtestmb.tex
#- source
%doc %{_texmfdistdir}/source/latex/jurabib/jurabib.dtx
%doc %{_texmfdistdir}/source/latex/jurabib/jurabib.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}
