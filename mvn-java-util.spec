#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-java-util
Version  : 1.9.0
Release  : 1
URL      : https://repo1.maven.org/maven2/com/cedarsoftware/java-util/1.9.0/java-util-1.9.0.jar
Source0  : https://repo1.maven.org/maven2/com/cedarsoftware/java-util/1.9.0/java-util-1.9.0.jar
Source1  : https://repo1.maven.org/maven2/com/cedarsoftware/java-util/1.9.0/java-util-1.9.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-java-util-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-java-util package.
Group: Data

%description data
data components for the mvn-java-util package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/cedarsoftware/java-util/1.9.0
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/com/cedarsoftware/java-util/1.9.0/java-util-1.9.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/cedarsoftware/java-util/1.9.0
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/com/cedarsoftware/java-util/1.9.0/java-util-1.9.0.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/com/cedarsoftware/java-util/1.9.0/java-util-1.9.0.jar
/usr/share/java/.m2/repository/com/cedarsoftware/java-util/1.9.0/java-util-1.9.0.pom
