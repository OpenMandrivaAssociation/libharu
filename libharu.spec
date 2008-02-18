%define	major 1
%define	libname %mklibname haru %{major}
%define develname %mklibname haru -d

Summary:	Free, cross platform, open-sourced software library for generating PDF
Name:		libharu
Version:	2.0.8
Release:	%mkrel 3
Group:		System/Libraries
License:	BSD-like
URL:		http://libharu.sourceforge.net/
Source0:	http://surfnet.dl.sourceforge.net/sourceforge/libharu/libharu_2_0_8.tgz
Patch0:		libharu-destdir.patch
BuildRequires:	libpng-devel
BuildRequires:	zlib-devel
BuildRequires:	file
BuildRoot:	%{_tmppath}/%{name}-%{version}-build

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

%setup -q
%patch0

# fix permissions
find doc -type f | xargs chmod 644

# strip away annoying ^M
find . -type f|xargs file|grep 'CRLF'|cut -d: -f1|xargs perl -p -i -e 's/\r//'
find . -type f|xargs file|grep 'text'|cut -d: -f1|xargs perl -p -i -e 's/\r//'

%build
%serverbuild

./configure --shared --prefix=%{_usr}

%make

%install

%makeinstall_std LIBDIR=%{_lib}

%post -n %{libname} -p /sbin/ldconfig

%postun	-n %{libname} -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc doc/* CHANGES README TODO
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/hpdf*.h
%{_libdir}/*.so
