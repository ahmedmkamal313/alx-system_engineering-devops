# 100-puppet_ssh_config.pp

# Use the file resource type to manage the /etc/ssh/ssh_config file
file { '/etc/ssh/ssh_config':
  # Ensure that the file exists and is a regular file
  ensure => file,
  # Use the file_line resource type to add or modify lines in the file
  # Use the match parameter to specify a regular expression to match the existing line
  # Use the line parameter to specify the new line content
  # Use the after parameter to specify where to insert the new line if the match is not found
  # Turn off password authentication
  file_line { 'Turn off passwd auth':
    path  => '/etc/ssh/ssh_config',
    match => '^#?PasswordAuthentication',
    line  => 'PasswordAuthentication no',
  },
  # Declare identity file
  file_line { 'Declare identity file':
    path  => '/etc/ssh/ssh_config',
    match => '^#?IdentityFile',
    line  => 'IdentityFile ~/.ssh/school',
    after => 'Host *',
  },
}

