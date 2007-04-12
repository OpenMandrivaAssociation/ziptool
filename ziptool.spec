Summary:	Tools for Iomega JAZ and ZIP drives
Name:		ziptool
Version:	1.4.0
Release:	%mkrel 4
License:	GPL
Group:		File tools
Url:		http://wolfpack.twu.net/utilities.html#ziptool
Source0:	ftp://wolfpack.twu.net/users/wolfpack/%{name}-%{version}.tar.bz2
#Patch0:	%{name}-1.2-compile.patch.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
ExcludeArch:	ppc
BuildRequires:	kernel-source

%description
Medium protection is done by software for Iomega's JAZ and ZIP drives.
jaztool and ziptool make this features available for Linux.

%prep
%setup -q
#%patch0 -p1
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


* Tue May 10 2005 Franck Villaume <fvill@mandriva.org> 1.4.0-3mdk
- fix the buildrequires....

* Sat Aug 02 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.4.0-2mdk
- rebuild

* Mon Jun 16 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 1.4.0-1mdk
- 1.4.0
- added Url, updated source URL
- cleaned up excessive whitespaces:o)
- quiet setup
- drop P0
- drop make install since it requires root, don't bother to patch it,
  rather do it ourself
- cosmetics

* Mon Aug 26 2002 David BAUDENS <baudens@mandrakesoft.com> 1.3-7mdk
- Rebuild

* Thu Aug 23 2001 Etienne Faure <etienne@mandrakesoft.com> 1.3-6mdk
- rebuild

* Mon Jan 22 2001 David BAUDENS <baudens@mandrakesoft.com> 1.3-5mdk
- ExcludeArch: ppc

* Thu Sep 21 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.3-4mdk
- buildrelease

* Fri Jul 28 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.3-3mdk
- BM

* Thu May 04 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.3-2mdk
- fix group
- fix files section
- bzip2 patch

* Mon Feb 14 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.3-1mdk
- used srpm provided by  Stefan van der Eijk <s.vandereijk@chello.nl>
- Stefan van der Eijk update to 1.3

* Fri Feb 11 2000 Stefan van der Eijk <s.vandereijk@chello.nl>
- 1.3
 
* Wed Jun 24 1998 Peter Soos <sp@osb.hu>
- Using %attr to build the package as an ordinary user.
- Using uncompressed man pages, because RedHat's helptool couldn't use it.   
