Summary:	A Generic Game Engine library for 2D double-buffering animation
Name:		gengameng
Version:	4.1
Release:	1
License:	GPL
Group:		X11/Libraries
Source0:	http://www3.sympatico.ca/sarrazip/dev/%{name}-%{version}.tar.gz
Patch0:		%{name}-config.patch
URL:		http://sarrazip.com/dev/burgerspace.html
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	nas-devel
Requires:	nas
Requires:	SDL >= 1.2.0
Requires:	SDL_image >= 1.2.0
PreReq:		/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix	/usr/X11R6

%description
Generic Game Engine library suitable for BurgerSpace and Cosmosmash.

%package devel
Summary: 	C++ header files for the gengameng library
Group: 		X11/Development/Libraries

%description devel
C++ header files for the Generic Game Engine ("gengameng") library
for 2D double-buffering animation.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install
install -d $RPM_BUILD_ROOT/%{_aclocaldir}
mv $RPM_BUILD_ROOT/%{_datadir}/aclocal/* $RPM_BUILD_ROOT/%{_aclocaldir} 

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgengameng.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gengameng-config
%dir %{_includedir}/gengameng
%{_includedir}/gengameng/*
%{_aclocaldir}/gengameng.m4
