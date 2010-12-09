Summary:	A utility to manage ATA drives 
Name:		ataidle
Version:	2.4
Release:	%mkrel 2
License:	BSD
Group:		System/Kernel and hardware 
Url:		http://www.cran.org.uk/bruce/software/ataidle.php
Source0:	http://www.cran.org.uk/bruce/software/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
ATAidle is a utility to set the power management features of ATA hard drives
in FreeBSD and Linux, including idle and standby timeouts, APM, and
acoustic level settings.

%prep
%setup -q

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_sbindir}
mkdir -p %{buildroot}/%{_mandir}/man8/
install ataidle %{buildroot}/%{_sbindir}
install ataidle.8 %{buildroot}/%{_mandir}/man8

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changelog
%{_sbindir}/ataidle
%{_mandir}/man8/*
