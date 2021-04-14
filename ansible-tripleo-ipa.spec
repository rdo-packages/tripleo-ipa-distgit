
%global srcname tripleo_ipa
%global rolename tripleo-ipa

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           ansible-%{rolename}
Version:        0.2.1
Release:        1%{?dist}
Summary:        Ansible assets for interacting with FreeIPA on behalf of TripleO

Group:          System Environment/Base
License:        ASL 2.0
URL:            https://opendev.org/x/tripleo-ipa/
Source0:        https://tarballs.opendev.org/x/%{rolename}/%{rolename}-%{upstream_version}.tar.gz

BuildArch:      noarch
BuildRequires:  git
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr

Requires: ansible-freeipa
Requires: krb5-workstation
Requires: python3-urllib-gssapi
Requires: python3-six
Requires: python3-netaddr
Requires: python3-PyYAML

%description

Ansible assets for interacting with FreeIPA on behalf of TripleO

%prep
%autosetup -n %{rolename}-%{upstream_version} -S git


%build
%{py3_build}


%install
export PBR_VERSION=%{version}
export SKIP_PIP_INSTALL=1
%{py3_install}


%files
%doc README*
%license LICENSE
%{python3_sitelib}/%{srcname}-*.egg-info
%{_datadir}/ansible/


%changelog
* Wed Apr 14 2021 Ade Lee <alee@redhat.com> - 0.2.1-1
- Update to 0.2.1
