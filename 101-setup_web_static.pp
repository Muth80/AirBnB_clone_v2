# Puppet manifest for setting up web_static

# Install Nginx if not already installed
package { 'nginx':
  ensure => 'installed',
}

# Create necessary directories
file { ['/data/web_static/releases', '/data/web_static/shared', '/data/web_static/releases/test']:
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

# Create fake HTML file
file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  content => '<html>
                <head>
                </head>
                <body>
                  Holberton School
                </body>
              </html>',
  owner   => 'ubuntu',
  group   => 'ubuntu',
}

# Create symbolic link
file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
  force  => true,
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

# Update Nginx configuration
file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  content => "server {
                listen 80 default_server;
                listen [::]:80 default_server;

                location /hbnb_static/ {
                  alias /data/web_static/current/;
                }
              }",
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  notify  => Service['nginx'],
}

# Restart Nginx service
service { 'nginx':
  ensure => 'running',
  enable => true,
  require => [Package['nginx'], File['/etc/nginx/sites-available/default']],
}
