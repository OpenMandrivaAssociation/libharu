%define	libname %mklibname haru %{version}
%define develname %mklibname haru -d

Summary:	Cross platform software library for generating PDF
Name:		libharu
Version:	2.3.0
Release:	1
Group:		System/Libraries
License:	BSD-like
URL:		http://libharu.sourceforge.net/
Source0:	https://github.com/libharu/libharu/archive/RELEASE_2_3_0.zip
#Patch0:		libharu-destdir.patch
BuildRequires:	libpng-devel
BuildRequires:	zlib-devel
BuildRequires:	file

%description
HARU is a free, cross platform, open-sourced software library for generating
PDF.

%package -n	%{libname}
Summary:	Shared libharu library
Group:		System/Libraries

%description -n	%{libname}
HARU is a free, cross platform, open-sourced software library for generating
PDF.

%package -n	%{develname}
Summary:        Development headers for libharu 
Group:          Development/C
Requires:       %{libname} = %{version}
Provides:	%{name}-devel = %{version}

%description -n	%{develname}
HARU is a free, cross platform, open-sourced software library for generating
PDF.

This package contains the static library and header files.

%prep

%setup -qn libharu-RELEASE_2_3_0
%autopatch -p1

# fix permissions
find doc -type f | xargs chmod 644

# strip away annoying ^M
find . -type f|xargs file|grep 'CRLF'|cut -d: -f1|xargs perl -p -i -e 's/\r//'
find . -type f|xargs file|grep 'text'|cut -d: -f1|xargs perl -p -i -e 's/\r//'

%build
%serverbuild

autoreconf -fiv
%configure --enable-debug
%make

%install

%makeinstall_std

%files -n %{libname}
%doc CHANGES README
%{_libdir}/libhpdf-%{version}.so

%files -n %{develname}
%{_includedir}/hpdf*.h
%{_libdir}/libhpdf.so
