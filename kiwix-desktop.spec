%define betasuffix 5
%define gitversion beta%{betasuffix}

Name: kiwix-desktop
Version: 2.0
Release: 0.1.%{gitversion}%{?dist}

License: GPLv3+
Summary: Kiwix desktop application

URL: https://github.com/kiwix/%{name}
Source0: %{url}/archive/%{version}-%{gitversion}.tar.gz

Requires: hicolor-icon-theme
Requires: shared-mime-info

BuildRequires: qt5-qtwebengine-devel
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: qt5-qtbase-devel
BuildRequires: kiwix-lib-devel
BuildRequires: mustache-devel
BuildRequires: pugixml-devel
BuildRequires: zimlib-devel
BuildRequires: qt5-linguist
BuildRequires: gcc-c++
BuildRequires: aria2
BuildRequires: gcc

# Required qt5-qtwebengine is not available on some arches.
ExclusiveArch: %{qt5_qtwebengine_arches}

%description
The Kiwix-desktop is a view/manager of zim files for GNU/Linux
and Windows. You can download and view your zim files as you
which.

%prep
%autosetup -n %{name}-%{version}-%{gitversion}
sed -e "/static {/,+2d" -e "/-rpath/d" -e "/git describe/c\DEFINES += GIT_VERSION='%{gitversion}'" -e "s/date/date +\%G-\%m-\%d/" -i %{name}.pro
mkdir -p %{_target_platform}

%build
pushd %{_target_platform}
    %qmake_qt5 PREFIX=%{_prefix} ..
popd

%make_build -C %{_target_platform}

%install
%make_install INSTALL_ROOT=%{buildroot} -C %{_target_platform}

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%doc ChangeLog README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/*.desktop
%{_datadir}/mime/packages/*.xml
%{_metainfodir}/*.appdata.xml

%changelog
* Tue Jun 04 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 2.0-0.1.beta5
- Initial SPEC release.
