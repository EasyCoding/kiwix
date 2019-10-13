Name: kiwix-lib
Version: 8.1.0
Release: 1%{?dist}

License: GPLv3+
Summary: Common code base for all Kiwix ports

URL: https://github.com/kiwix/%{name}
Source0: %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: mustache-devel
BuildRequires: pugixml-devel
BuildRequires: libcurl-devel
BuildRequires: libicu-devel
BuildRequires: zimlib-devel
BuildRequires: gtest-devel
BuildRequires: ninja-build
BuildRequires: gcc-c++
BuildRequires: meson
BuildRequires: cmake
BuildRequires: aria2
BuildRequires: gcc

%description
The Kiwix library provides the Kiwix software core. It contains
the code shared by all Kiwix ports.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -p1
sed -e "s/, 'werror=true'//" -i meson.build

%build
%meson
%meson_build

%install
%meson_install

# Fedora's version of pugixml package does not provide pkg-config file.
sed -e 's/pugixml //g' -i %{buildroot}%{_libdir}/pkgconfig/kiwix.pc

%files
%doc AUTHORS ChangeLog README.md
%license COPYING
%{_bindir}/kiwix-compile-resources
%{_libdir}/libkiwix.so.8*

%files devel
%{_includedir}/kiwix
%{_libdir}/libkiwix.so
%{_libdir}/pkgconfig/kiwix.pc

%changelog
* Sun Oct 13 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 8.1.0-1
- Updated to version 8.1.0.

* Sat Aug 17 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 5.2.0-1
- Updated to version 5.2.0.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 04 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 5.1.0-1
- Updated to version 5.1.0.

* Tue Apr 23 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 5.0.0-1
- Updated to version 5.0.0.

* Wed Apr 10 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 4.1.0-1
- Updated to version 4.1.0.

* Tue Mar 12 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 4.0.1-1
- Initial SPEC release.
