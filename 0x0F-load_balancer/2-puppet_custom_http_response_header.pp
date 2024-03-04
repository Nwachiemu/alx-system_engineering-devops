# Define custom HTTP header name and value
# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Configure Nginx
file_line {'Adding_Header':
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
