%include	/usr/lib/rpm/macros.perl
Summary:	RIPE NCC Autonomous Systems Query
Name:		ripe-asused
Version:	3.72
Release:	0.1
License:	distributable
Group:		Applications/Networking
Source0:	ftp://ftp.ripe.net/tools/asused-%{version}.tar.gz
# Source0-md5:	6821376705b9f9e080015dd9d1394161
Patch0:		%{name}-newquery.patch
BuildRequires:	perl >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Asused is a tool used by RIPE NCC hostmasters for checking various
aspects of our members' IP allocations and assignments as stored in
the RIPE database. We make it available to our members so they can
also check their own data. Our internal tool uses some more modules to
perform more checks which use information that is private to our
members, so the public distribution does not contain or require these
modules.

%prep
%setup -q -n asused-%{version}
%patch0 -p1 

%build
%{__perl} Makefile.PL
%{__make}
pod2man asused.pod asused.1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

sed -i -e "s|asused.conf|/etc/asused.conf|g" $RPM_BUILD_ROOT%{_bindir}/asused
sed -i -e "s|-Iblib/lib||g" $RPM_BUILD_ROOT%{_bindir}/asused

install -d $RPM_BUILD_ROOT%{_mandir}/man1
install asused.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes WARNING
%attr(755,root,root) %{_bindir}/asused
%{_mandir}/man1/*
%{_mandir}/man3/*
%{perl_sitelib}/*.pm
%dir %{perl_sitelib}/NCC
%{perl_sitelib}/NCC/*.pm
%dir %{perl_sitelib}/Reg
%{perl_sitelib}/Reg/*.pm
%dir %{perl_sitelib}/RipeWhois
%{perl_sitelib}/RipeWhois/*.pm
%dir %{perl_sitelib}/Net/RIPEWhois
%{perl_sitelib}/Net/RIPEWhois/*.pm
%{_mandir}/man1/*
