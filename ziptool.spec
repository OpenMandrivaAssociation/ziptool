Summary:	Tools for Iomega JAZ and ZIP drives
Name:		ziptool
Version:	1.4.0
Release:	%mkrel 6
License:	GPL
Group:		File tools
Url:		http://wolfpack.twu.net/utilities.html#ziptool
Source0:	ftp://wolfpack.twu.net/users/wolfpack/%{name}-%{version}.tar.bz2
Patch0:		ziptool-1.4.0-build-fix-private-scsi-define.patch
Patch1:		ziptool-1.4.0-format-security.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	kernel-source-latest

%description
Medium protection is done by software for Iomega's JAZ and ZIP drives.
jaztool and ziptool make this features available for Linux.

%prep
%setup -q
%patch0 -p1 -b .build-fix-private-scsi-define
%patch1 -p1 -b .format-security
%{__gzip} -d %{name}.1.gz

%build
%make CFLAGS="$RPM_OPT_FLAGS -s"

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__install} -m755 %{name} -D $RPM_BUILD_ROOT%{_bindir}/%{name}
%{__install} -m644 %{name}.1 -D $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README 
%{_mandir}/man1/%{name}.1*
%defattr(755,root,root,755)
%{_bindir}/%{name}


%changelog
* Thu Oct 08 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 1.4.0-6mdv2010.0
+ Revision: 456208
- BuildRequires main kernel source.
- Fix build with current kernel sources.
- Fix build with -Wformat -Werror=format-security

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild
    - rebuild
    - rebuild
    - rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.4.0-5mdv2008.1
+ Revision: 136633
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 22 2007 Olivier Thauvin <nanardon@mandriva.org> 1.4.0-5mdv2008.0
+ Revision: 68893
- rebuild


* Fri Jul 14 2006 Olivier Thauvin <nanardon@mandriva.org>
+2006-07-14 20:26:06 (41217)
- rebuild

* Fri Jul 14 2006 Olivier Thauvin <nanardon@mandriva.org>
+2006-07-14 20:20:48 (41212)
Import ziptool

* Tue May 10 2005 Franck Villaume <fvill@mandriva.org> 1.4.0-3mdk
- fix the buildrequires....

* Sat Aug 02 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.4.0-2mdk
- rebuild

