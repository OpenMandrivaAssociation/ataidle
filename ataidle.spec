%define name ataidle
%define version 0.9
%define release %mkrel 2

Summary: A utility to manage ATA drives 
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.cran.org.uk/bruce/software/%{name}-%{version}.tar.bz2
License: BSD
Group: System/Kernel and hardware 
Url: http://www.cran.org.uk/bruce/software/ataidle.php


%description
ATAidle is a utility to set the power management features of ATA hard drives
in FreeBSD and Linux, including idle and standby timeouts, APM, and
acoustic level settings.

%prep
%setup -q

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_sbindir}
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man8/
install $RPM_BUILD_DIR/%{name}-%{version}/ataidle $RPM_BUILD_ROOT/%{_sbindir}
install $RPM_BUILD_DIR/%{name}-%{version}/ataidle.8 $RPM_BUILD_ROOT/%{_mandir}/man8


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_sbindir}/ataidle
%{_mandir}/man8/*


