Summary:	Convert the .hp files into nice PostScript graphs
Summary(pl):	Konwersja plik�w .hp do �adnych wykres�w w PostScripcie
Name:		hp2ps
Version:	1.0
Release:	1
License:	The Glasgow Haskell Compiler License
Group:		Applications
Source0:	http://www.cl.cam.ac.uk/users/njn25/valgrind/%{name}-src.tar.bz2
# Source0-md5:	f9ad5f4400b4d63fcbeb6342caa1d908
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convert the .hp files into nice PostScript graphs.

%description -l pl
Narz�dzie konwertuj�ce pliki .hp do �adnych wykres�w w PostScripcie.

%prep
%setup -q -n %{name}

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install hp2ps $RPM_BUILD_ROOT%{_bindir}
install hp2ps.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES LICENSE README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
