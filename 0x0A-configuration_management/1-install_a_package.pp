# 1-install_a_package.pp

# Install the python3-pip package
package { 'python3-pip':
  ensure => installed,
}

# Install the flask package from pip3
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}
