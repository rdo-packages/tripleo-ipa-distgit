%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x5d2d1e4fb8d38e6af76c50d53d4fec30cf5ce3da

%global srcname tripleo_ipa
%global rolename tripleo-ipa

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           ansible-%{rolename}
Version:        0.2.2
Release:        1%{?dist}
Summary:        Ansible assets for interacting with FreeIPA on behalf of TripleO

Group:          System Environment/Base
License:        ASL 2.0
URL:            https://opendev.org/x/tripleo-ipa/
Source0:        https://tarballs.opendev.org/x/%{rolename}/%{rolename}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.opendev.org/x/%{rolename}/%{rolename}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
BuildRequires:  openstack-macros
%endif
BuildRequires:  git-core
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr

Requires: ansible-freeipa
Requires: krb5-workstation
Requires: openssl-perl
Requires: python3-ipaclient
Requires: python3-ipalib
Requires: python3-urllib-gssapi
Requires: python3-six
Requires: python3-netaddr
Requires: python3-PyYAML


%description

Ansible assets for interacting with FreeIPA on behalf of TripleO

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
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
* Thu Oct 21 2021 RDO <dev@lists.rdoproject.org> 0.2.2-1
- Update to 0.2.2

