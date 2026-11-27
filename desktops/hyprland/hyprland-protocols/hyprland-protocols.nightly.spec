#? https://src.fedoraproject.org/rpms/hyprland-protocols/blob/rawhide/f/hyprland-protocols.spec

%global realname hyprland-protocols
%global ver 0.8.0
%global commit 825b71324c8b1b49ef138d2e059e60c87bbe758c
%global commit_date 20261127
%global shortcommit %{sub %commit 1 7}

Name:           %realname.nightly
Version:        %ver^%{commit_date}git.%shortcommit
Release:        1%?dist
Summary:        Wayland protocol extensions for Hyprland
BuildArch:      noarch

License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprland-protocols
Source0:        %url/archive/%commit.tar.gz

BuildRequires:  meson
Packager:		madonuko <mado@fyralabs.com>
Provides:		%realname = %evr
Conflicts:		%realname

%description
%{summary}.

%package        devel
Summary:        Wayland protocol extensions for Hyprland
Provides:		%realname-devel = %evr
Conflicts:		%realname-devel

%description    devel
%{summary}.


%prep
%autosetup -p1 -n %realname-%commit


%build
%meson
%meson_build


%install
%meson_install


%files devel
%license LICENSE
%doc README.md
%{_datadir}/pkgconfig/%{realname}.pc
%{_datadir}/%{realname}/
