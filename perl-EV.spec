#
# Conditional build:
%bcond_with	tests		# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	EV
Summary:	EV - perl interface to libev, a high performance full-featured event loop
Summary(pl.UTF-8):	EV - interfejs perlowy do libev
Name:		perl-EV
Version:	3.8
Release:	3
# same as perl, libev: BSD-like
License:	GPL v1+ or Artistic, partially BSD-like
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/M/ML/MLEHMANN/%{pdir}-%{version}.tar.gz
# Source0-md5:	3ce46dd8b6e65103ab55eba3f84448ad
URL:		http://search.cpan.org/dist/EV/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides an interface to libev
(http://software.schmorp.de/pkg/libev.html). While the documentation
below is comprehensive, one might also consult the documentation of
libev itself (http://pod.tst.eu/http://cvs.schmorp.de/libev/ev.pod or
perldoc EV::libev) for more subtle details on watcher semantics or
some discussion on the available backends, or how to force a specific
backend with LIBEV_FLAGS, or just about in any case because it has
much more detailed information.

This module is very fast and scalable. It is actually so fast that you
can use it through the AnyEvent module, stay portable to other event
loops (if you don't rely on any watcher types not available through
it) and still be faster than with any other event loop currently
supported in Perl.

This module does not export any symbols.

%description -l pl.UTF-8
Moduł ten dostarcza intefejs do libev.

%prep
%setup -q -n %{pdir}-%{version}

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
mv -f libev/{Changes,LICENSE,README} libev-doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README COPYING libev-doc
%dir %{perl_vendorarch}/EV
%{perl_vendorarch}/EV/*.pm
%{perl_vendorarch}/EV.pm
%{perl_vendorarch}/EV/EVAPI.h
%{perl_vendorarch}/EV/ev.h
%dir %{perl_vendorarch}/auto/EV
%{perl_vendorarch}/auto/EV/EV.bs
%attr(755,root,root) %{perl_vendorarch}/auto/EV/EV.so
%{_mandir}/man3/*
