Name:           tuatara-repos
Version:        %(date -u "+%Y%m%d")
Release:        1
Summary:        Release package for Tuatara

License:        GPL-3.0-or-later
URL:            https://github.com/terrapkg/tuatara
Source0:        tuatara.repo
Source1:        tuatara-source.repo
Requires:       tuatara-build-key
Obsoletes:      tuatara-release < %{version}-%{release}
# SUSE gives repo packages architectures but we don't need to do this.
BuildArch:      noarch

Packager:       Tuatara Packaging Team <terra@fyralabs.com>

%description
Release package for Tuatara, containing the Tuatara repository configuration.

%prep
%setup -qcT

%build

%install
for repo in %{_sourcedir}/*.repo; do
  install -Dpm644 $repo -t %buildroot%_sysconfdir/zypp/repos.d
done

%files
%config(noreplace) %_sysconfdir/zypp/repos.d/tuatara.repo
%config(noreplace) %_sysconfdir/zypp/repos.d/tuatara-source.repo
