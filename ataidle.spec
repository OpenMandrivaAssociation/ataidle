Summary:	A utility to manage ATA drives 
Name:		ataidle
Version:	2.7.1
Release:	2
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


%changelog
* Sun Feb 19 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 2.7.1-1mdv2012.0
+ Revision: 777327
- update to new version 2.7.1

* Sun Apr 10 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 2.5-1
+ Revision: 652308
- update to new version 2.5

* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 2.4-2mdv2011.0
+ Revision: 616627
- the mass rebuild of 2010.0 packages

* Mon Sep 14 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 2.4-1mdv2010.0
+ Revision: 440608
- update to new version 2.4

* Tue Sep 01 2009 Thierry Vignaud <tv@mandriva.org> 2.3-3mdv2010.0
+ Revision: 423972
- rebuild

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 2.3-2mdv2009.0
+ Revision: 266218
- rebuild early 2009.0 package (before pixel changes)

* Fri Apr 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2.3-1mdv2009.0
+ Revision: 195690
- new version
- compile with %%optflags
- spec file clean

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 0.9-2mdv2008.1
+ Revision: 140690
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Jan 26 2007 Erwan Velu <erwan@mandriva.org> 0.9-2mdv2007.0
+ Revision: 113782
- Rebuild
- Import ataidle

* Wed Nov 16 2005 Lenny Cartier <lenny@mandriva.com> 0.9-1mdk
- 0.9

* Sun Apr 10 2005 Emmanuel Andry <eandry@free.fr> 0.8-1mdk
- New release 0.8
- Fixed summary
- Changed archive gz to bz2

* Thu Jul 01 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.6-2mdk
- fix description

* Thu Jul 01 2004 Erwan Velu <erwan@mandrakesoft.com> 0.6-1mdk
- Initial release

