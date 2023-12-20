BuildArch:      noarch
Name:           aps-dts-user
Version:        1.1.0
Release:        1
License:        GPLv3
Group:          Unspecified
Summary:        A RPM package containing the APSensing dts user configuration
Distribution:   PhotonPonyOS

URL:            https://github.com/AP-Sensing/aps-dts-user/tree/ppos38
Vendor:         AP Sensing
Packager:       AP Sensing
Provides:       aps-dts-user = %{version}-%{release}

Source0:        %{_sourcedir}/dts.conf

Requires:       (systemd or systemd-standalone-sysusers)

%description
A RPM package containing the APSensing dts user configuration.

%install
install -d -m 755 $RPM_BUILD_ROOT/usr/lib/sysusers.d/
install -m 644 %{_sourcedir}/dts.conf $RPM_BUILD_ROOT/usr/lib/sysusers.d

%files
%attr(644, root, root) /usr/lib/sysusers.d/dts.conf

%changelog
* Wed Dec 20 2023 Fabian Sauter <fabian.sauter+rpm@apsensing.com> - 1.1.0-1
- Using systemd-sysusers for managing the dts user

* Fri Sep 22 2023 Fabian Sauter <fabian.sauter+rpm@apsensing.com> - 1.0.0-2
- Empty ghost file to fix RPM generation

* Fri Sep 22 2023 Fabian Sauter <fabian.sauter+rpm@apsensing.com> - 1.0.0-1
- Initial release
