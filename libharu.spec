%define libname %mklibname haru %{version}
%define develname %mklibname haru -d

Summary:	Cross platform software library for generating PDF
Name:		libharu
Version:	2.3.0
Release:	1
Group:		System/Libraries
License:	BSD-like
URL:		http://libharu.sourceforge.net
Source0:	https://github.com/libharu/libharu/archive/%{name}-RELEASE_2_3_0.tar.gz
#Patch0:		libharu-destdir.patch
Patch1:		libharu-2.3.0-shadings.patch
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	file

%description
HARU is a free, cross platform, open-sourced software library for generating
PDF.

%package -n %{libname}
Summary:	Shared libharu library
Group:		System/Libraries

%description -n %{libname}
HARU is a free, cross platform, open-sourced software library for generating
PDF.

%package -n %{develname}
Summary:	Development headers for libharu 
Group:		Development/C
Requires:	%{libname} >= %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{develname}
HARU is a free, cross platform, open-sourced software library for generating
PDF.

This package contains the static library and header files.

%prep
%autosetup -n %{name}-RELEASE_2_3_0 -p1

# fix permissions
find doc -type f | xargs chmod 644

# strip away annoying ^M
find . -type f|xargs file|grep 'CRLF'|cut -d: -f1|xargs perl -p -i -e 's/\r//'
find . -type f|xargs file|grep 'text'|cut -d: -f1|xargs perl -p -i -e 's/\r//'

%build
autoreconf -fi
%configure --enable-debug

%make_build

%install
%make_install

%files -n %{libname}
%{_libdir}/libhpdf-%{version}.so

%files -n %{develname}
%doc CHANGES README
%{_includedir}/hpdf*.h
%{_libdir}/libhpdf.so
