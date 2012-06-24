Summary:	Binary file editor based on ncurses.
Summary(fr):	Visualisation et edition de fichiers en hexadecimal ou en ASCII
Summary(pl):	Edytor plikow binarnych oparty na bibliotece ncurses
Name:		hexedit
Version:	1.1.0
Release:	1
License:	GPL
Group:		Applications/Editors
Group(pt):	X11/Aplica��es/Editores
Group(pl):	Aplikacje/Edytory
Source0:	http://www.chez.com/prigaux/%{name}-%{version}.src.tgz
Patch0:		hexedit-DESTDIR.patch
URL:		http://www.chez.com/prigaux/hexedit.html
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
hexedit shows a file both in ASCII and in hexadecimal. The file can be
a device as the file is read a piece at a time. You can modify the
file and search through it.

%description -l pl
przegl�danie i edycja plik�w w formacie hexadecymalnym lub w ASCII.
hexedit pokazuje plik w zar�wno w postaci ASCII jak i hexadecymalnej.
Mo�esz przeszukiwa� modyfikowany plik. The file can be a device as the
file is not whole read.

%description -l fr
hexedit montre le fichier � la fois en ASCII et en hexad�cimal. Le
fichier peut �tre un device vu que le fichier est lu par petit
morceau. Possibilit� de modifier le fichier et de faire une recherche.

%prep
%setup -q -n %{name}
%patch -p1

%build
LDFLAGS="-s"
CFLAGS="$RPM_OPT_FLAGS -I/usr/include/ncurses"
export LDFLAGS CFLAGS
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
