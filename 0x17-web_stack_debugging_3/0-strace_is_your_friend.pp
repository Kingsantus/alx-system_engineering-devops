# 0-strace_is_your_friend.pp

# Define the Apache service
service { 'apache2':
  ensure => 'running',
  enable => true,
}

# Run strace and identify the issue
exec { 'strace_apache':
  command  => 'sudo strace -f -o /tmp/apache_strace.log curl -sI 127.0.0.1',
  require  => Service['apache2'],
  creates  => '/tmp/apache_strace.log', # Only run if the log file doesn't exist
}

# Analyze strace output and fix the identified issue
exec { 'fix_apache_issue':
  command  => 'sudo sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  require  => Exec['strace_apache'],
}

# Ensure Apache service is restarted after the fix
service { 'apache2':
  ensure  => 'running',
  enable  => true,
  require => Exec['fix_apache_issue'],
}

