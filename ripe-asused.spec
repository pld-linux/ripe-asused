%include	/usr/lib/rpm/macros.perl
Summary:	RIPE NCC Autonomous Systems Query
Summary(pl.UTF-8):   Odpytywanie autonomicznych systemów RIPE NCC
Name:		ripe-asused
Version:	3.72
Release:	0.1
License:	distributable
Group:		Applications/Networking
Source0:	ftp://ftp.ripe.net/tools/asused-%{version}.tar.gz
# Source0-md5:	6821376705b9f9e080015dd9d1394161
Patch0:		%{name}-newquery.patch
Patch1:		%{name}-spelling.patch
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Asused is a tool used by RIPE NCC hostmasters for checking various
aspects of their members' IP allocations and assignments as stored in
the RIPE database. They make it available to our members so they can
also check their own data. RIPE internal tool uses some more modules
to perform more checks which use information that is private to their
members, so the public distribution does not contain or require these
modules.

%description -l pl.UTF-8
Asused to narzędzie używane przez hostmasterów RIPE NCC do sprawdzania
różnych aspektów alokacji i przydziałów IP swoich członków zgodnie z
zapisami w bazie danych RIPE. Zostało udostępnione członkom, dzięki
czemu oni także mogą sprawdzać swoje dane. Wewnętrzne narzędzie RIPE
używa trochę więcej modułów do sprawdzania informacji prywatnych dla
swoich członków, więc publiczna dystrybucja nie zawiera albo nie
wymaga tych modułów.

%prep
%setup -q -n asused-%{version}
%patch0 -p1 
%patch1 -p1 

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
pod2man asused.pod asused.1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT SITEPREFIX=%{_prefix}

sed -i -e "s|asused.conf|%{_sysconfdir}/asused.conf|g" $RPM_BUILD_ROOT%{_bindir}/asused
sed -i -e "s|-Iblib/lib||g" $RPM_BUILD_ROOT%{_bindir}/asused

install -d $RPM_BUILD_ROOT%{_mandir}/man1
install asused.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes WARNING
%attr(755,root,root) %{_bindir}/asused
%{perl_vendorlib}/*.pm
%dir %{perl_vendorlib}/NCC
%{perl_vendorlib}/NCC/*.pm
%dir %{perl_vendorlib}/Reg
%{perl_vendorlib}/Reg/*.pm
%dir %{perl_vendorlib}/RipeWhois
%{perl_vendorlib}/RipeWhois/*.pm
%dir %{perl_vendorlib}/Net/RIPEWhois
%{perl_vendorlib}/Net/RIPEWhois/*.pm
%{_mandir}/man1/*
%{_mandir}/man3/*
