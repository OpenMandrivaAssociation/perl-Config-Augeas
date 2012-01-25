%define upstream_name       Config-Augeas
%define upstream_version 0.701

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	4
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Edit configuration files through Augeas C library
Url:        http://search.cpan.org/dist/%{upstream_name}
Source:     http://www.cpan.org/modules/by-module/Config/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:  perl-devel
BuildRequires:  perl(Module::Build)
BuildRequires:  augeas-devel
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Augeas is a library and command line tool that focuses on the most basic
problem in handling Linux configurations programmatically: editing actual
configuration files in a controlled manner.

To that end, Augeas exposes a tree of all configuration settings (well, all
the ones it knows about) and a simple local API for manipulating the tree.
Augeas then modifies underlying configuration files according to the
changes that have been made to the tree; it does as little modeling of
configurations as possible, and focuses exclusively on transforming the
tree-oriented syntax of its public API to the myriad syntaxes of individual
configuration files.

This module provides an object oriented Perl interface for Augeas
configuration edition library with a more "perlish" API than Augeas C
counterpart.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
rm -rf %buildroot
./Build install destdir=%{buildroot}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README ChangeLog
%{perl_vendorarch}/Config
%{perl_vendorarch}/auto/Config
%{_mandir}/man3/*
