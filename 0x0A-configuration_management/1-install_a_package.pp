# 1-install_a_package.pp

# Install the flask package from pip3
package { 'Flask':
  ensure => '2.1.0',
  provider => 'pip3',
}