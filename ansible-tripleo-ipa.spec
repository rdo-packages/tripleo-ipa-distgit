# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_bin python%{pyver}
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build
# End of macros for py2/py3 compatibility

%global srcname tripleo_ipa
%global rolename tripleo-ipa

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           ansible-%{rolename}
Version:        0.2.0
Release:        1%{?dist}
Summary:        Ansible assets for interacting with FreeIPA on behalf of TripleO

Group:          System Environment/Base
License:        ASL 2.0
URL:            https://opendev.org/x/tripleo-ipa/
Source0:        https://tarballs.opendev.org/x/%{rolename}/%{rolename}-%{upstream_version}.tar.gz

BuildArch:      noarch
BuildRequires:  git
BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-setuptools
BuildRequires:  python%{pyver}-pbr

Requires: ansible-freeipa
Requires: krb5-workstation
Requires: openssl-perl
Requires: python%{pyver}-ipaclient
Requires: python%{pyver}-ipalib
Requires: python%{pyver}-urllib-gssapi
Requires: python%{pyver}-six
Requires: python%{pyver}-netaddr
%if %{pyver} == 2
Requires: PyYAML
%else
Requires: python%{pyver}-PyYAML
%endif

%description

Ansible assets for interacting with FreeIPA on behalf of TripleO

%prep
%autosetup -n %{rolename}-%{upstream_version} -S git


%build
%{pyver_build}


%install
export PBR_VERSION=%{version}
export SKIP_PIP_INSTALL=1
%{pyver_install}


%files
%doc README*
%license LICENSE
%{pyver_sitelib}/%{srcname}-*.egg-info
%{_datadir}/ansible/


%changelog
* Mon May 04 2020 Grzegorz Grasza <xek@redhat.com> - 0.2.0-1
- Update to 0.2.0

* Thu Apr 16 2020 Yatin Karel <ykarel@redhat.com> - 0.1.1-1
- Update to 0.1.1

