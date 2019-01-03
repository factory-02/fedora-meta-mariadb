Name:                           meta-mariadb
Version:                        1.0.0
Release:                        1%{?dist}
Summary:                        META-package for install and configure MariaDB
License:                        GPLv3

Source10:                       server.custom.cnf

Requires:                       MariaDB-server

%description
META-package for install and configure MariaDB.

# -------------------------------------------------------------------------------------------------------------------- #
# -----------------------------------------------------< SCRIPT >----------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

%install
install -p -d -m 0755 %{buildroot}%{_sysconfdir}/my.cnf.d
install -p -m 0644 %{SOURCE10} \
    %{buildroot}%{_sysconfdir}/my.cnf.d/server.custom.cnf

%files
%config(noreplace) %{_sysconfdir}/my.cnf.d/server.custom.cnf

%changelog
* Wed Jan 02 2019 Kitsune Solar <kitsune.solar@gmail.com> - 1.0.0-1
- Initial build.
