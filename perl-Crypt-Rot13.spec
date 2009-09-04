%define real_name Crypt-Rot13

Summary:	Crypt-Rot13 module for perl 
Name:		perl-%{real_name}
Version:	0.6
Release:	%mkrel 5
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
rot13 is a simple encryption in which ASCII letters are rotated 13 places. This
module provides an array object with methods to encrypt its string elements by
rotating ASCII letters n places down the alphabet.

%prep
%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes COPYING README
%{perl_vendorlib}/Crypt/Rot13.pm
%{_mandir}/*/*


