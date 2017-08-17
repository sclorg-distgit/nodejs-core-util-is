%{?scl:%scl_package nodejs-delegates}
%{!?scl:%global pkg_name %{name}}

# This macro is needed at the start for building on EL6
%{?nodejs_find_provides_and_requires}

%global barename core-util-is

Name:               %{?scl_prefix}nodejs-core-util-is
Version:            1.0.2
Release:            5%{?dist}
Summary:            The util.is functions introduced in Node v0.12
License:            MIT
URL:                https://www.npmjs.org/package/core-util-is
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz

BuildArch:          noarch
%if 0%{?fedora} >= 19
ExclusiveArch:      %{nodejs_arches} noarch
%else
ExclusiveArch:      %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:      %{?scl_prefix}nodejs-devel

%description
The util.is functions introduced in Node v0.12.

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep --caret

%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/core-util-is
cp -pr package.json lib \
    %{buildroot}%{nodejs_sitelib}/core-util-is

%nodejs_symlink_deps

%files
%doc README.md LICENSE
%{nodejs_sitelib}/core-util-is/

%changelog
* Mon Jul 03 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.2-5
- rh-nodejs8 rebuild

* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.2-4
- Rebuilt with updated metapackage

* Thu Feb 11 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.2-1
- Initial packaging for RHEL
- update to new upstream release

* Tue Jul 22 2014 Ralph Bean <rbean@redhat.com> - 1.0.1-1
- Initial packaging for Fedora.
