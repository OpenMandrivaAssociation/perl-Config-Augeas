%define perlvendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)

Name:           perl-Config-Augeas
Version:        0.500
Release:        %mkrel 1
Summary:        Edit configuration files through Augeas C library
License:        LGPLv2+
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Config-Augeas/
Source0:        http://www.cpan.org/modules/by-module/Config/Config-Augeas-%{version}.tar.gz
Patch0:			gcc-fix.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl-devel
BuildRequires:  libaugeas-devel

%description
Augeas is a library and command line tool that focuses on the most basic
problem in handling Linux configurations programmatically: editing actual
configuration files in a controlled manner.

%prep
%setup -q -n Config-Augeas-%{version}
%patch0

%build
%{__perl} Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS" destdir=${RPM_BUILD_ROOT}
./Build

%install
rm -rf $RPM_BUILD_ROOT

./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find ${RPM_BUILD_ROOT} -type f -name perllocal.pod -o -name .packlist -o -name '*.bs' -a -size 0 | xargs rm -f
find ${RPM_BUILD_ROOT} -type d -depth | xargs rmdir --ignore-fail-on-non-empty

#%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc ChangeLog README
%{perlvendorlib}/*
%{_mandir}/man3/*
