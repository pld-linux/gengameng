Summary:	A Generic Game Engine library for 2D double-buffering animation
Name:		gengameng
Version:	4.1
Release:	1
License:	GPL
Group:		X11/Libraries
Source0:	http://www3.sympatico.ca/sarrazip/dev/%{name}-%{version}.tar.gz
Patch0:		%{name}-config.patch
URL:		http://sarrazip.com/dev/burgerspace.html
BuildRequires:	SDL_image-devel
BuildRequires:	libstdc++-devel
PreReq:		/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix	/usr/X11R6

%description
Generic Game Engine library suitable for BurgerSpace and Cosmosmash.

%package devel
Summary: 	C++ header files for the gengameng library
Group: 		X11/Development/Libraries
Requires:	%{name} = %version}

%description devel
C++ header files for the Generic Game Engine ("gengameng") library
for 2D double-buffering animation.

%package static
Summary: 	Static gengameng library
Group: 		X11/Development/Libraries
Requires:	%{name}-devel = %version}

%description static
Static gengameng library.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--enable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	aclocaldir=%{_aclocaldir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgengameng.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gengameng-config
%attr(755,root,root) %{_libdir}/libgengameng.so
%attr(755,root,root) %{_libdir}/libgengameng.la
%{_includedir}/gengameng
%{_aclocaldir}/gengameng.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/libgengameng.a
