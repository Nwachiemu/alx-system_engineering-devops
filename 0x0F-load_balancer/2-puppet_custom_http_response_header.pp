# creating a custom HTTP header response, with Puppet

exec { 'apt-update':
  command => '/usr/bin/apt-get update',
}

# Install Nginx package
package { 'nginx':
  ensure => installed,
  require => Exec['apt-update'],
}

# Configure Nginx
file_line {'Header':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  after   => 'listen 80 default_server;',
  line    => '    add_header X-Served-By $hostname;',
  require => Package['nginx'],
}

# Enable and start Nginx service
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
