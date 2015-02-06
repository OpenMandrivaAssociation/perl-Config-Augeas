%define upstream_name       Config-Augeas
%define upstream_version 1.000

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 1.000
Release:	3
Summary:	Edit configuration files through Augeas C library
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source:		http://www.cpan.org/modules/by-module/Config/Config-Augeas-1.000.tar.gz
BuildRequires:	perl-devel
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Test::More)
BuildRequires:	augeas-devel

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
perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc README ChangeLog
%{perl_vendorarch}/Config
%{perl_vendorarch}/auto/Config
%{_mandir}/man3/*


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.701.0-4
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.701.0-3
+ Revision: 680838
- mass rebuild

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.701.0-2mdv2011.0
+ Revision: 555709
- rebuild

* Fri Feb 19 2010 Jérôme Quelin <jquelin@mandriva.org> 0.701.0-1mdv2010.1
+ Revision: 508048
- update to 0.701

* Wed Dec 23 2009 Jérôme Quelin <jquelin@mandriva.org> 0.601.0-1mdv2010.1
+ Revision: 481707
- update to 0.601

* Sat Jul 18 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.501.0-1mdv2010.0
+ Revision: 397171
- new version

  + Bruno Cornec <bcornec@mandriva.org>
    - Again adapt the group to a valid one this time
    - Fix the Group used
    - Create the first perl-Config-Augeas package from version 0.500 of Dominique Dumont
    - create perl-Config-Augeas


