Name:		texlive-facture
Version:	1.2.2
Release:	2
Summary:	Generate an invoice
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/xetex/latex/facture
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/facture.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/facture.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/facture.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Une classe simple permettant de produite une facture, avec ou
sans TVA, avec gestion d'une adresse differente pour la
livraison et pour la facturation. A simple class that allows
production of an invoice, with or without VAT; different
addresses for delivery and for billing are permitted.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/xelatex/facture
%doc %{_texmfdistdir}/doc/xelatex/facture
#- source
%doc %{_texmfdistdir}/source/xelatex/facture

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
