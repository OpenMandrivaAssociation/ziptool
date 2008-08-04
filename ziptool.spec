Summary:	Tools for Iomega JAZ and ZIP drives
Name:		ziptool
Version:	1.4.0
Release:	%mkrel 7
License:	GPL
Group:		File tools
Url:		http://wolfpack.twu.net/utilities.html#ziptool
Source0:	ftp://wolfpack.twu.net/users/wolfpack/%{name}-%{version}.tar.bz2
#Patch0:	%{name}-1.2-compile.patch.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
#ExcludeArch:	ppc
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
