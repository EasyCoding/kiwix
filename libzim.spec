Name: libzim
Version: 4.0.5
Release: 1%{?dist}

License: GPLv2 and ASL 2.0 and BSD
Summary: Reference implementation of the ZIM specification

URL: https://github.com/openzim/%{name}
Source0: %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: xapian-core-devel
BuildRequires: libicu-devel
BuildRequires: gtest-devel
BuildRequires: ninja-build
BuildRequires: zlib-devel
BuildRequires: xz-devel
BuildRequires: gcc-c++
BuildRequires: meson
BuildRequires: gcc

%description
The ZIM library is the reference implementation for the ZIM file
format. It's a solution to read and write ZIM files on many systems
and architectures.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc AUTHORS ChangeLog README.md
%license COPYING
%{_libdir}/%{name}.so.4*

%files devel
%{_includedir}/zim
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Tue Mar 12 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 4.0.5-1
- Initial SPEC release.
