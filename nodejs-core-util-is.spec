# spec file for package nodejs-nodejs-core-util-is
%{?scl:%scl_package nodejs-nodejs-core-util-is}
%{!?scl:%global pkg_name %{name}}

%global npm_name core-util-is
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-core-util-is
Version:	1.0.1
Release:	2%{?dist}
Summary:	The `util.is*` functions introduced in Node v0.12.
Url:		https://github.com/isaacs/core-util-is
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
Source1:	https://raw.githubusercontent.com/kasicka/core-util-is/1f0d425cbcc2941bb38f5c4a3e3026857db4c239/LICENSE
License:	MIT
#License text can be found in lib/util.js
BuildArch:	noarch
ExclusiveArch:	%{ix86} x86_64 %{arm}} noarch

BuildRequires:	%{?scl_prefix}nodejs-devel
#BuildRequires:	nodejs-packaging

%description
The `util.is*` functions introduced in Node v0.12.

%prep
%setup -q -n package

cp -p %{SOURCE1} .

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json *.js lib/ \
	%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%files
%{nodejs_sitelib}/core-util-is

%doc README.md LICENSE

%changelog
* Tue Sep 22 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.1-2
- Add lib/ to %%install

* Thu Aug 13 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.1-1
- Initial build
