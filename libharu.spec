%define major %(echo %{version} |cut -d. -f1)
%define libname %mklibname hpdf
%define oldlibname %mklibname hpdf 2
%define develname %mklibname hpdf -d

Summary:	Cross platform software library for generating PDF
Name:		libharu
Version:	2.4.5
Release:	1
Group:		System/Libraries
License:	BSD-like
URL:		https://libharu.sourceforge.net
Source0:	https://github.com/libharu/libharu/archive/refs/tags/v%{version}.tar.gz
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
%rename %{oldlibname}

%description -n %{libname}
HARU is a free, cross platform, open-sourced software library for generating
PDF.

%package -n %{develname}
Summary:	Development headers for libharu 
Group:		Development/C
Requires:	%{libname} >= %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Provides:	libhpdf-devel = %{EVRD}

%description -n %{develname}
HARU is a free, cross platform, open-sourced software library for generating
PDF.

This package contains the static library and header files.

%prep
%autosetup -p1
# fix unversioned shared library
sed -i -e '/add_library(hpdf/aset_target_properties(hpdf PROPERTIES VERSION %{version} SOVERSION %(echo %{version}|cut -d. -f1))' src/CMakeLists.txt

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
%{_libdir}/libhpdf.so
%{_libdir}/libhpdf.so.%{major}*

%files -n %{develname}
%doc CHANGES
%{_includedir}/hpdf*.h
%{_datadir}/%{name}
