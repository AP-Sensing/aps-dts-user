BuildArch:      noarch
Name:           aps-dts-user
Version:        1.0.0
Release:        2
License:        GPLv3
Group:          Unspecified
Summary:        A RPM package containing the APSensing dts user configuration
Distribution:   PhotonPonyOS

URL:            https://github.com/AP-Sensing/ftdi-d2xx/tree/ppos38
Vendor:         AP Sensing
Packager:       AP Sensing
Provides:       aps-dts-user = %{version}-%{release}

Requires(pre):  shadow-utils
Requires(pre):  coreutils

%description
A RPM package containing the APSensing dts user configuration.

%pre
# useradd
# --system: create a system account
# --create-home: create the user's home directory
# --home-dir: home directory of the new account
# --shell: login shell of the new account
# --comment: GECOS field of the new account
getent passwd dts > /dev/null || useradd --system --create-home --home-dir /home/dts --shell /usr/bin/bash --comment "Main dts user account" dts

%files
# Add an empty ghost file to ensure the RPM gets generated.
%ghost /home/dts

%changelog
* Fri Sep 22 2023 Fabian Sauter <fabian.sauter+rpm@apsensing.com> - 1.0.0-2
- Empty ghost file to fix RPM generation

* Fri Sep 22 2023 Fabian Sauter <fabian.sauter+rpm@apsensing.com> - 1.0.0-1
- Initial release
