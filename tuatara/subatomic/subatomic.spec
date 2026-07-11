%define debug_package %{nil}
%global import_path github.com/FyraLabs/subatomic

Name:           subatomic
Version:        0.15.0
Release:        1%{?dist}
Summary:        A modern package delivery system

License:        MIT
URL:            https://github.com/FyraLabs/subatomic
Source0:        %url/archive/refs/tags/v%version.tar.gz

BuildRequires:  golang-packaging
BuildRequires:  git-core
BuildRequires:  gcc
Requires:       createrepo_c

%description
Subatomic is a package delivery system which supports multiple package formats.
It manages a repository of packages, handling updating, signing, and other
tasks.

%package cli
Summary:        Client for Subatomic repo manager

%description cli
Client for Subatomic repo manager

%files cli
%{_bindir}/subatomic-cli

%prep
%autosetup
go mod download


%build
%goprep %{import_path}
%gobuild server
%gobuild subatomic-cli


%install
install -Dm755 go/bin/server %{buildroot}%{_bindir}/subatomic
install -Dm755 go/bin/subatomic-cli %{buildroot}%{_bindir}/subatomic-cli


%files
%{_bindir}/subatomic


%changelog
* Fri Sep 30 2022 Cappy Ishihara <cappy@cappuchino.xyz> - 0.1.0.200283ccd3cf7c90b6a9be565ce6ff52bdec977e-1
- Intial release
