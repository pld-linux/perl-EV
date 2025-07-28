#
# Conditional build:
%bcond_without	tests	# unit tests

%define		pdir	EV
Summary:	EV - Perl interface to libev, a high performance full-featured event loop
Summary(pl.UTF-8):	EV - perlowy interfejs do libev - wydajnej pętli zdarzeń
Name:		perl-EV
Version:	4.34
Release:	3
Epoch:		1
# same as Perl, libev: BSD-like
License:	GPL v1+ or Artistic (Perl module), BSD-like (embedded libev)
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-authors/id/M/ML/MLEHMANN/%{pdir}-%{version}.tar.gz
# Source0-md5:	de739e773a995d8ad8602fa4f9f21ff2
Patch0:		typemap.patch
URL:		https://metacpan.org/dist/EV
BuildRequires:	perl-Canary-Stability
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.52
BuildRequires:	perl-common-sense
BuildRequires:	perl-devel >= 1:5.8.2
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
Conflicts:	perl-AnyEvent < 5.29
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides an interface to libev
<http://software.schmorp.de/pkg/libev.html>.

This module is very fast and scalable. It is actually so fast that you
can use it through the AnyEvent module, stay portable to other event
loops (if you don't rely on any watcher types not available through
it) and still be faster than with any other event loop currently
supported in Perl.

%description -l pl.UTF-8
Moduł ten dostarcza intefejs do libev
<http://software.schmorp.de/pkg/libev.html>.

Jest bardzo szybki i skalowalny. Właściwie jest na tyle szybki, że
można go użyć poprzez moduł AnyEvent i pozostawić kod przenośnym na
inne pętle zdarzeń (jeśli nie jest wymagane użycie typów obserwatorów
niedostępnych przez AnyEvent), i całość jest nadal szybsza niż inne
pętle zdarzeń dostępne z poziomu Perla.

%prep
%setup -q -n %{pdir}-%{version}
%patch -P0 -p0

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor </dev/null
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d libev-doc
%{__mv} libev/{Changes,LICENSE,README} libev-doc
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/EV/libev.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes COPYING README libev-doc
%dir %{perl_vendorarch}/EV
%{perl_vendorarch}/EV/*.pm
%{perl_vendorarch}/EV.pm
%{perl_vendorarch}/EV/EVAPI.h
%{perl_vendorarch}/EV/ev.h
%dir %{perl_vendorarch}/auto/EV
%attr(755,root,root) %{perl_vendorarch}/auto/EV/EV.so
%{_mandir}/man3/EV.3pm*
%{_mandir}/man3/EV::*.3pm*
