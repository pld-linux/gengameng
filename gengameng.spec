Summary:	A Generic Game Engine library for 2D double-buffering animation
Summary(pl.UTF-8):	Biblioteka ogólnego silnika gier z podwójnie buforowaną animacją 2D
Name:		gengameng
Version:	4.1
Release:	4
License:	GPL
Group:		X11/Libraries
Source0:	http://www3.sympatico.ca/sarrazip/dev/%{name}-%{version}.tar.gz
# Source0-md5:	112322dbdc6684717cdfd7c61d225655
Patch0:		%{name}-config.patch
Patch1:		%{name}-link.patch
Patch2:		%{name}-acfix.patch
URL:		http://sarrazip.com/dev/burgerspace.html
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	SDL_image-devel >= 1.2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.4d
Requires:	SDL >= 1.2.0
Requires:	SDL_image >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Generic Game Engine library suitable for BurgerSpace and Cosmosmash.

%description -l pl.UTF-8
Biblioteka ogólnego silnika gier wykorzystana w grach BurgerSpace i
Cosmosmash.

%package devel
Summary:	C++ header files for the gengameng library
Summary(pl.UTF-8):	Pliki nagłówkowe C++ dla biblioteki gengameng
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	SDL-devel >= 1.2.0
Requires:	SDL_image-devel >= 1.2.0
Requires:	libstdc++-devel

%description devel
C++ header files for the Generic Game Engine ("gengameng") library
for 2D double-buffering animation.

%description devel -l pl.UTF-8
Pliki nagłówkowe C++ dla biblioteki ogólnego silnika gier
("gengameng") z podwójnie buforowaną animacją 2D.

%package static
Summary:	Static gengameng library
Summary(pl.UTF-8):	Statyczna biblioteka gengameng
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gengameng library.

%description static -l pl.UTF-8
Statyczna biblioteka gengameng.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
# supplied libtool is broken (C++)
%{__libtoolize}
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
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
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/libgengameng.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gengameng-config
%attr(755,root,root) %{_libdir}/libgengameng.so
%{_libdir}/libgengameng.la
%{_includedir}/gengameng
%{_aclocaldir}/gengameng.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/libgengameng.a
