Summary:	Binary file editor based on ncurses.
Summary(fr):	Visualisation et edition de fichiers en hexadecimal ou en ASCII
Summary(pl):	Edytor plików binarnych oparty na bibliotece ncurses
Name:		hexedit
Version:	1.1.0
Release:	2
License:	GPL
Group:		Applications/Editors
Group(de):	Applikationen/Editors
Group(pl):	Aplikacje/Edytory
Group(pt):	Aplicações/Editores
Source0:	http://www.chez.com/prigaux/%{name}-%{version}.src.tgz
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.chez.com/prigaux/hexedit.html
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
hexedit shows a file both in ASCII and in hexadecimal. The file can be
a device as the file is read a piece at a time. You can modify the
file and search through it.

%description -l pl
Przegl±danie i edycja plików w formacie hexadecymalnym lub w ASCII.
hexedit pokazuje plik w zarówno w postaci ASCII jak i hexadecymalnej.
Mo¿esz przeszukiwaæ modyfikowany plik. The file can be a device as the
file is not whole read.

%description -l fr
hexedit montre le fichier à la fois en ASCII et en hexadécimal. Le
fichier peut être un device vu que le fichier est lu par petit
morceau. Possibilité de modifier le fichier et de faire une recherche.

%prep
%setup -q -n %{name}
%patch -p1

%build
CFLAGS="%{rpmcflags} -I/usr/include/ncurses"
aclocal
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%doc *.gz
%{_mandir}/man1/*
