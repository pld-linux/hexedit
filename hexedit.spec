Summary: Binary file editor based on ncurses.
Summary(pl): Edytor plikow binarnych oparty na bibliotece ncurses.
Name: hexedit
Version: 0.9.4
Release: 1
Group: Applications/System
Group(pl): Aplikacje/System
Copyright: GPL
Vendor: PLD
Distribution: PLD
URL: http://www.chez.com/prigaux/
Source: http://www.chez.com/prigaux/%{name}-%{version}.tar.gz
BuildArch: i386
BuildRoot: /tmp/%{name}-%{version}-root  


%description
View and edit files in hexdecimal or ASCII mode.

%description -l pl
Przegl±danie i edycja plików w trybie hexdecymalnym lub ASCII.


%prep
%setup
%build
make  

%install
install -d $RPM_BUILD_ROOT/usr/{bin,share{/man/man1,/doc/%{name}-%{version}}}
install -s %{name} $RPM_BUILD_ROOT/usr/bin
install -s Changes TODO %{name}-%{version}.lsm \
 $RPM_BUILD_ROOT/usr/share/doc/%{name}-%{version}
install -s hexedit.1 \
 $RPM_BUILD_ROOT/usr/share/man/man1

gzip -9nf $RPM_BUILD_ROOT/usr/share/doc/%{name}-%{version}/*
gzip -9nf $RPM_BUILD_ROOT/usr/share/man/man1/hexedit.1

%clean
rm -rf $RPM_BUILD_ROOT

%files

%defattr(644,root,root,755)
%attr(755,root,root) /usr/bin/*
%attr(644,root,root) /usr/share/doc/%{name}-%{version}/*
%attr(644,root,root) /usr/share/man/man1/*
%doc {Changes TODO %{name}-%{version}.lsm}.gz
 
 
