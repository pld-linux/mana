#
# TODO:
#	- subpackage for uim stuff?
#
#
# Conditional build:
%bcond_with	bootstrap	# don't require dictionary for package build
#
Summary:	A kana(romaji)-kanji conversion engine using ChaSen algorithm
#Summary(pl.UTF-8):	-
Name:		mana
Version:	0.2.1
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.jp/shinji/20514/%{name}-%{version}.tar.bz2
# Source0-md5:	3a173e9c6047ed18ae8080cfcd38f3a4
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-change_scheme_dir.patch
URL:		http://sourceforge.jp/projects/shinji/
BuildRequires:	gdbm-devel
BuildRequires:	glib2-devel
BuildRequires:	iconv
BuildRequires:	ocaml
BuildRequires:	ocaml-camlp4
BuildRequires:	ocaml-findlib
Requires:	gdbm
%{!?with_bootstrap:Requires:	manadic}
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A kana(romaji)-kanji conversion engine using ChaSen algorithm.

#%description -l pl.UTF-8

%prep
%setup -q
%patch0 -p1
%patch1 -p0

%build
%configure
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/uim

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# install mana-prelude.scm for uim
install -p mana/mana-prelude.scm $RPM_BUILD_ROOT%{_datadir}/uim

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/mana
%attr(755,root,root) %{_libdir}/mana/make*
#%{_datadir}/uim/mana-prelude.scm
