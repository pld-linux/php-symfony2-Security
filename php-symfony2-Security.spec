%define		pearname	Security
%define		php_min_version 5.3.3
%include	/usr/lib/rpm/macros.php
Summary:	Symfony2 Security Component
Name:		php-symfony2-Security
Version:	2.3.4
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	http://pear.symfony.com/get/%{pearname}-%{version}.tgz
# Source0-md5:	c8865a5a757454cf11cbb5fb4c00a886
URL:		http://pear.symfony.com/package/Security/
BuildRequires:	php-channel(pear.symfony.com)
BuildRequires:	php-pear-PEAR >= 1:1.4.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php-channel(pear.symfony.com)
Requires:	php-pear >= 4:1.3.10
Requires:	php-symfony2-EventDispatcher >= 2.1
Requires:	php-symfony2-HttpFoundation >= 2.1
Requires:	php-symfony2-HttpKernel >= 2.1
Suggests:	php-symfony2-ClassLoader
Suggests:	php-symfony2-Finder
Suggests:	php-symfony2-Form
Suggests:	php-symfony2-Routing
Suggests:	php-symfony2-Validator
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides an infrastructure for sophisticated authorization systems.

%prep
%pear_package_setup

# no packaging of tests
mv .%{php_pear_dir}/Symfony/Component/%{pearname}/Tests .
mv .%{php_pear_dir}/Symfony/Component/%{pearname}/phpunit.xml.dist .

# fixups
mv docs/%{pearname}/Symfony/Component/%{pearname}/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md install.log
%{php_pear_dir}/.registry/.channel.*/*.reg
%dir %{php_pear_dir}/Symfony/Component/Security
%{php_pear_dir}/Symfony/Component/Security/*.php
%{php_pear_dir}/Symfony/Component/Security/Acl
%{php_pear_dir}/Symfony/Component/Security/Core
%{php_pear_dir}/Symfony/Component/Security/Http

%dir %{php_pear_dir}/Symfony/Component/Security/Resources
%dir %{php_pear_dir}/Symfony/Component/Security/Resources/translations
%lang(ar) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.ar.xlf
%lang(ca) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.ca.xlf
%lang(cs) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.cs.xlf
%lang(da) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.da.xlf
%lang(de) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.de.xlf
%lang(el) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.el.xlf
%lang(en) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.en.xlf
%lang(es) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.es.xlf
%lang(fa) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.fa.xlf
%lang(fr) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.fr.xlf
%lang(gl) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.gl.xlf
%lang(hu) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.hu.xlf
%lang(it) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.it.xlf
%lang(lb) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.lb.xlf
%lang(nl) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.nl.xlf
%lang(no) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.no.xlf
%lang(pl) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.pl.xlf
%lang(pt_BR) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.pt_BR.xlf
%lang(pt_PT) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.pt_PT.xlf
%lang(ro) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.ro.xlf
%lang(ru) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.ru.xlf
%lang(sk) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.sk.xlf
%lang(sl) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.sl.xlf
%lang(sr@cyrillic) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.sr_Cyrl.xlf
%lang(sr@latin) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.sr_Latn.xlf
%lang(sv) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.sv.xlf
%lang(tr) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.tr.xlf
%lang(uk) %{php_pear_dir}/Symfony/Component/Security/Resources/translations/security.ua.xlf
