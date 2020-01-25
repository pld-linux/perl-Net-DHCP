#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Net
%define		pnam	DHCP
Summary:	Net::DHCP - Perl extension for handling DHCP packets
Summary(pl.UTF-8):	Net::DHCP - rozszerzenie Perla do obsługi pakietów DHCP
Name:		perl-%{pdir}-%{pnam}
Version:	0.696
Release:	1
License:	Perl
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	60e32496ae2b750611487537b54e0bae
URL:		http://search.cpan.org/dist/Net-DHCP/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::DHCP is a DHCP set of classes designed to handle basic DHCP
handling. It can be used to develop either client, server or relays.
It is composed of 100% pure Perl.

%description -l pl.UTF-8
Net::DHCP jest zestawem klas do obsługi DHCP. Może być użyty do
tworzenia klienta, serwera lub przekaźnika. Napisany w całości
w Perlu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%{__cp} -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Net/DHCP
%{perl_vendorlib}/Net/DHCP/Constants.pm
%{perl_vendorlib}/Net/DHCP/Packet.pm
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.pl
%{_examplesdir}/%{name}-%{version}/l2tp-dhcp-inform
