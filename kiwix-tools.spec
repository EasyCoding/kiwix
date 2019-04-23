Name: kiwix-tools
Version: 1.2.1
Release: 1%{?dist}

License: GPLv3+
Summary: Common code base for all Kiwix ports

URL: https://github.com/kiwix/%{name}
Source0: %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0: %{name}-fix-flags.patch

BuildRequires: libmicrohttpd-devel
BuildRequires: kiwix-lib-devel
BuildRequires: pugixml-devel
BuildRequires: ninja-build
BuildRequires: zlib-devel
BuildRequires: gcc-c++
BuildRequires: meson
BuildRequires: gcc

%description
The Kiwix tools is a collection of Kiwix related command line
tools.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%doc AUTHORS Changelog README.md
%license COPYING
%{_bindir}/kiwix*
%{_mandir}/man1/kiwix*.1*
%{_mandir}/*/man1/kiwix*.1*

%changelog
* Tue Apr 23 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 1.2.1-1
- Updated to version 1.2.1.

* Wed Apr 10 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 1.1.0-1
- Updated to version 1.1.0.

* Tue Mar 12 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 1.0.0-1
- Initial SPEC release.
