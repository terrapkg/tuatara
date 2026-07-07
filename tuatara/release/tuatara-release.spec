Name:           tuatara-release
Version:        0
Release:        1
Summary:        Release package for Tuatara

License:        MIT
URL:            https://github.com/terrapkg/tuatara
Source0:        tuatara.repo
BuildArch:      noarch

Packager:       Terra Packaging Team <terra@fyralabs.com>

%description
Release package for Tuatara, containing the Tuatara repository configuration.

%prep

%build

%install
install -Dpm644 -t %buildroot%_sysconfdir/zypp/repos.d %SOURCE0

%files
%config(noreplace) %_sysconfdir/zypp/repos.d/tuatara.repo
