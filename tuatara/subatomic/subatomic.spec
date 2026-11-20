%undefine __brp_mangle_shebangs
%global rustflags_opt_level 3

Name:           subatomic
Version:        1.1.5
Release:        1%{?dist}
Summary:        A modern package delivery system
SourceLicense:  AGPL-3.0-or-later
License:        (ISC AND (Apache-2.0 OR ISC)) AND (BSD-3-Clause OR MIT OR Apache-2.0) AND bzip2-1.0.6 AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR BSL-1.0) AND (MIT OR Apache-2.0 OR Zlib) AND AGPL-3.0-or-later AND (0BSD OR MIT OR Apache-2.0) AND Zlib AND (ISC AND (Apache-2.0 OR ISC) AND Apache-2.0 AND MIT AND BSD-3-Clause AND (Apache-2.0 OR ISC OR MIT) AND (Apache-2.0 OR ISC OR MIT-0)) AND MIT AND (MIT OR Apache-2.0 OR BSD-1-Clause) AND ((MIT OR Apache-2.0) AND Unicode-3.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND Unicode-3.0 AND MPL-2.0+ AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND (Apache-2.0 OR BSL-1.0 OR MIT) AND MIT AND BSD-3-Clause AND ISC AND ((Apache-2.0 OR MIT) AND BSD-3-Clause) AND BSD-3-Clause AND (MIT OR Apache-2.0 OR LGPL-2.1-or-later) AND (Unlicense OR MIT)
URL:            https://github.com/FyraLabs/subatomic
Source0:        %url/archive/refs/tags/v%version.tar.gz

BuildRequires:  cargo-packaging
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libzstd)

Packager:       Owen Zimmerman <owen@fyralabs.com>

%description
Subatomic is a package delivery system which supports multiple package formats.
It manages a repository of packages, handling updating, signing, and other
tasks.

%package -n satm
Version:        1.1.0
Summary:        CLI web client for subatomic-server

%description -n satm
CLI web client for subatomic-server.

%package -n kiritan
Version:        1.1.1
Summary:        Next-generation modern RPM repository metadata generator

%description -n kiritan
Next-generation modern RPM repository metadata generator

%prep
%autosetup
%global _cargo_home %{rpmbuilddir}%{?buildsubdir:/%{buildsubdir}}/.cargo 
%{__rm} -rf {.cargo/,%{_cargo_home}/} 
%global _rustup_home %{rpmbuilddir}/.rustup 
%global __cargo . %{_cargo_home}/env && /usr/bin/env CARGO_HOME=%{_cargo_home} RUSTUP_HOME=%{_rustup_home} RUSTFLAGS='%{terra_rustflags}' %{_cargo_home}/bin/cargo 
%global __rustc %{_cargo_home}/bin/rustc 
%global __rustdoc %{_cargo_home}/bin/rustdoc 
%dnl /usr/bin/env CARGO_HOME=%{_cargo_home} RUSTUP_HOME=%{_rustup_home} RUSTUP_INIT_SKIP_PATH_CHECK=yes rustup-init --default-toolchain nightly -y -q --no-modify-path 
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs > rustup-install.sh
chmod +x rustup-install.sh
/usr/bin/env CARGO_HOME=%{_cargo_home} RUSTUP_HOME=%{_rustup_home} RUSTUP_INIT_SKIP_PATH_CHECK=yes ./rustup-install.sh -y
. %{_cargo_home}/env 
%bcond rust_nightly 1

for crate in kiritan libsubatomic satm; do
pushd crates/$crate
%{__cargo} fetch --locked
popd
done

%cargo_prep_online

%build
export ZSTD_SYS_USE_PKG_CONFIG=1
%cargo_build

for crate in kiritan satm; do
pushd crates/$crate
%cargo_build
popd
done

%install
install -Dm 755 target/rpm/subatomic    %{buildroot}%{_bindir}/subatomic
install -Dm 755 target/rpm/satm         %{buildroot}%{_bindir}/satm
install -Dm 755 target/rpm/kiritan      %{buildroot}%{_bindir}/kiritan
cargo tree --format "{l}: {p}" | sed -e "s: ($(pwd)[^)]*)::g" -e "s: / :/:g" -e "\|/.*:|{s|/| OR |}" | sort -u > LICENSE.dependencies
pushd crates/libsubatomic
cargo tree --format "{l}: {p}" | sed -e "s: ($(pwd)[^)]*)::g" -e "s: / :/:g" -e "\|/.*:|{s|/| OR |}" | sort -u > LICENSE-libsubatomic.dependencies
popd
for crate in kiritan satm; do
mkdir -p license_${crate}
pushd crates/$crate
cargo tree --format "{l}: {p}" | sed -e "s: ($(pwd)[^)]*)::g" -e "s: / :/:g" -e "\|/.*:|{s|/| OR |}" | sort -u > LICENSE.dependencies
popd
done

%files
%doc README.md docs/*
%license LICENSE LICENSE.dependencies LICENSE-libsubatomic.dependencies
%{_bindir}/subatomic

%files -n satm
%license LICENSE license_satm/LICENSE.dependencies
%{_bindir}/satm

%files -n kiritan
%license LICENSE license_kiritan/LICENSE.dependencies
%{_bindir}/kiritan

%changelog
* Thu Sep 10 2026 Owen Zimmerman <owen@fyralabs.com> - 1.0.0-1
- Convert to rust format

* Fri Sep 30 2022 Cappy Ishihara <cappy@cappuchino.xyz> - 0.1.0.200283ccd3cf7c90b6a9be565ce6ff52bdec977e-1
- Intial release
