%define major 2
%define libname %mklibname hpdf %{major}
%define develname %mklibname hpdf -d

Summary:	Cross platform software library for generating PDF
Name:		libharu
Version:	2.3.0
Release:	1
Group:		System/Libraries
License:	BSD-like
URL:		http://libharu.sourceforge.net
Source0:	https://github.com/libharu/libharu/archive/%{name}-RELEASE_2_3_0.tar.gz
Patch0:		libharu-RELEASE_2_3_0_cmake.patch
Patch1:		libharu-2.3.0-triangleshading.patch
Patch2:		libharu-2.3.0-smallnumber.patch
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	file
BuildRequires:	cmake

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
%cmake -DLIBHPDF_STATIC=NO -DSHARE_INSTALL_PREFIX=%{_datadir}

%make_build

%install
%make_install -C build

%files -n %{libname}
%{_libdir}/libhpdf.so.%{major}*

%files -n %{develname}
%doc CHANGES README
%{_includedir}/hpdf*.h
%{_libdir}/libhpdf.so
