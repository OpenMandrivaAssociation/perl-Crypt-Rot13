%define upstream_name    Crypt-Rot13
%define upstream_version 0.6

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Crypt-Rot13 module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
rot13 is a simple encryption in which ASCII letters are rotated 13 places. This
module provides an array object with methods to encrypt its string elements by
rotating ASCII letters n places down the alphabet.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes COPYING README
%{perl_vendorlib}/Crypt/Rot13.pm
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.600.0-2mdv2011.0
+ Revision: 680869
- mass rebuild

* Fri Feb 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.600.0-1mdv2011.0
+ Revision: 504832
- rebuild using %%perl_convert_version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.6-5mdv2010.0
+ Revision: 430391
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.6-4mdv2009.0
+ Revision: 256344
- rebuild

* Wed Dec 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.6-2mdv2008.1
+ Revision: 138072
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Sep 13 2006 Oden Eriksson <oeriksson@mandriva.com> 0.6-1mdv2007.0
- rebuild

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 0.6-1mdk
- initial Mandriva package

