Summary:	Binary file editor based on ncurses.
Summary(pl):	Edytor plikow binarnych oparty na bibliotece ncurses
Name:		hexedit
Version:	0.9.4
Release:	2
License:	GPL
Group:		Applications/Editors
Group(pt):	X11/Aplicações/Editores
Group(pl):	Aplikacje/Edytory
Source0:	http://www.chez.com/prigaux/%{name}-%{version}.tar.gz
URL:		http://www.chez.com/prigaux/
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
View and edit files in hexdecimal or ASCII mode.

%description -l pl
Przegl±danie i edycja plików w trybie hexdecymalnym lub ASCII.

%prep
%setup -q

%build
make	CFLAGS="$RPM_OPT_FLAGS -I%{_includedir}/ncurses" \
	LOADLIBES="-lncurses"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install -s %{name} $RPM_BUILD_ROOT%{_bindir}

install hexedit.1 $RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf Changes TODO *.lsm \
	$RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%doc *.gz
%{_mandir}/man1/*
