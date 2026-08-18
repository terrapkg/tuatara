%global keydir %{_prefix}/lib/rpm/gnupg/keys/

Name:      tuatara-build-key
Version:   1.0
Release:   69.1
Summary:   GPG keys to verify Tuatara packages
License:   GPL-3.0-or-later
Group:     System/Packages
Source0:   gpg-pubkey-tuatara-tumbleweed.asc
# Another known name for GPG keys on openSUSE, a la Packman.
Provides:  rpmkey-tuatara = %{?epoch:%{epoch}:}%{version}-%{release}
Packager:  Tuatara Packaging Team <terra@fyralabs.com>
BuildArch: noarch

%description
This package contains the GPG keys that are used to sign the
Tuatara RPM packages.

%prep
%setup -qcT

%build

%install
mkdir -p %{buildroot}%{keydir}
for key in %{_sourcedir}/gpg-pubkey-*; do
  install -m 644 $key -t %{buildroot}%{keydir}
done

%files
%defattr(644,root,root)
%{keydir}/gpg-pubkey-*.asc

%changelog
* Mon Jul 20 2026 Gilver E. <roachy@fyralabs.com> - 1.0-69.1
- Add Tuatara build keys
