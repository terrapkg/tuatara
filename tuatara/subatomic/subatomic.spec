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
go mod vendor


%build
%dnl %goprep %{import_path}
%dnl %gobuild server
%dnl %gobuild subatomic-cli
go build -o out/subatomic -mod=vendor -buildmode=pie server
go build -o out/subatomic-cli -mod=vendor -buildmode=pie subatomic-cli


%install
#goinstall
#gosrc

install -Dm755 out/* -t %buildroot%_bindir

#gofilelist

%dnl %check
%dnl %gotest %{import_path}

%files
%{_bindir}/subatomic


%changelog
* Fri Sep 30 2022 Cappy Ishihara <cappy@cappuchino.xyz> - 0.1.0.200283ccd3cf7c90b6a9be565ce6ff52bdec977e-1
- Intial release
