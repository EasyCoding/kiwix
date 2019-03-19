%global appname Mustache

Name: mustache
Version: 3.2.1
Release: 1%{?dist}

License: Boost
Summary: Mustache text templates for modern C++

URL: https://github.com/kainjow/%{appname}
Source0: %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: ninja-build
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: gcc

BuildArch: noarch

%description
Text templates implementation for modern C++ (requires C++11).

%package devel
Summary: Development files for %{name}
Provides: %{name}-static = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
The %{name}-devel package contains C++ headers for developing
applications that use %{name}.

%prep
%autosetup -n %{appname}-%{version}
mkdir -p %{_target_platform}
sed -e '/-Werror/d' -i CMakeLists.txt

%build
pushd %{_target_platform}
    %cmake -G Ninja \
    ..
popd
%ninja_build -C %{_target_platform}

%check
pushd %{_target_platform}
    ctest --output-on-failure
popd

%install
%{__mkdir_p} %{buildroot}%{_includedir}
%{__install} -m 0644 -p %{name}.hpp %{buildroot}%{_includedir}

%files devel
%doc README.md
%license LICENSE
%{_includedir}/%{name}.hpp

%changelog
* Tue Mar 12 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 3.2.1-1
- Initial SPEC release.
