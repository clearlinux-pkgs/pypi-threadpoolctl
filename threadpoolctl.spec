#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : threadpoolctl
Version  : 2.1.0
Release  : 1
URL      : https://files.pythonhosted.org/packages/78/e8/e39dc842f512ab5be11efe83160ddb7ad3c0cc1b8d42ce8c0469a0d2b926/threadpoolctl-2.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/78/e8/e39dc842f512ab5be11efe83160ddb7ad3c0cc1b8d42ce8c0469a0d2b926/threadpoolctl-2.1.0.tar.gz
Summary  : threadpoolctl
Group    : Development/Tools
License  : BSD-3-Clause
Requires: threadpoolctl-license = %{version}-%{release}
Requires: threadpoolctl-python = %{version}-%{release}
Requires: threadpoolctl-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
# Thread-pool Controls [![Build Status](https://dev.azure.com/joblib/threadpoolctl/_apis/build/status/joblib.threadpoolctl?branchName=master)](https://dev.azure.com/joblib/threadpoolctl/_build/latest?definitionId=1&branchName=master) [![codecov](https://codecov.io/gh/joblib/threadpoolctl/branch/master/graph/badge.svg)](https://codecov.io/gh/joblib/threadpoolctl)

%package license
Summary: license components for the threadpoolctl package.
Group: Default

%description license
license components for the threadpoolctl package.


%package python
Summary: python components for the threadpoolctl package.
Group: Default
Requires: threadpoolctl-python3 = %{version}-%{release}

%description python
python components for the threadpoolctl package.


%package python3
Summary: python3 components for the threadpoolctl package.
Group: Default
Requires: python3-core
Provides: pypi(threadpoolctl)

%description python3
python3 components for the threadpoolctl package.


%prep
%setup -q -n threadpoolctl-2.1.0
cd %{_builddir}/threadpoolctl-2.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1605903663
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/threadpoolctl
cp %{_builddir}/threadpoolctl-2.1.0/LICENSE %{buildroot}/usr/share/package-licenses/threadpoolctl/8e0a661de07123104e0def1ed841c9c5cedb993c
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/threadpoolctl/8e0a661de07123104e0def1ed841c9c5cedb993c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
