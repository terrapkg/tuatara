Name:           terra-appstream-helper
Version:        0.1.10
Release:        3%?dist
Summary:        Scripts and RPM macros to help with AppStream metadata generation for Terra
License:        GPL-3.0-or-Later
URL:            https://github.com/terrapkg/appstream-helper
Source:         %{url}/archive/refs/tags/v%version.tar.gz
BuildArch:      noarch
Requires:       python3-%{name} = %{evr}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  %pythons

Packager:       Terra Packaging Team <terra@fyralabs.com>

%description
%{summary}.

%package -n     python3-%{name}
Summary:        Python files for %{name}
Requires:       %{name} = %{evr}
BuildArch:      noarch

%description -n python3-%{name}
Python files needed for %{name}.

%prep
%autosetup -n appstream-helper-%{version}


%build
%pyproject_wheel


%install
%pyproject_install

%files
%license LICENSE
%doc README.md
%{_bindir}/terra-appstream-helper
%{_rpmmacrodir}/macros.terra-appstream


%files -n python3-%{name}
%{python_sitelib}/terra_appatream_helper*/
%pycache_only %{python_sitelib}/__pycache__/*
